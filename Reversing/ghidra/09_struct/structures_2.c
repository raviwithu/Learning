#include<stdio.h>

int main(){
	typedef struct {
		char * brand;
		int model;
	} vehicle;

	vehicle mycar;
	mycar.brand = "Ford";
	mycar.model = 2007;

	printf("My car - %s", mycar.brand);
}
