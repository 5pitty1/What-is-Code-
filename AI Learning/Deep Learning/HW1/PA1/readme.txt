** Make sure the CAFE directory is in the same directory as the script **

To run the program, load up a python interpreter with the logistic.py script included:
	python3 -i logistic.py

And to call the logistic regression between certain expressions call the evaluateLogistic function:
	Function syntax: evaluateLogistic(semantic1, semantic2, learning_rate, dimensions)

	e.x.
	>> evaluateLogistic("h","m",0.2,8)

To display the 6 emotions, call:
	>> displaySixEmotions(buildImageMap())