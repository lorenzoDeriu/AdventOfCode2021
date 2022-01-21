#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#include "../input/getInput.h"

int binaryToInt(char*); 

int main(int argc, char **argv) {
	int size = 0;
	char **input = getInput("input3.txt", &size);

	int zeroCounter = 0;
	int oneCounter = 0;

	int sizeOfBitWord = strlen(input[0])-1;

	char *mostCommonBit = malloc(sizeOfBitWord);
	char *lessCommonBit = malloc(sizeOfBitWord);

	for(int i = 0; i < sizeOfBitWord; i++) {
		for(int j = 0; j < size; j++)
			if(input[j][i] == '1') oneCounter++;
			else zeroCounter++;
		
		if(oneCounter > zeroCounter) {
			mostCommonBit[i] = '1';
			lessCommonBit[i] = '0';
		} else {
			mostCommonBit[i] = '0';
			lessCommonBit[i] = '1';
		}

		oneCounter = 0;
		zeroCounter = 0;
	}

	destroyInput(input, size);

	int gamma = binaryToInt(mostCommonBit);
	int epsilon = binaryToInt(lessCommonBit);
	free(mostCommonBit);
	free(lessCommonBit);

	int powerConsumption = epsilon * gamma;
	printf("%d\n", powerConsumption);

	return 0; 
}

int binaryToInt(char *binary) {
	int result = 0;

	for(int i = 0; i < strlen(binary); i++) {
		if(binary[i] == '1') result += pow(2, strlen(binary) - (i+1));
	}

	return result;
}