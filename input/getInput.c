#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "getInput.h"

char **getInput(char *, int *);
void fail(char *);
void destroyInput(char **, int );

char **getInput(char *fileName, int *dim) {
	FILE *inputFile = fopen (fileName, "r");
	
	int size = 10;
	int index = 0;
	char **input = malloc(size * sizeof(char *));

	char *row = malloc(10);

	size_t buffer_size = 200;

	while (!feof(inputFile)) {
		getline(&row, &buffer_size, inputFile);
		if(row != NULL) 
			if(size > index) input[index] = strdup(row);
			else {
				size *= 2;
				input = realloc(input, size * sizeof(char *));
				input[index] = strdup(row);
			}
		else fail("getInput fail tacking new row");

		index++;
	}
	free(row);
	fclose(inputFile);

	size = index;
	input = realloc(input, size * sizeof(char *));

	*dim = size;

	return input;
}

void fail(char *ErrorMessage) {
	fprintf(stderr, "%s\n", ErrorMessage);
	exit(-1);
}

void destroyInput(char **input, int size) {
	for(int i = 0; i < size; i++)
		free(input[i]);
	
	free(input);
}