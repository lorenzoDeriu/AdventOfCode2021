from collections import deque

FILE_NAME = "input10.txt"

OPEN  = ["(", "{", "[", "<"]
CLOSE = [")", "}", "]", ">"]
SCORE = {
	")": 3,
	"]": 57,
	"}": 1197,
	">": 25137
}

def main():
	input_file = open(FILE_NAME)
	input = input_file.read().splitlines()
	input_file.close()

	score = 0

	for line in input:
		open_bracket = deque()
		for bracket in line:
			if is_open(bracket):
				open_bracket.append(bracket)
			elif not bracket_pair(open_bracket.pop(), bracket):
				score += get_score(bracket)
				continue

	print(score)

def is_open(bracket: str) -> bool:
	return bracket in OPEN

def bracket_pair(open_bracket: str, closed_bracket: str) -> bool:
	return OPEN.index(open_bracket) == CLOSE.index(closed_bracket)

def get_score(bracket: str) -> int:
	return SCORE[bracket]

if __name__ == "__main__":
	main()