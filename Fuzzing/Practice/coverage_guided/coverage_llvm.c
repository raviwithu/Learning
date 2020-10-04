#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<stdint.h>


int LLVMFuzzerTestOneInput(const uint8_t *Data, size_t Size){

    if(Size < 10){
        //printf("Not enough argument");
        return 0;
    }

    char *password = Data;
    if(password[0] == 'a'){
        if(password[1] == 'b'){
            if(password[2] == 'c'){
                if(password[3] == 'd'){
                    if(password[4] == 'e'){
                        if(password[5] == 'f'){
                            if(password[6] == 'g'){
                                if(password[8] == 'h'){
                                        abort();
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
