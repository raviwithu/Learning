#!/usr/bin/env python3

import serial,time
import sys
import binascii
from tqdm import tqdm
ser = serial.Serial(sys.argv[1], 115200)
output_file = open(sys.argv[2], "w")

ser.write(b'printenv\r\n')
while True:
    s    = ser.readline()
    line = s.decode('utf-8').replace('\r\n','')
    time.sleep(.1)
    output_file.write(line+"\r\n") #Appends output to fil


output_file.close()
ser.close()
