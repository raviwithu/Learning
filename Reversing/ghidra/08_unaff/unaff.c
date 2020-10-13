#include<stdlib.h>


long c;
register long *b asm("r15");


void initRegisterPointerVar(){
	b =&c;
}

void setRegisterPointerVar(long x){
	*b = x;
}

long getRegisterPointerVar(){
	return *b;

}

int main(int argc, char *argv){
	setRegisterPointerVar("345678");

}
