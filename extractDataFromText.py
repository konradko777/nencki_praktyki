def readDataFromIteration(nameOfTextFile):
	textFile = open(nameOfTextFile, 'r')
	values = [None]*4
	for i in range(0,4):
		line = textFile.readline()
		numericValue = line.split('=')[1].strip()
		values[i] = numericValue
	print values

readDataFromIteration("iter1.txt")
