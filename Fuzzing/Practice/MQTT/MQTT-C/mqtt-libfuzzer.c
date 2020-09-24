#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<stdint.h>

#include "mqtt.h"

int LLVMFuzzerTestOneInput(const uint8_t *Data, size_t Size){
    struct mqtt_response response;
    mqtt_unpack_response(&response, Data, Size); 
    return 0;
}

    