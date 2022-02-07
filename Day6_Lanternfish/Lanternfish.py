FILE_NAME = "input6.txt"
# NUMBER_OF_DAYS = 80 part 1
NUMBER_OF_DAYS = 256 # part 2

def main():
	inputFile = open(FILE_NAME)
	input = inputFile.read()
	inputFile.close()

	initialState = input.split(',')

	fishInDay = [0 for i in range(9)]
	for state in initialState:
		fishInDay[int(state)] += 1
	
	for _ in range(NUMBER_OF_DAYS):
		deadFish = fishInDay[0]

		for i in range(8):
			fishInDay[i] = fishInDay[i + 1]

		fishInDay[8] = deadFish
		fishInDay[6] += deadFish

	totalFish = 0

	for day in fishInDay:
		totalFish += day

	print(totalFish)

if __name__ == "__main__":
	main()