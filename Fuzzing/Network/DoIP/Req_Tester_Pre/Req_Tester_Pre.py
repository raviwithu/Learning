#!/usr/bin/env python3


import sys,os,platform,subprocess
from boofuzz import *
import datetime

# importing functions from General folder
sys.path.append("../General/")
from Pre_Post_CallBack import *

global target_ip
target_ip = sys.argv[1]
target_port = 13400

net_monitor_ip = "127.0.0.1"
net_monitor_port = 2700

suffix = '{0:%Y%m%d_%H%M%S}'.format(datetime.datetime.now())
filename = 'logs_'+ sys.argv[0].replace(".py","") + str(suffix)+".csv"


'''
if os.path.exists(filename):
    f = file("myfile.csv", "w+")
else:
    f = file("myfile.csv", "w+")
'''

#for logs
csv_log = open(filename,"w+")
#my_logger = [FuzzLoggerCsv(file_handle=csv_log)]
#loggers = [FuzzLoggerText(), FuzzLoggerCsv(file_handle=csv_file.open('w'))]
loggers = [FuzzLoggerText(), FuzzLoggerCsv(file_handle=csv_log)]


s_initialize("DoIP_Req_Tester_Present")
if s_block_start("DoIP_HEADER"):
    if s_block_start():
        s_string("\x02", fuzzable = False, name = "VER")
        s_byte(0xfd,  fuzzable = True, name = "INV_VER")
        s_word(0x8001, fuzzable=True, endian = ">",name = "TYPE")#8001 is for diagnostic message
        s_size("DoIP_PAYLOAD", length=4, endian = ">",fuzzable= True, output_format = "binary", name = "DoIP_PAYLOAD_SIZE")
        if s_block_start("DoIP_PAYLOAD"):
            s_word(0x0e00, fuzzable = True, endian = ">",name = "SOURCE_ADDR")
            s_word(0x0e40, fuzzable = True, endian = ">",name = "TARGET_ADDR")
            s_byte(0x00, fuzzable = True, name = "ACT_TYPE")
            s_byte(0x3e, fuzzable = True, name = "UDS_Tester_Present")
            s_byte(0x80, fuzzable = True, name = "UDS_Reply")
            #s_string("Random", size = 1000, name="Random_Data") # this may be not necessary, just adding extra padding to see extra length are handled
        s_block_end()
    s_block_end()
s_block_end()
#s_repeat("DoIP_Req_Tester_Present", 0, 1000, 40, name="DoIP_Req_Tester_Present_Repeat")

#session = Session(target=Target(connection=TCPSocketConnection(target_ip,target_port)),post_test_case_callbacks=[post_test_callback],pre_send_callbacks=[pre_test_callback],fuzz_loggers=loggers,sleep_time=2)
session = Session(target=Target(connection=TCPSocketConnection(target_ip,target_port),monitors=[spaceTargetMonitor]),fuzz_loggers=loggers,sleep_time=2)
mutation_count = s_get("DoIP_Req_Tester_Present").num_mutations()
print(mutation_count)
session.connect(s_get("DoIP_Req_Tester_Present"))
#session.feature_check()
session.fuzz_single_case(1)
#session.fuzz(max_depth=3)
