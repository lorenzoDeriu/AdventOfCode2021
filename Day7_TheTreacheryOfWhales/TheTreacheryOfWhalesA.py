FILE_NAME = "input7.txt"

def main():
	inputFile = open(FILE_NAME)
	crabPosition = inputFile.read().split(",")
	inputFile.close()

	for index, position in enumerate(crabPosition):
		crabPosition[index] = int(position)

	sum = 0
	for position in crabPosition:
		sum += position

	AVG = int(sum / len(crabPosition)) # starting point

	if computeFuel(crabPosition, AVG) < computeFuel(crabPosition, AVG + 1):
		if computeFuel(crabPosition, AVG) < computeFuel(crabPosition, AVG - 1):
			print("result: {}".format(computeFuel(crabPosition, AVG)))
		else:
			i = 1
			while computeFuel(crabPosition, AVG - i) > computeFuel(crabPosition, AVG - (i + 1)):
				i += 1
			print("result: {}".format(computeFuel(crabPosition, AVG - i)))
	else:
		i = 1
		while computeFuel(crabPosition, AVG + i) > computeFuel(crabPosition, AVG + (i + 1)):
			i += 1
		print("result: {}".format(computeFuel(crabPosition, AVG + i)))

def computeFuel(positionList, target):
	fuel = 0
	for position in positionList:
		fuel += abs(target - position)
	
	return fuel

if __name__ == "__main__":
	main()