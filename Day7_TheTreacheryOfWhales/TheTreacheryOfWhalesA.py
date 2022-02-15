FILE_NAME = "input7.txt"

def main():
	input_file = open(FILE_NAME)
	crab_position = input_file.read().split(",")
	input_file.close()

	for index, position in enumerate(crab_position):
		crab_position[index] = int(position)

	sum = 0
	for position in crab_position:
		sum += position

	AVG = int(sum / len(crab_position)) # starting point

	if compute_fuel(crab_position, AVG) < compute_fuel(crab_position, AVG + 1):
		if compute_fuel(crab_position, AVG) < compute_fuel(crab_position, AVG - 1):
			print("result: {}".format(compute_fuel(crab_position, AVG)))
		else:
			i = 1
			while compute_fuel(crab_position, AVG - i) > compute_fuel(crab_position, AVG - (i + 1)):
				i += 1
			print("result: {}".format(compute_fuel(crab_position, AVG - i)))
	else:
		i = 1
		while compute_fuel(crab_position, AVG + i) > compute_fuel(crab_position, AVG + (i + 1)):
			i += 1
		print("result: {}".format(compute_fuel(crab_position, AVG + i)))

def compute_fuel(position_list: list, target: int) -> int:
	fuel = 0
	for position in position_list:
		fuel += abs(target - position)
	
	return fuel

if __name__ == "__main__":
	main()