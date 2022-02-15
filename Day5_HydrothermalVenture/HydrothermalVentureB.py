from typing import TypeVar

FILE_NAME = "input5.txt"

input_file = open(FILE_NAME)
input = input_file.read().split("\n")
input_file.close()

Position = TypeVar("Position", bound = "Position")

class Position:
	def __init__(self, new_X: int, new_Y: int) -> None:
		self.x = int(new_X)
		self.y = int(new_Y)

	def __eq__(self, other: Position) -> bool:
		if other == None:
			return False
		return self.x == other.x and self.y == other.y

class Line:
	def __init__(self, new_start_position: Position, new_end_position: Position) -> None:
		self.start_position = new_start_position
		self.end_position = new_end_position

def main():
	line_list = build_line_list(input)
	high, width = get_max_X(line_list)+1, get_max_Y(line_list)

	grid = [[0 for _ in range(width + 1)] for _ in range(high + 1)]

	for line in line_list:
		current_position = line.start_position

		while(current_position != None):
			update_grid(grid, current_position)
			current_position = get_next_position(line, current_position)
	
	counter = 0

	for row in grid:
		for number in row:
			if number >= 2:
				counter += 1
	
	print(counter)

def build_line_list(input: list) -> list:
	line_list = []
	for line in input:
		line_position = line.replace(" -> ", ",").split(",")
		start_position = Position(line_position[0], line_position[1])
		end_position = Position(line_position[2], line_position[3])

		new_line = Line(start_position, end_position)
		line_list.append(new_line)

	return line_list

def get_max_X(line_list: list) -> int:
	max = line_list[0].start_position.x
	for line in line_list:
		if max < line.start_position.x: max = line.start_position.x
		elif max < line.end_position.x: max = line.end_position.x

	return max

def get_max_Y(line_list: list) -> int:
	max = line_list[0].start_position.y
	for line in line_list:
		if max < line.start_position.y: max = line.start_position.y
		elif max < line.end_position.y: max = line.end_position.y

	return max

def update_grid(grid: list, position_to_update: Position):
	grid[position_to_update.x][position_to_update.y] += 1

def get_next_position(line: Line, current_position: Position) -> Position:
	if current_position == line.end_position:
		return None
	return Position(update_coordinate(current_position.x, line.end_position.x), update_coordinate(current_position.y, line.end_position.y))

def update_coordinate(current_coordinate: int, target: int) -> int:
	if current_coordinate < target:
		current_coordinate += 1
	elif current_coordinate > target:
		current_coordinate -= 1
	return current_coordinate

if __name__ == "__main__":
	main()