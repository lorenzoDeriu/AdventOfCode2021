#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "../input/getInput.h"

int main(int argc, char *argv[]) {
	int size = 0;
	char **testArray = getInput("input1.txt", &size);
	
	int previous = atoi(testArray[0]);
	int current;
	int counter = 0;

	for(int i = 1; i < size; i++) {
		current = atoi(testArray[i]);
		if(current > previous) counter++;

		previous = current;
	}

	destroyInput(testArray, size);

	printf("%d\n", counter);
	
	return 0;
}