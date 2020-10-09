#include<stdio.h>

int main(){
	//initalized variables
	volatile int a = 3;
	volatile float b = 4.5;
	volatile double c = 5.25;
	//uninitialized variable
	volatile float sum;

	sum = a + b + c;
	printf("This sum of a,b and c id %f.", sum);
}
