#include <stdio.h>
#include <stdint.h>
#include <mqtt.h>
 int main(int argc, char* argv[]) {
     if(argc > 1 ){
         return 0;
     }


    struct mqtt_response response;
    mqtt_unpack_response(&response, argv[1], strlen(argv[1]));
    return 0;
 }
