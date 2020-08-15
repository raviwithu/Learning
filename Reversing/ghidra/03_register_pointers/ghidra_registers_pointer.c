#include <stdlib.h>


long c;
register long *b asm("r15");


void initRegisterpointerVar(){
	b = &c;
}

void setRegisterPointerVar(long x){
	*b = x;
}

long getRegisterPointerVar(){
	return *b;
}

int main(int agc, char *argv[]){

	printf("Pointer register ");
}
