FILE_NAME = "input6.txt"
# NUMBER_OF_DAYS = 80 part 1
NUMBER_OF_DAYS = 256 # part 2

def main():
	input_file = open(FILE_NAME)
	input = input_file.read()
	input_file.close()

	initial_state = input.split(',')

	fish_in_day = [0 for i in range(9)]
	for state in initial_state:
		fish_in_day[int(state)] += 1
	
	for _ in range(NUMBER_OF_DAYS):
		dead_fish = fish_in_day[0]

		for i in range(8):
			fish_in_day[i] = fish_in_day[i + 1]

		fish_in_day[8] = dead_fish
		fish_in_day[6] += dead_fish

	total_fish = 0

	for number_of_fish in fish_in_day:
		total_fish += number_of_fish

	print(total_fish)

if __name__ == "__main__":
	main()