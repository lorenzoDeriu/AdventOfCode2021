FILE_NAME = "input11.txt"
NUMBER_OF_STEPS = 100

def main():
	input_file = open(FILE_NAME)
	input = input_file.read().splitlines()
	input_file.close()

	octopus_list = build_octopus_list(input)
	lights_counter = 0

	for i in range(NUMBER_OF_STEPS):
		for octopus in octopus_list:
			octopus.energy_level += 1
			octopus.energy_transmitted = False

		updated = True

		while updated:
			updated = False 
			for octopus in octopus_list:
				if octopus.energy_level > 9 and not octopus.energy_transmitted:
					updated = True
					octopus.energy_transmitted = True
					for near_octopus_index in octopus.near_octopuses:
						octopus_list[near_octopus_index].energy_level += 1

		for octopus in octopus_list:
			if octopus.energy_level > 9:
				octopus.energy_level = 0
				lights_counter += 1

	print(lights_counter)
	return


class Octopus:
	def __init__(self, new_id: int, new_energy_level: int) -> None:
		self.id = new_id
		self.energy_level = new_energy_level
		self.near_octopuses = []
		self.energy_transmitted = False


def build_octopus_list(input: list[str]) -> list[Octopus]:
	id = 0
	matrix = [[None for i in range(10)] for j in range(10)]
	octopus_list = []

	for x, row in enumerate(input):
		for y, energy_level in enumerate(row):
			matrix[x][y] = Octopus(id, int(energy_level))
			id += 1

	for row_index, row in enumerate(matrix):
		for column_index, octopus in enumerate(row):
			list = []
			if row_index != 0:
				list.append(matrix[row_index-1][column_index].id)
				if column_index != 0:
					list.append(matrix[row_index-1][column_index-1].id)
				if column_index != 9:
					list.append(matrix[row_index-1][column_index+1].id)
			if column_index != 0:
				list.append(matrix[row_index][column_index-1].id)
			if column_index != 9:
				list.append(matrix[row_index][column_index+1].id)
			if row_index != 9:
				list.append(matrix[row_index+1][column_index].id)
				if column_index != 0:
					list.append(matrix[row_index+1][column_index-1].id)
				if column_index != 9:
					list.append(matrix[row_index+1][column_index+1].id)

			octopus.near_octopuses = list.copy()
			octopus_list.append(octopus)

	return octopus_list

if __name__ == "__main__":
	main()