#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#include "../input/getInput.h"

#define BitsNumber 12
#define FileName "input3.txt"

char mostCommonBitInPosition(int position, char **listOfBitsWord, int size);
char **removeFrom(char **array, char bit, int bitToCheck, int* size);
int binaryToInt(char *binary);

int main(int argc, char *argv[]) {
	int sizeCarbonDioxide = 0;
	char **carbonDioxideScrubberRating = getInput(FileName, &sizeCarbonDioxide);
	
	int i = 0;
	
	while(sizeCarbonDioxide != 1 && i < BitsNumber) {
		char mostCommonBit = mostCommonBitInPosition(i, carbonDioxideScrubberRating, sizeCarbonDioxide);
		if(mostCommonBit == '2') mostCommonBit = '1';
		
		carbonDioxideScrubberRating = removeFrom(carbonDioxideScrubberRating, mostCommonBit, i, &sizeCarbonDioxide);	
		i++;
	}

	int carbonDioxideRating = binaryToInt(carbonDioxideScrubberRating[0]);
	destroyInput(carbonDioxideScrubberRating, sizeCarbonDioxide);

	int sizeOxygen = 0;
	char **oxygenGeneratorRating = getInput(FileName, &sizeOxygen);
	
	i = 0;

	while(sizeOxygen != 1 && i < BitsNumber) {
		char leastCommonBit;
		char mostCommonBit = mostCommonBitInPosition(i, oxygenGeneratorRating, sizeOxygen);

		if(mostCommonBit == '1') leastCommonBit = '0';
		else if(mostCommonBit == '0') leastCommonBit = '1';
		else leastCommonBit = '0';
			
		oxygenGeneratorRating = removeFrom(oxygenGeneratorRating, leastCommonBit, i, &sizeOxygen);	
		i++;
	}

	int oxygenRating = binaryToInt(oxygenGeneratorRating[0]);

	destroyInput(oxygenGeneratorRating, sizeOxygen);

	printf("%d\n", carbonDioxideRating * oxygenRating);

	return 0;
}

char mostCommonBitInPosition(int position, char **listOfBitsWord, int size) {
	int oneCounter = 0;
	int zeroCounter = 0;

	for(int j = 0; j < size; j++)
		if(listOfBitsWord[j][position] == '1') oneCounter++;
		else zeroCounter++;

	if(zeroCounter > oneCounter) 
		return '0';
	else if(oneCounter > zeroCounter)
		return '1';
	else return '2';
}

char **removeFrom(char **array, char bit, int bitToCheck, int* size) {
	int newSize = 0;
	for(int i = 0; i < *size; i++) {
		if(array[i][bitToCheck] != bit) {
			array[newSize] = array[i];
			newSize++;
		} else free(array[i]);
	}
	*size = newSize;
	return realloc(array, (newSize * sizeof(char*)));
}

int binaryToInt(char *binary) {
	int result = 0;

	for(int i = 0; i < strlen(binary); i++)
		if(binary[i] == '1') 
			result += pow(2, (strlen(binary)-1) - (i+1));
	

	return result;
}