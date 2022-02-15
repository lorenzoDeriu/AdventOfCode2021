FILE_NAME = "input8.txt"

def main():
    input_file = open(FILE_NAME)
    input = input_file.read().split("\n")
    input_file.close()

    rules = []
    numbers = []

    for line in input:
        line = line.split(" | ")
        rules.append(line[0].split(" "))
        numbers.append(line[1].split(" "))
    
    result = 0

    for rule, number in zip(rules, numbers):
        rule = sorted(rule, key = len)

        for index, word in enumerate(rule):
            rule[index] = ''.join(sorted(word))
        
        for index, word in enumerate(number):
            number[index] = ''.join(sorted(word)) 

        effective_numbers = ['' for _ in range(10)]
        
        effective_numbers[1] = rule[0]
        effective_numbers[7] = rule[1]
        effective_numbers[4] = rule[2]
        effective_numbers[8] = rule[9]

        for r in rule:
            if len(r) == 5:
                if get_segment_in_common(r, effective_numbers[1]) == 2:
                    effective_numbers[3] = r
                elif get_segment_in_common(r, effective_numbers[4]) == 2:
                    effective_numbers[2] = r
                elif get_segment_in_common(r, effective_numbers[4]) == 3:
                    effective_numbers[5] = r
            
            if len(r) == 6:
                if get_segment_in_common(r, effective_numbers[3]) == 5:
                    effective_numbers[9] = r
                elif get_segment_in_common(r, effective_numbers[1]) == 2:
                    effective_numbers[0] = r
                elif get_segment_in_common(r, effective_numbers[1]) == 1:
                    effective_numbers[6] = r

        strNumber = ""
        for digit in number:
            strNumber += str(effective_numbers.index(digit))
        result += int(strNumber)

    print(result)
   
def get_segment_in_common(str1: str, str2: str) -> int:
    number_of_signal = 0
    for char in str1:
        if(char in str2):
            number_of_signal += 1
    return number_of_signal

if __name__ == "__main__":
    main()