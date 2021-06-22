#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

int functionFunction(char * param)
{
	char* localString = "conjunction function";
	int localint = 0xdeadbeef;
	char localString2[10];

	strcpy(localString2, param);
	return 1;
}
int LLVMFuzzerTestOneInput(const uint8_t *Data, size_t Size) {
//int main(int argc, char* argv[]){
	if(Size > 5) { 
		char* localString = "main function";
		int localInt = 0x11223344;
		//functionFunction(argv[1]);
		functionFunction(Data);
		return 0;
	}
}
