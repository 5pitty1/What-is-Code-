import re
import numpy as np
from matplotlib import pyplot as plt
import random
from math import exp, log
import pandas as pd
import sys

import dataloader
import pca


# Create a map from semantic to image
def buildImageMap():
    # Load and match filenames to images
    images, labels = dataloader.load_data()
    labeledImages = list(zip(labels, images))
    labeledImages.sort(key=lambda tup: tup[0])

    imageMap = {}
    for label, image in labeledImages:
        # Parse semantic from filename
        semantic = re.search(r"_([a-z]*)\d*.", label).groups()[0]

        # Map semantic to list of images
        if semantic not in imageMap:
            imageMap[semantic] = []
        imageMap[semantic].append((image, semantic))

    # Remove neutral emotion
    imageMap.pop("n")

    return imageMap


# Create a figure to display 6 emotions
def displaySixEmotions(imageMap):
    # Get 6 Emotions
    sixEmotions = []
    for semantic in imageMap:
        image, semantic = imageMap[semantic][0]
        sixEmotions.append(image)
    sixEmotions = sixEmotions[:6]

    # Show 6 Emotions
    fig, axs = plt.subplots(1, 6, sharey=True, gridspec_kw={"hspace": 0})
    fig.suptitle("Six Emotions")
    for i, img in enumerate(sixEmotions):
        axs[i].plot(1, 6, i + 1)
        axs[i].imshow(img, cmap="gray")

    plt.savefig("6 Emotions.png")


class LogisticModel:
    def __init__(self, semantic1, semantic2, learning_rate, dimensions):
        self.semantic1 = semantic1
        self.semantic2 = semantic2
        self.learning_rate = learning_rate
        self.dimensions = dimensions
        self.PCA = None
        self.weights = None
        self.epochError = None

    # Build train/validate/test division in a random order
    def splitData(self, imageMap):
        testpair = random.sample(range(0, 10), 2)
        smallImageMap = {
            self.semantic1: imageMap[self.semantic1],
            self.semantic2: imageMap[self.semantic2],
        }

        model_set = {}
        test_set = []
        for semantic, images in smallImageMap.items():
            model_set[semantic] = [x for i, x in enumerate(images) if i not in testpair]
            test_set += [x for i, x in enumerate(images) if i in testpair]

        return model_set, test_set

    def splitModelSet(self, model_set):
        holdout = random.sample(range(0, 8), 2)
        training_set = []
        validation_set = []
        for semantic, images in model_set.items():
            training_set += [x for i, x in enumerate(images) if i not in holdout]
            validation_set += [x for i, x in enumerate(images) if i in holdout]

        return training_set, validation_set

    def loadPCA(self, training_set):
        # Load training set into pca
        self.PCA = pca.PCA(self.dimensions)
        images = [image for image, semantic in training_set]
        self.PCA.fit(np.array(images))

    def getReducedImage(self, image):
        reduced = self.PCA.transform(np.array(image))
        reduced = np.insert(reduced, 0, 1)
        return reduced

    def reduceData(self, training, validation, test):
        for i, (image, semantic) in enumerate(training):
            training[i] = (self.getReducedImage(image), semantic)

        for i, (image, semantic) in enumerate(validation):
            validation[i] = (self.getReducedImage(image), semantic)

        for i, (image, semantic) in enumerate(test):
            test[i] = (self.getReducedImage(image), semantic)

    def sigmoid(self, image):
        return 1 / (1 + exp(-np.dot(image, self.weights)))

    def entropyChange(self, image, semantic):
        sigResult = self.sigmoid(image)

        teacher = 1 if semantic == self.semantic1 else 0
        output = 1 if sigResult > 0.5 else 0
        # print(teacher, output, sigResult)

        return -1 * (teacher - sigResult) * image

    def batchGradientDescent(self, training_set, validation_set, epoch):
        # Initialize model by setting weights to zero
        self.weights = np.zeros(self.dimensions + 1)

        # Keep track of the weights with the least error
        best_weights = self.weights
        best_error = self.validateModel(self.weights, validation_set)

        for t in range(epoch):
            # print("----------------- Epoch", t, "-----------------")
            # Calculate Net Entropy Change
            totalChange = 0
            for image, semantic in training_set:
                totalChange += self.entropyChange(image, semantic)
            self.weights = self.weights - self.learning_rate * totalChange

            # Validate Model
            curr_error = self.validateModel(self.weights, validation_set)
            if curr_error >= best_error:
                self.weights = best_weights
                curr_error = best_error
                # break

            # Update weights and error score
            best_weights = self.weights
            best_error = curr_error
            self.epochError[t].append(best_error)

        return self.weights

    def trainModel(self, epoch, imageMap):
        self.epochError = [[] for i in range(epoch)]
        totalCorrect = 0
        totalAttempted = 0

        print(
            "Training model on",
            dataloader.emotion_dict[self.semantic1],
            "and",
            dataloader.emotion_dict[self.semantic2],
            "with",
            self.dimensions,
            "principal components...",
            end="",
        )
        for i in range(5):

            # Train/Validate/Test Splitting with 60/20/20 Ratio
            model_set, test_set = self.splitData(imageMap)
            training_set, validation_set = self.splitModelSet(model_set)

            # Load training set into the PCA and reduce all images to the PCA
            self.loadPCA(training_set)
            self.reduceData(training_set, validation_set, test_set)

            # Train model
            self.batchGradientDescent(training_set, validation_set, epoch)

            # Test Model
            numCorrect, numAttempted = self.testModel(test_set)
            totalCorrect += numCorrect
            totalAttempted += numAttempted
        print("Complete")
        print("Total Correct:", totalCorrect)
        print("Total Attempted:", totalAttempted)
        print("Percent Correct: ", totalCorrect / totalAttempted * 100, "%")

    def validateModel(self, weight, validation_set):
        totalEntropy = 0
        for image, semantic in validation_set:
            sigResult = self.sigmoid(image)

            teacher = 1 if semantic == self.semantic1 else 0

            totalEntropy += teacher * log(sigResult)
            totalEntropy += (1 - teacher) * log(1 - sigResult)

        return totalEntropy / -len(validation_set)

    def testModel(self, test_set):
        numAttempted = 0
        numCorrect = 0
        for image, semantic in test_set:
            sigResult = self.sigmoid(image)

            teacher = 1 if semantic == self.semantic1 else 0
            output = 1 if sigResult > 0.5 else 0
            if teacher == output:
                numCorrect += 1
            numAttempted += 1

        return numCorrect, numAttempted

    def plotError(self, epoch):

        errorMatrix = np.matrix(self.epochError).T
        means = np.mean(errorMatrix, axis=0)
        means = np.squeeze(np.asarray(means))
        stds = np.std(errorMatrix, axis=0)
        stds = np.squeeze(np.asarray(stds))

        plt.plot(means, marker="o", color="b")
        plt.fill_between(range(epoch), means - stds, means + stds, alpha=0.1)
        plt.ylabel("Cross-Entropy Cost")
        plt.xlabel("Epoch")
        plt.title(
            "Error Over 10 Epochs with "
            + str(self.dimensions)
            + " Principal Components"
        )
        plt.show()


