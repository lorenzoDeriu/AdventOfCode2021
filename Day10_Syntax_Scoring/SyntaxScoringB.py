from collections import deque

FILE_NAME = "input10.txt"

OPEN  = ["(", "{", "[", "<"]
CLOSE = [")", "}", "]", ">"]
SCORE = {
	"(": 1,
	"[": 2,
	"{": 3,
	"<": 4
}

def main():
	input_file = open(FILE_NAME)
	input = input_file.read().splitlines()
	input_file.close()

	score = []

	for line in input:
		open_bracket = deque()
		incomplete = True

		for bracket in line:
			if is_open(bracket):
				open_bracket.append(bracket)
			elif not bracket_pair(open_bracket.pop(), bracket):
				incomplete = False
	
		if incomplete:
			open_bracket.reverse()
			line_score = get_score(open_bracket)
			score.append(line_score)

	print(median(score))

def is_open(bracket: str) -> bool:
	return bracket in OPEN

def bracket_pair(open_bracket: str, closed_bracket: str) -> bool:
	return OPEN.index(open_bracket) == CLOSE.index(closed_bracket)

def get_score(missing_bracket: list[str]) -> int:
	score = 0

	for bracket in missing_bracket:
		score = (score * 5) + SCORE[bracket]

	return score

def median(integer_list: list[int]) -> int:
	integer_list_sorted = sorted(integer_list)

	return integer_list_sorted[len(integer_list_sorted) // 2]

if __name__ == "__main__":
	main()


