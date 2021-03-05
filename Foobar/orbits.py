from math import factorial
from fractions import gcd

# Combinatorial choose function
def ncr(n, r):
    return factorial(n) / (factorial(r) * factorial(n - r))


# Returns a list of integer partitions of TARGET
def getPartitions(target, maxValue, partition):
    if target == 0:
        return [partition]

    result = []
    if maxValue > 1:
        result += getPartitions(target, maxValue - 1, partition)
    if maxValue <= target:
        result += getPartitions(target - maxValue, maxValue, (maxValue,) + partition)

    return result


# Given a transformation in the form row and column permutations, partitioned into subgroups, calculates
# the number of matrix states that stay fixed is 2 raised to the sum of the gcd's of each pair of row
# and column subgroups
def getNumFixedMatrices(rowPartition, colPartition, s):
    total = 0
    for colGroup in colPartition:
        for rowGroup in rowPartition:
            total += gcd(colGroup, rowGroup)

    return s ** total


# Calculates the number of transformations that have the underlying structure of the partition of
# rows and columns. Treats each subgroup as a k-cycle symmetric group and we calculate how many
# permutations are k-cycles where k is the length of a subgroup.
def getNumTransformations(rowPartition, colPartition, w, h):
    total = 1

    rowDuplicates = {}
    numRows = h
    for rowGroup in rowPartition:
        if rowGroup != 1:
            total *= ncr(numRows, rowGroup) * factorial(rowGroup - 1)
            if rowGroup not in rowDuplicates:
                rowDuplicates[rowGroup] = 0
            rowDuplicates[rowGroup] += 1
            numRows -= rowGroup

    for val in rowDuplicates.values():
        total /= factorial(val)

    colDuplicates = {}
    numCols = w
    for colGroup in colPartition:
        if colGroup != 1:
            total *= ncr(numCols, colGroup) * factorial(colGroup - 1)
            if colGroup not in colDuplicates:
                colDuplicates[colGroup] = 0
            colDuplicates[colGroup] += 1

            numCols -= colGroup

    for val in colDuplicates.values():
        total /= factorial(val)

    return total


# In order to calculate the number of orbits most efficiently, we utilize Burnside's Lemma.
# To do so, we need to define our matrix states, and what actions we can
# apply onto a matrix. Rather than thinking of an action as swapping two
# rows or two columns, it is equivalent to have an action be a permutation
# of rows and a permutation of columns. This is because, by performing enough swaps,
# we can reach any permutation of rows and columns.
# Then for each permutation, we find the number of matrices that don't change
# after applying that permutation. (Which we can optimize by grouping permutations
# by their underlying structure of k-cycles).
# Given all this information, we can use Burnside's lemma to sum over the number of
# fixed states for each permutation and divide by the number of permutations to
# get the number of orbits.
def solution(w, h, s):

    rowPartitions = getPartitions(h, h, ())
    colPartitions = getPartitions(w, w, ())

    partitionMap = {}
    for rowPartition in rowPartitions:
        for colPartition in colPartitions:
            partitionMap[(rowPartition, colPartition)] = (
                getNumFixedMatrices(rowPartition, colPartition, s),
                getNumTransformations(rowPartition, colPartition, w, h),
            )

    total = 0
    for numStates, numTransformations in partitionMap.values():
        total += numStates * numTransformations

    total /= factorial(h) * factorial(w)
    return total


print(solution(12, 12, 20))