class SoftmaxModel:
    def __init__(self, learning_rate, dimensions):
        self.semantics = None
        self.learning_rate = learning_rate
        self.dimensions = dimensions
        self.PCA = None
        self.weights = None
        self.epochError = None

    # Build train/validate/test division in a random order
    def splitData(self, imageMap):
        self.semantics = imageMap.keys()
        testpair = random.sample(range(0, 10), 2)
        model_set = {}
        test_set = []
        for semantic, images in imageMap.items():
            model_set[semantic] = [x for i, x in enumerate(images) if i not in testpair]
            test_set += [x for i, x in enumerate(images) if i in testpair]

        return model_set, test_set

    def splitModelSet(self, model_set):
        holdout = random.sample(range(0, 8), 2)
        training_set = []
        validation_set = []
        for semantic, images in model_set.items():
            training_set += [x for i, x in enumerate(images) if i not in holdout]
            validation_set += [x for i, x in enumerate(images) if i in holdout]

        return training_set, validation_set

    def loadPCA(self, training_set):
        # Load training set into pca
        self.PCA = pca.PCA(self.dimensions)
        images = [image for image, semantic in training_set]
        self.PCA.fit(np.array(images))

    def getReducedImage(self, image):
        reduced = self.PCA.transform(np.array(image))
        reduced = np.insert(reduced, 0, 1)
        return reduced

    def reduceData(self, training, validation, test):
        for i, (image, semantic) in enumerate(training):
            training[i] = (self.getReducedImage(image), semantic)

        for i, (image, semantic) in enumerate(validation):
            validation[i] = (self.getReducedImage(image), semantic)

        for i, (image, semantic) in enumerate(test):
            test[i] = (self.getReducedImage(image), semantic)

    def softmax(self, training_images):
        net_input = training_images.dot(self.weights.T)
        return (np.exp(net_input).T / (np.sum(np.exp(net_input), axis=1))).T

    def entropyChange(self, training_images, one_hot):
        sigResult = self.softmax(training_images)

        difference = -1 * (one_hot - sigResult)

        for column in difference.T:
            self.weights = self.weights - self.learning_rate * column.dot(
                training_images
            )

    def stochasticGradientDescent(self, training_set, validation_set, epoch):

        # Initialize model by setting weights to zero
        self.weights = np.zeros((len(self.semantics), self.dimensions + 1))

        # Keep track of the weights with the least error
        best_weights = self.weights
        # best_error = self.validateModel(self.weights, validation_set)

        for t in range(1):  # epoch
            print("----------------- Epoch", t, "-----------------")
            # Calculate Net Entropy Change
            training_images, training_semantics = zip(*training_set)
            one_hot = pd.get_dummies(training_semantics).to_numpy()
            training_images = np.array(training_images)

            self.entropyChange(training_images, one_hot)

            # Validate Model
            curr_error = self.validateModel(self.weights, validation_set)
            if curr_error >= best_error:
                self.weights = best_weights
                curr_error = best_error
                # break

            # Update weights and error score
            best_weights = self.weights
            best_error = curr_error
            self.epochError[t].append(best_error)
        return self.weights

    def trainModel(self, epoch, imageMap):
        self.epochError = [[] for i in range(epoch)]
        totalCorrect = 0
        totalAttempted = 0

        print(
            "Training model with a learning rate of",
            self.learning_rate,
            "and with",
            self.dimensions,
            "principal components...",
        )
        # for i in range(5):

        # Train/Validate/Test Splitting with 60/20/20 Ratio
        model_set, test_set = self.splitData(imageMap)
        training_set, validation_set = self.splitModelSet(model_set)

        # Load training set into the PCA and reduce all images to the PCA
        self.loadPCA(training_set)
        self.reduceData(training_set, validation_set, test_set)

        # Train model
        self.stochasticGradientDescent(training_set, validation_set, epoch)

        # # Test Model
        # numCorrect, numAttempted = self.testModel(test_set)
        # totalCorrect += numCorrect
        # totalAttempted += numAttempted

        print("Complete")
        # print("Total Correct:", totalCorrect)
        # print("Total Attempted:", totalAttempted)
        # print("Percent Correct: ", totalCorrect / totalAttempted * 100, "%")

    def validateModel(self, weight, validation_set):
        totalEntropy = 0
        for image, semantic in validation_set:
            sigResult = self.softmax(image)

            teacher = 1 if semantic == self.semantic1 else 0

            totalEntropy += teacher * log(sigResult)
            totalEntropy += (1 - teacher) * log(1 - sigResult)

        return totalEntropy / -len(validation_set)

    def testModel(self, test_set):
        numAttempted = 0
        numCorrect = 0
        for image, semantic in test_set:
            sigResult = self.softmax(image)

            teacher = 1 if semantic == self.semantic1 else 0
            output = 1 if sigResult > 0.5 else 0
            if teacher == output:
                numCorrect += 1
            numAttempted += 1

        return numCorrect, numAttempted

    def plotError(self, epoch):

        errorMatrix = np.matrix(self.epochError).T
        means = np.mean(errorMatrix, axis=0)
        means = np.squeeze(np.asarray(means))
        stds = np.std(errorMatrix, axis=0)
        stds = np.squeeze(np.asarray(stds))

        plt.plot(means, marker="o", color="b")
        plt.fill_between(range(epoch), means - stds, means + stds, alpha=0.1)
        plt.ylabel("Cross-Entropy Cost")
        plt.xlabel("Epoch")
        plt.title(
            "Error Over 10 Epochs with "
            + str(self.dimensions)
            + " Principal Components"
        )
        plt.show()


def evaluateLogistic(semantic1, semantic2, learning_rate, dimensions):
    epoch = 10

    # Map semantics to list of images
    imageMap = buildImageMap()

    # Create logistic regression model
    model = LogisticModel(semantic1, semantic2, learning_rate, dimensions)

    model.trainModel(epoch, imageMap)

    model.plotError(epoch)


def evaluateSoftmax(learning_rate, dimensions):
    epoch = 20

    # Map semantics to list of images
    imageMap = buildImageMap()

    # Create logistic regression model
    model = SoftmaxModel(learning_rate, dimensions)

    model.trainModel(epoch, imageMap)

    # model.plotError(epoch)

