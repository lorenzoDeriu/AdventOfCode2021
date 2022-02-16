FILE_NAME = "input9.txt"

class Position:
	def __init__(self, new_X: int, new_Y: int) -> None:
		self.x = new_X
		self.y = new_Y

class Cell:
	def __init__(self, new_high: int) -> None:
		self.high = new_high
		self.visited = False

	def visit(self) -> None:
		self.visited = True

def main():
	input_file = open(FILE_NAME)
	input = input_file.read().splitlines()
	input_file.close()

	low_points = low_point_detection(input)

	grid = [[Cell(int(high)) for high in row] for row in input]

	basin = []

	for low_point in low_points:
		queue = [low_point]
		basin_size = 0
		
		grid[low_point.x][low_point.y].visit()

		while len(queue) != 0:
			basin_size += 1
			pos = queue.pop()

			if pos.x != 0:
				if (not grid[pos.x - 1][pos.y].visited) and (grid[pos.x - 1][pos.y].high != 9):
					grid[pos.x - 1][pos.y].visit()
					queue.append(Position(pos.x - 1, pos.y))
			
			if pos.x != len(grid)-1:
				if (not grid[pos.x + 1][pos.y].visited) and (grid[pos.x + 1][pos.y].high != 9):
					grid[pos.x + 1][pos.y].visit()
					queue.append(Position(pos.x + 1, pos.y))
			
			if pos.y != 0:
				if (not grid[pos.x][pos.y - 1].visited) and (grid[pos.x][pos.y - 1].high != 9):
					grid[pos.x][pos.y - 1].visit()
					queue.append(Position(pos.x, pos.y - 1))
			
			if pos.y != len(grid[0])-1:
				if (not grid[pos.x][pos.y + 1].visited) and (grid[pos.x][pos.y + 1].high != 9):
					grid[pos.x][pos.y + 1].visit()
					queue.append(Position(pos.x, pos.y + 1))
		
		basin.append(basin_size)
	
	basin = sorted(basin, key = None, reverse = True)
	print(basin[0] * basin[1] * basin[2])

def low_point_detection(input: list) -> list:
	low_points_list = []

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
				low_points_list.append(Position(row, column))
	return low_points_list

if __name__ == "__main__":
	main()