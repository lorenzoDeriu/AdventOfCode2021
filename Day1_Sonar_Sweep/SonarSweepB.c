#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "../input/getInput.h"

int *convertToInt(char **, int );

int main(int argc, char *argv[]) {
	int size = 0;
	int *input = convertToInt(getInput("input2.txt", &size), size);
	
	int previous = -1;
	int current;

	int counter = 0;

	for(int i = 0; i < size - 2; i++) {
		current = input[i] + input[i + 1] + input[i + 2];
		
		if(current > previous && previous != -1) 
			counter++;

		previous = current;
	}

	free(input);

	printf("%d\n", counter);
	
	return 0;
}

int *convertToInt(char **stringArray, int size) {
	int *intArray = malloc (size * sizeof(int));

	for(int i = 0; i < size; i++)
		intArray[i] = atoi(stringArray[i]);

	destroyInput(stringArray, size);

	return intArray;
}