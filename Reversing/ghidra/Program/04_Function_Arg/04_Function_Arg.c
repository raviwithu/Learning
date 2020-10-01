#include<stdio.h>
#include<string.h>
int funcFunc(char* arg1){
	char* localString = "local string";
	int localInt = 1;
	char localString2[10];

	strcpy(localString2, arg1);
	return 0;

}

int main(int argc, char* argv[]){
	if (argc != 2){
		return 0;
	}
	funcFunc(argv[1]);
	return 0;

}
