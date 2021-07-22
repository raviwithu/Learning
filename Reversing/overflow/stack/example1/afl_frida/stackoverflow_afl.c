#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int functionFunction(char *param)
{
	char* localString = "conjunction function";
	int localint = 0xdeadbeef;
	char localString2[10];

	strcpy(localString2, param);
	return 1;
}

int main(int argc, char *argv[]){
	printf("Entering into program\n");
	if(argc != 2){
		printf("Need file argument\n");
		return 0;
	}
	
	FILE *f = fopen(argv[1], "r");
	if(f == NULL){
		printf("Faile to open file\n");
		return 0;
	}

	fseek(f, 0 , SEEK_END);
	int file_length = ftell(f);
	printf("File length is: %d\n", file_length);
	char *file_buffer = malloc(file_length);
	fseek(f, 0, SEEK_SET);

	int read_elements = fread(file_buffer, file_length, 1, f);
	printf("Read %d elements\n", read_elements);

	char* localString = "main function";
	int localInt = 0x11223344;
	functionFunction(file_buffer);
	return 0;
}
