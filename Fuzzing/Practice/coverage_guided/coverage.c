#include<stdio.h>
#include<string.h>
#include<stdlib.h>


int main(int argc, char *argv[]){

    if(argc != 2){
        printf("Not enough argument");
        return 0;
    }

    char *password = argv[1];
    if(password[0] == 'a'){
        if(password[1] == 'b'){
            if(password[2] == 'c'){
                if(password[3] == 'd'){
                    if(password[4] == 'e'){
                        if(password[5] == 'f'){
                            if(password[6] == 'g'){
                                if(password[8] == 'h'){
                                        return 1;
                                }
                            }
                        }    
                    }
                }

            }

        }
    }
    return 0;
}
