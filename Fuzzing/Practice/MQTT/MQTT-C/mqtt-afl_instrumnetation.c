#include <stdio.h>
#include <stdint.h>
#include <mqtt.h>
 int main(int argc, char *argv[]){

#ifdef __AFL_HAVE_MANUAL_CONTROL
		__AFL_INIT();
#endif

	printf("Entering into program\n");
	if(argc != 2){
		printf("Need file argument\n");
		return 0;
	}
    while (__AFL_LOOP(1000)) {
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

		//int read_elements = fread(file_buffer, file_length, 1, f);

		struct mqtt_response response;
		mqtt_unpack_response(&response, file_buffer, file_length);
		return 0;
 	}
 }
