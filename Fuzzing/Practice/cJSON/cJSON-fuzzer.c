#include <stdio.h>

#include "cJSON.h"

int main(int argc, char *argv[]){

	if(argc !=2){
		printf("Arg req\n");
		return 0;
	}

	FILE *f = fopen(argv[1], "r");
	if(f==NULL){
		printf("Failed to open\n");
		return 0;
	
	}

	fseek(f, 0, SEEK_END);
	int file_length = ftell(f);
	printf("File length is: %d\n", file_length);
	char *file_buffer = malloc(file_length+1);
	fseek(f, 0, SEEK_SET);

	int read_elements = fread(file_buffer, file_length, 1, f);
	printf("Read %d elements\n", read_elements);
	file_buffer[file_length] = '\x00';

	cJSON *test = cJSON_Parse(file_buffer);
	if(test != NULL){
		printf("Success in loading!\n");
	}else{
		printf("Failed to load!\n");
	}
}
