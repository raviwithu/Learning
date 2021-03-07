#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#include "mqtt.h"

int main(int argc, char *argv[]){
    if(argc != 2){
        printf("1 arg required");
        return 0;
    }

    FILE *f = fopen(argv[1], "r");
    if(f == NULL){
        printf("Failed to open file!\n");
        return 0;
    }

    fseek(f, 0, SEEK_END);
    int file_length = ftell(f);
    printf("File len is: %d\n", file_length);
    u_int8_t *file_buffer = malloc(file_length +1);
    fseek(f, 0, SEEK_SET);

    int read_elements = fread(file_buffer, file_length, 1, f);
    printf("Read %d elements\n", read_elements);

    file_buffer[file_length] = '\x80';

    struct mqtt_response response;
    mqtt_unpack_response(&response, file_buffer, file_length);

}

