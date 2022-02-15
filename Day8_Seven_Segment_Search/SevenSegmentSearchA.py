FILE_NAME = "input8.txt"
SEARCHED_SEGMENGTS_LENGHT = [2,4,3,7]

def main():
	input_file = open(FILE_NAME)
	input = input_file.read().split("\n")
	input_file.close()

	counter = 0
	
	for index, row in enumerate(input):
		input[index] = row.split("| ")[1].split(" ")
		counter = updateCounter(input[index], counter)
	
	print(counter)

def updateCounter(array: list, counter: int) -> int:
	for word in array:
		if len(word) in SEARCHED_SEGMENGTS_LENGHT:
			counter += 1
	return counter

if __name__ == "__main__":
	main()