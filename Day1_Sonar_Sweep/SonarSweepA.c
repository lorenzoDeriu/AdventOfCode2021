#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "../input/getInput.h"

int main(int argc, char *argv[]) {
	int size = 0;
	char **input = getInput("input1.txt", &size);
	
	int previous = atoi(input[0]);
	int current;
	int counter = 0;

	for(int i = 1; i < size; i++) {
		current = atoi(input[i]);
		if(current > previous) counter++;

		previous = current;
	}

	destroyInput(input, size);

	printf("%d\n", counter);
	
	return 0;
}