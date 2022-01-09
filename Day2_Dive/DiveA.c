#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "../input/getInput.h"

typedef struct {
	int progression;
	int depth;
} Position;

int main(int argc, char *argv[]) {
	int size = 0;
	char **input = getInput("input2A.txt", &size);

	Position position;
	position.progression = 0;
	position.depth = 0;

	for(int i = 0; i < size; i++) {
		char *command = strtok(input[i], " "); 
		int meter = atoi(strtok(NULL, " "));

		if(strcmp(command, "forward") == 0)
			position.progression += meter;
		else if(strcmp(command, "down") == 0)
			position.depth += meter;
		else position.depth -= meter;
	}

	destroyInput(input, size);

	fprintf(stdout, "%d\n", (position.progression * position.depth));
	return 0;
}