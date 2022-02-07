FILE_NAME = "input5.txt"

inputFile = open(FILE_NAME)
input = inputFile.read().split("\n")
inputFile.close()

class Position:
	def __init__(self, newX, newY):
		self.x = int(newX)
		self.y = int(newY)

	def __eq__(self, other):
		return self.x == other.x and self.y == other.y

class Line:
	def __init__(self, newStartPosition, newEndPosition):
		self.startPosition = newStartPosition
		self.endPosition = newEndPosition

def main():
	lineList = buildLineList(input)
	high, width = getMax_X(lineList)+1, getMax_Y(lineList)

	grid = [[0 for w in range(width + 1)] for h in range(high + 1)]

	for line in lineList:
		currentPosition = line.startPosition

		while(currentPosition != None):
			updateGrid(grid, currentPosition)
			currentPosition = getNextPosition(line, currentPosition)
	
	counter = 0

	for row in grid:
		for number in row:
			if number >= 2:
				counter += 1
	
	print(counter)

def buildLineList(input):
	lineList = []
	for line in input:
		linePosition = line.replace(" -> ", ",").split(",")
		startPosition = Position(linePosition[0], linePosition[1])
		endPosition = Position(linePosition[2], linePosition[3])

		newLine = Line(startPosition, endPosition)
		lineList.append(newLine)

	return lineList

def getMax_X(lineList):
	max = lineList[0].startPosition.x
	for line in lineList:
		if max < line.startPosition.x: max = line.startPosition.x
		elif max < line.endPosition.x: max = line.endPosition.x

	return max

def getMax_Y(lineList):
	max = lineList[0].startPosition.y
	for line in lineList:
		if max < line.startPosition.y: max = line.startPosition.y
		elif max < line.endPosition.y: max = line.endPosition.y

	return max

def updateGrid(grid, positionToUpdate):
	grid[positionToUpdate.x][positionToUpdate.y] += 1

def getNextPosition(line, currentPosition):
	if currentPosition == line.endPosition:
		return None
	return Position(updateCoordinate(currentPosition.x, line.endPosition.x), updateCoordinate(currentPosition.y, line.endPosition.y))

def updateCoordinate(currentCoordinate, target):
	if currentCoordinate < target:
		currentCoordinate += 1
	elif currentCoordinate > target:
		currentCoordinate -= 1
	return currentCoordinate

if __name__ == "__main__":
	main()