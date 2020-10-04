#include<stdint.h>
#include "mxml.h"

int LLVMFuzzerTestOneInput(const uint8_t *Data, size_t Size){
    if(Size == 0  ){
        return 0;
    }

    if(Size % 4 !=0 ){
        return 0;
    }

    if(Data[Size-1] != '\x00'){
        return 0;
    }
    mxml_node_t *top = mxmlLoadString(NULL, Data, MXML_OPAQUE_CALLBACK);
    return 0;
    
}