#!/usr/bin/env python3


import sys,os
from boofuzz import *
import datetime

# importing functions from General folder
sys.path.append("../General/")
from Pre_Post_CallBack import post_test_callback,pre_test_callback

global target_ip
target_ip = "192.168.1.12"
target_port = 13400

suffix = '{0:%Y%m%d_%H%M%S}'.format(datetime.datetime.now())
filename = sys.argv[0].replace(".py","") + str(suffix)+".csv"

'''
if os.path.exists(filename):
    f = file("myfile.csv", "w+")
else:
    f = file("myfile.csv", "w+")
'''
dir_path = os.getcwd() + '/log'

if not os.path.exists(dir_path):
    os.makedirs(dir_path)

csv_log = open(dir_path + '/' + filename,"w+")



def post_test_callback(target, fuzz_data_logger, session, sock, *args, **kwargs):
    #print("In post test callback fill me here") 
    '''
    response = os.system("fping -c1 -t10" + target_ip)
    print("ping response - " + str(response))
    if response == 0:
        return True
    else:
        return False
    '''

def pre_test_callback(target, fuzz_data_logger, session, sock, *args, **kwargs):
    print("In pre test callback fill me here")



s_initialize("DoIP_Routing_Act_Req")
if s_block_start("DoIP_HEADER"):
    if s_block_start():
        s_string("\x02", fuzzable = False, name = "VER")
        s_byte(0xfd,  name = "INV_VER")
        s_word(0x0005, fuzzable=False, endian = ">",name = "TYPE")
        s_size("DoIP_PAYLOAD", length=4, endian = ">",fuzzable= True, output_format = "binary", name = "DoIP_PAYLOAD_SIZE")
        if s_block_start("DoIP_PAYLOAD"):
            s_word(0x0e00, fuzzable = True, endian = ">",name = "SOURCE_ADDR")
            s_byte(0x00, fuzzable = False, name = "ACT_TYPE")
            s_dword(0x00000000, fuzzable = False, name = "RSV_ISO")
            s_dword(0x00000000, fuzzable = False, name = "RSV_OEM")
        s_block_end()
    s_block_end()
s_block_end()


session = Session(target=Target(connection=TCPSocketConnection(target_ip,target_port)),post_test_case_callbacks=[post_test_callback],pre_send_callbacks=[pre_test_callback],sleep_time=2)
session.connect(s_get("DoIP_Routing_Act_Req"))
#session.feature_check()
session.fuzz()
