FILE_NAME = "input8.txt"

def main():
    inputFile = open(FILE_NAME)
    input = inputFile.read().split("\n")
    inputFile.close()

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

        effectiveNumbers = ['' for _ in range(10)]
        
        effectiveNumbers[1] = rule[0]
        effectiveNumbers[7] = rule[1]
        effectiveNumbers[4] = rule[2]
        effectiveNumbers[8] = rule[9]

        for r in rule:
            if len(r) == 5:
                if getSegmentsInCommon(r, effectiveNumbers[1]) == 2:
                    effectiveNumbers[3] = r
                elif getSegmentsInCommon(r, effectiveNumbers[4]) == 2:
                    effectiveNumbers[2] = r
                elif getSegmentsInCommon(r, effectiveNumbers[4]) == 3:
                    effectiveNumbers[5] = r
            
            if len(r) == 6:
                if getSegmentsInCommon(r, effectiveNumbers[3]) == 5:
                    effectiveNumbers[9] = r
                elif getSegmentsInCommon(r, effectiveNumbers[1]) == 2:
                    effectiveNumbers[0] = r
                elif getSegmentsInCommon(r, effectiveNumbers[1]) == 1:
                    effectiveNumbers[6] = r

        strNumber = ""
        for digit in number:
            strNumber += str(effectiveNumbers.index(digit))
        result += int(strNumber)

    print(result)
   
def getSegmentsInCommon(str1, str2):
    numberOfSignal = 0
    for char in str1:
        if(char in str2):
            numberOfSignal += 1
    return numberOfSignal

if __name__ == "__main__":
    main()