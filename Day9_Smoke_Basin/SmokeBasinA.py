FILE_NAME = "input9.txt"

def main():
	input_file = open(FILE_NAME)
	input = input_file.read().splitlines()
	input_file.close()

	low_points_counter = 0

	for row, line in enumerate(input):
		for column, _ in enumerate(line):
			higher_then_top = False
			higher_then_left = False
			higher_then_right = False
			higher_then_bottom = False

			if row == 0:
				higher_then_top = True
			else:
				higher_then_top = input[row][column] < input[row-1][column]

			if row == len(input) - 1:
				higher_then_bottom = True
			else:
				higher_then_bottom = input[row][column] < input[row+1][column]
			
			if column == 0:
				higher_then_left = True
			else:
				higher_then_left = input[row][column] < input[row][column-1]

			if column == len(line) - 1:
				higher_then_right = True
			else:
				higher_then_right = input[row][column] < input[row][column+1]
			
			if higher_then_bottom and higher_then_left and higher_then_right and higher_then_top:
				low_points_counter += 1 + int(input[row][column])
		
	print(low_points_counter)

if __name__ == "__main__":
	main()