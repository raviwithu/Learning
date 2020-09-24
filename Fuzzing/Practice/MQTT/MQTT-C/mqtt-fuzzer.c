#include<stdlib.h>
#include<stdio.h>
#include<string.h>

#include "mqtt.h"

int main(int argc, char* argv[]){

    if(argc != 2){
        printf("Need atleast one argument");
    }

    FILE *f = fopen(argv[1], "r");
    if(f == NULL){
        printf("Faile to open file \n");
        return 0;
    }

    fseek(f, 0, SEEK_END);
    int file_length = ftell(f);
    printf("File length is :%d\n", file_length);
    char *file_buffer = malloc(file_length);
    fseek(f, 0 , SEEK_SET);
    fread(file_buffer, file_length, 1, f);
    struct mqtt_response response;
    mqtt_unpack_response(&response, file_buffer, file_length);
}