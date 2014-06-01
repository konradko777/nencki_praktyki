def readDataFromIteration(nameOfTextFile):
	textFile = open(nameOfTextFile, 'r')
	for line in textFile:
		print line


readDataFromIteration("iter1.txt")
