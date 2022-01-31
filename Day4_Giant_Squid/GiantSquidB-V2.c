#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

#include "../input/getInput.h"

#define BoardDimension 5
#define FileName "input4.txt"

typedef struct {
	int number;
	bool marked;
} Cell;

typedef struct {
	Cell **cell;
} Board;

int *convertToIntagerArray(char *, int *);
Board *buildBoards(char**, int, int*);
Cell *getBoardRow(char*);
void printBoard(Board);
void markCell(Board*, int, int);
bool updateWinner(Board*, int, Board**, int*);
void removeWinner(Board**, int*);
long getScore(Board, int);
bool isWinner(Board);

int main(int argc, char **argv) {
	int inputSize = 0;
	char **input = getInput(FileName, &inputSize);

	int numberOfDrawns = 0;
	int *numberDrawn = convertToIntagerArray(input[0], &numberOfDrawns);

	int numberOfBoard = 0;
	Board *board = buildBoards(input, inputSize, &numberOfBoard);

	destroyInput(input, inputSize);

	Board **winner = malloc(numberOfBoard * sizeof(Board*));
	int numberOfWinner = 0;

	for(int i = 0; i < numberOfDrawns; i++) {
		markCell(board, numberOfBoard, numberDrawn[i]);
		
		if(updateWinner(board, numberOfBoard, winner, &numberOfWinner)) {
			removeWinner(&board, &numberOfBoard);
		}

		if((winner[numberOfWinner - 1] != NULL && numberOfBoard == 0)) {
			printf("Score: %ld\n", getScore(*winner[numberOfWinner-1], numberDrawn[i]));
			break;
		}
	}

	free(numberDrawn);

	for(int i = 0; i < numberOfBoard; i++) {
		for(int j = 0; j < BoardDimension; j++)
			free(board[i].cell[j]);
		free(board[i].cell);
	}
	
	free(board);

	return 0;
} 

int *convertToIntagerArray(char *strArray, int *size) {
	*size = 10;
	int *intagerArray = malloc(*size * sizeof(int));
	int numberInserted = 0;
	
	char *token = strtok(strArray, ",");

	while(token != NULL) {
		intagerArray[numberInserted] = atoi(token);
		numberInserted++;

		if(numberInserted == *size) {
			*size *= 2;
			intagerArray = realloc(intagerArray, *size * sizeof(int));
		}
		
		token = strtok(NULL, ",");
	}

	*size = numberInserted;
	intagerArray = realloc(intagerArray, *size * sizeof(int));

	return intagerArray;
}

Board *buildBoards(char **input, int inputSize, int *numberOfBoards) {
	*numberOfBoards = 10;
	Board *boardsList = malloc(*numberOfBoards * sizeof(Board));
	int boardsCreated = 0;

	for(int i = 2; i < inputSize; i += 6) {
		Cell *boardRow;
		
		boardsList[boardsCreated].cell = malloc(BoardDimension * sizeof(Cell*));
		for(int j = 0; j < BoardDimension; j++) {
			boardRow = getBoardRow(input[i+j]);
			
			boardsList[boardsCreated].cell[j] = boardRow;
		}
		
		boardsCreated++;
		if(boardsCreated == *numberOfBoards) {
			*numberOfBoards *= 2;
			boardsList = realloc(boardsList, *numberOfBoards * sizeof(Board));
		}
	}

	*numberOfBoards = boardsCreated;
	boardsList = realloc(boardsList, *numberOfBoards * sizeof(Board));

	return boardsList;	
}

Cell *getBoardRow(char* row) {
	char *number = strtok(row, " ");

	Cell *numberRow = malloc(BoardDimension * sizeof(Cell));
	int index = 0;

	while(number != NULL) {

		numberRow[index].number = atoi(number);
		numberRow[index].marked = false;
		index++;

		number = strtok(NULL, " ");
	}

	return numberRow;
}

void printBoard(Board board) {
	for(int i = 0; i < BoardDimension; i++) {
		for(int j = 0; j < BoardDimension; j++) 
			printf("%2d ", board.cell[i][j].number);
		printf("\n");
	}
	printf("\n");
}

void markCell(Board *boardList, int numberOfBoard, int numberDrawn) {
	for(int i = 0; i < numberOfBoard; i++) {
		for(int j = 0; j < BoardDimension; j++)
			for(int k = 0; k < BoardDimension; k++)
				if(boardList[i].cell[j][k].number == numberDrawn) boardList[i].cell[j][k].marked = true;
	}
}

bool wholeRowMarked(Board board, int row) {
	for(int i = 0; i < BoardDimension; i++)
		if(!board.cell[row][i].marked) return false;
	
	return true;
}

bool wholeColumnMarked(Board board, int column) {
	for(int i = 0; i < BoardDimension; i++)
		if(!board.cell[i][column].marked) return false;
	
	return true;
}

bool updateWinner(Board* boardsList, int numberOfBoard, Board** winnerList, int* numberOfWinner) {
	bool newWinnerInserted = false;
	for(int i = 0; i < numberOfBoard; i++)
		if(isWinner(boardsList[i])) {
			winnerList[*numberOfWinner] = &(boardsList[i]);
			*numberOfWinner += 1;
			newWinnerInserted = true;
		}

	return newWinnerInserted;
}

bool isWinner(Board board) {
	for(int j = 0; j < BoardDimension; j++)
		if(wholeRowMarked(board, j) || wholeColumnMarked(board, j))
			return true;
	
	return false;
}

void removeWinner(Board **boardsList, int *numberOfBoard) {
	int index = 0;
	
	for(int i = 0;  i < *numberOfBoard; i++) {
		if(!isWinner((*boardsList)[i])) {
			(*boardsList)[index] = (*boardsList)[i];
			index++;
		}
	}

	*numberOfBoard = index;
	(*boardsList) = realloc((*boardsList), (*numberOfBoard) * sizeof(Board));
}

long getScore(Board winner, int lastNumberDrawned) {
	int unmarkedSum = 0;

	for(int i = 0; i < BoardDimension; i++) 
		for(int j = 0; j < BoardDimension; j++)
			if(!winner.cell[i][j].marked) unmarkedSum += winner.cell[i][j].number;
		

	return unmarkedSum * lastNumberDrawned;
}