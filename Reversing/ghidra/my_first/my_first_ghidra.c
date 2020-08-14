#include <string.h>
#include <stdlib.h>
#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>

void print_systeminfo(){
	pid_t our_pid = getpid();
	printf("PID : %d\n", our_pid);
}



int main(int argc, char *argv[]){
	
	print_systeminfo();


	if (argc == 2){
		FILE *f = fopen(argv[1], "r");
		fseek(f, 0, SEEK_END);
		size_t filesize = ftell(f);
		printf("Supplied file size is: %lu\n", filesize);
	}

	return 0;
}

