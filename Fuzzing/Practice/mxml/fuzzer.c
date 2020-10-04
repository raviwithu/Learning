#include<stdint.h>
#include "mxml.h"

int main(int argc, char *argv[]){
    if(argc != 2  ){
        return 0;
    }

    FILE *fp =  fopen(argv[1], 'r');
    mxml_node_t *top = mxmlLoadString(NULL, fp, MXML_OPAQUE_CALLBACK);
    mxmlDelete(top);
    return 0;
    
}
