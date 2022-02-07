#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

#include "../input/getInput.h"

#define FileName "input5.txt"

typedef struct point {
	int x;
	int y;
} Point;

typedef struct line {
	Point startPoint;
	Point endPoint;
} Line;

bool isPerpendicular(Line);
Line *getPerpendicularLineArray(char**,int,size_t*);
int maxVertical(Line*,int);
int maxHorizontal(Line*,int);
void updateGrid(int**,Line);

int main(int argc, char **argv) {
	int inputSize = 0;
	char **input = getInput(FileName, &inputSize);

	size_t size;
	Line *perpendicularLine = getPerpendicularLineArray(input, inputSize, &size);

	destroyInput(input, inputSize);

	size_t verticalSize = (size_t) maxVertical(perpendicularLine, size) + 1;
	size_t horizontalSize = (size_t) maxHorizontal(perpendicularLine, size) + 1;

	int **grid = malloc(verticalSize * sizeof(int *));
	for(int i = 0; i < verticalSize; i++)
		grid[i] = calloc(horizontalSize, sizeof(int));

	for(int i = 0; i < size; i++)
		updateGrid(grid, perpendicularLine[i]);
	
	free(perpendicularLine);

	int dangerousZoneCounter = 0;
	for(int i = 0; i < verticalSize; i++)
		for(int j = 0; j < horizontalSize; j++)
			if(grid[i][j] >= 2) dangerousZoneCounter++;
		
	printf("%d\n", dangerousZoneCounter);

	for(int i = 0; i < verticalSize; i++)
		free(grid[i]);
	free(grid);
	

	return 0;
}

int maxVertical(Line* lineArray, int size) {
	if(size == 0) return 0;
	
	int max = lineArray[0].startPoint.y;
	
	for(int i = 0; i < size; i++)
		if(max < lineArray[i].startPoint.y) max = lineArray[i].startPoint.y;
		else if(max < lineArray[i].endPoint.y) max = lineArray[i].endPoint.y;

	return max;
}

int maxHorizontal(Line* lineArray, int size) {
	if(size == 0) return 0;
	
	int max = lineArray[0].startPoint.x;
	
	for(int i = 0; i < size; i++)
		if(max < lineArray[i].startPoint.x) max = lineArray[i].startPoint.x;
		else if(max < lineArray[i].endPoint.x) max = lineArray[i].endPoint.x;

	return max;
}

bool isPerpendicular(Line line) {
	return (line.startPoint.x == line.endPoint.x) || (line.startPoint.y == line.endPoint.y);
}

Line *getPerpendicularLineArray(char** input, int inputSize, size_t* size) {
	*size = 10;
	Line *array = malloc(*size * sizeof(Line));

	int index = 0;

	for(int i = 0; i < inputSize; i++) {
		Line newLine;

		newLine.startPoint.x = atoi(strtok(input[i], ", ->"));
		newLine.startPoint.y = atoi(strtok(NULL, ", ->"));
		
		newLine.endPoint.x = atoi(strtok(NULL, ", ->"));
		newLine.endPoint.y = atoi(strtok(NULL, ", ->"));

		if(isPerpendicular(newLine)) {
			array[index] = newLine;
			index++;

			if(index == (int) (*size)) {
				*size *= 2;
				
				array = realloc(array, *size * sizeof(Line));
			}
		}
	}

	*size = index;
	array = realloc(array, *size * sizeof(Line));

	return array;
}

bool isGoingVertical(Line line) {
	return line.startPoint.x == line.endPoint.x;
}

bool isGoingForward(Line line) {
	return isGoingVertical(line) ? (line.startPoint.y < line.endPoint.y) : (line.startPoint.x < line.endPoint.x);
}

Point getNextPoint(Point point, bool isGoingVertical, bool isGoingForward) {
	if(isGoingVertical)
		if(isGoingForward) point.y++;
		else point.y--;
	else
		if(isGoingForward) point.x++;
		else point.x--;
	
	return point;
}

void updateGrid(int** grid, Line newLine) {
	Point currentPoint = newLine.startPoint;
	while(currentPoint.x != newLine.endPoint.x || currentPoint.y != newLine.endPoint.y) {
		grid[currentPoint.x][currentPoint.y] += 1;

		currentPoint = getNextPoint(currentPoint, isGoingVertical(newLine), isGoingForward(newLine));
	}
	grid[newLine.endPoint.x][newLine.endPoint.y] += 1;
}
