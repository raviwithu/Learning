#!/usr/bin/env python3


import sys
from boofuzz import *
import datetime

suffix = '{0:%Y%m%d_%H%M%S}'.format(datetime.datetime.now())
filename = sys.argv[0].replace(".py","") + str(suffix)+".csv"

'''
if os.path.exists(filename):
    f = file("myfile.csv", "w+")
else:
    f = file("myfile.csv", "w+")
'''


csv_log = open(filename,"w+")



def post_test_callback(target, fuzz_data_logger, session, sock, *args, **kwargs):
    print("In post test callback fill me here")


def pre_test_callback(target, fuzz_data_logger, session, sock, *args, **kwargs):
    print("In pre test callback fill me here")



s_initialize("DoIP_Routing_Act_Req")
if s_block_start("DoIP_HEADER"):
    if s_block_start():
        s_string("\x02", fuzzable = False, name = "VER")
        s_byte(0xfd,  name = "INV_VER")
        s_word(0x8001, fuzzable=False, endian = ">",name = "TYPE")
        s_size("DoIP_PAYLOAD", length=4, endian = ">",fuzzable= True, output_format = "binary", name = "DoIP_PAYLOAD_SIZE")
        if s_block_start("DoIP_PAYLOAD"):
            s_word(0x0e00, fuzzable = True, endian = ">",name = "SOURCE_ADDR")
            s_word(0x0009, fuzzable = True, endian = ">",name = "TARGET_ADDR")
            s_word(0x2707, fuzzable = True, endian = ">",name = "UDS_Sec_Access")
        s_block_end()
    s_block_end()
s_block_end()


session = Session(target=Target(connection=TCPSocketConnection("192.168.10.128",8000)),post_test_case_callbacks=[post_test_callback],pre_send_callbacks=[pre_test_callback],sleep_time=2)
session.connect(s_get("DoIP_Routing_Act_Req"))
session.feature_check()
#session.fuzz()
