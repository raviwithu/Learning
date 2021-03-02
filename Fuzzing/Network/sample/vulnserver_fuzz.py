#/usr/bin/env python3

from boofuzz import *

def post_test_callback(target, fuzz_data_logger, session, sock, *args, **kwargs):
    #target.send(bytes.fromhex("e000"))
    print(target.recv())
    if target.recv() == b'':
        fuzz_data_logger.log_fail("No data received from server")


def pre_test_callback(target, fuzz_data_logger, session, *args, **kwargs):
    target.send(bytes.fromhex('\n'))




s_initialize("VULN_SERVER_COMMAND_HELP")
if s_block_start("HELP"):
    s_string("HELP",fuzzable=False,name="HELP")
    s_delim(" ",fuzzable=False,name="DELIMIT_1")
    s_string("ULUL",size=3000,fuzzable=True,name="HELP_VALUE")
s_block_end()


s_initialize("VULN_SERVER_COMMAND_STAT")
if s_block_start("STAT"):
    s_string("STATS",fuzzable=False,name="STAT")
    s_delim(" ",fuzzable=False,name="DELIMIT_2")
    s_string("ULUL",fuzzable=True,max_len=7000000,name="STAT_VALUE")
s_block_end()



s_initialize("VULN_SERVER_COMMAND_RTIME")
if s_block_start("RTIME"):
    s_string("RTIME",fuzzable=False,name="RTIME")
    s_delim(" ",fuzzable=False,name="DELIMIT_3")
    s_string("ULUL",fuzzable=True,max_len=7000,name="RTIME_VALUE")
s_block_end()

s_initialize("VULN_SERVER_COMMAND_LTIME")
if s_block_start("LTIME"):
    s_string("LTIME",fuzzable=False,name="LTIME")
    s_delim(" ",fuzzable=False,name="DELIMIT_4")
    s_string("ULUL",fuzzable=True,max_len=7000,name="LTIME_VALUE")
s_block_end()

s_initialize("VULN_SERVER_COMMAND_SRUN")
if s_block_start("SRUN"):
    s_string("SRUN",fuzzable=False,name="SRUN")
    s_delim(" ",fuzzable=False,name="DELIMIT_5")
    s_string("ULUL",fuzzable=True,max_len=7000,name="SRUN_VALUE")
s_block_end()

s_initialize("VULN_SERVER_COMMAND_TRUN")
if s_block_start("TRUN"):
    s_string("TRUN",fuzzable=False,name="TRUN")
    s_delim(" ",fuzzable=False,name="DELIMIT_6")
    s_string(".",fuzzable=False,name="TRUN1")
    s_string("ULUL",fuzzable=True,size=3000,max_len=7000,name="TRUN_VALUE")
s_block_end()

s_initialize("VULN_SERVER_COMMAND_GMON")
if s_block_start("GMON"):
    s_string("GGMON",fuzzable=False,name="GMON")
    s_delim(" ",fuzzable=False,name="DELIMIT_7")
    s_string("ULUL",fuzzable=True,max_len=7000,name="GMON_VALUE")
s_block_end()

s_initialize("VULN_SERVER_COMMAND_GDOG")
if s_block_start("GDOG"):
    s_string("GDOG",fuzzable=False,name="GDOG")
    s_delim(" ",fuzzable=False,name="DELIMIT_8")
    s_string("ULUL",fuzzable=True,max_len=7000,name="GDOG_VALUE")
s_block_end()

s_initialize("VULN_SERVER_COMMAND_KSTET")
if s_block_start("KSTET"):
    s_string("KSTET",fuzzable=False,name="KSTET")
    s_delim(" ",fuzzable=False,name="DELIMIT_9")
    s_string("ULUL",fuzzable=True,max_len=7000,name="KSTET_VALUE")
s_block_end()

s_initialize("VULN_SERVER_COMMAND_GTER")
if s_block_start("GTER"):
    s_string("GTER",fuzzable=False,name="GTER")
    s_delim(" ",fuzzable=False,name="DELIMIT_10")
    s_string("ULUL",fuzzable=True,max_len=7000,name="GTER_VALUE")
s_block_end()

s_initialize("VULN_SERVER_COMMAND_HTER")
if s_block_start("HTER"):
    s_string("HTER",fuzzable=False,name="HTER")
    s_delim(" ",fuzzable=False,name="DELIMIT_11")
    s_string("ULUL",fuzzable=True,max_len=7000,name="HTER_VALUE")
s_block_end()

s_initialize("VULN_SERVER_COMMAND_LTER")
if s_block_start("LTER"):
    s_string("LTER",fuzzable=False,name="LTER")
    s_delim(" ",fuzzable=False,name="DELIMIT_12")
    s_string("ULUL",fuzzable=True,max_len=7000,name="LTER_VALUE")
s_block_end()

s_initialize("VULN_SERVER_COMMAND_KSTAN")
if s_block_start("KSTAN"):
    s_string("KSTAN",fuzzable=False,name="KSTAN")
    s_delim(" ",fuzzable=False,name="DELIMIT_13")
    s_string("ULUL",fuzzable=True,max_len=7000,name="KSTAN_VALUE")
s_block_end()

s_initialize("VULN_SERVER_COMMAND_RANDOM")
if s_block_start("RANDOM"):
    s_string("EXIT",fuzzable=False,max_len=7000,name="RANDOM")
s_block_end()


session = Session(target=Target(connection=TCPSocketConnection("192.168.129.187",9999)),sleep_time=2,post_test_case_callbacks=[post_test_callback], pre_send_callbacks=[pre_test_callback])
#session.connect(s_get("VULN_SERVER_COMMAND_HELP"))
#session.connect(s_get("VULN_SERVER_COMMAND_STAT"))
session.connect(s_get("VULN_SERVER_COMMAND_TRUN"))
session.fuzz_single_case(1)
#session.fuzz_single_node_by_path("VULN_SERVER_COMMAND_TRUN:VULN_SERVER_COMMAND_TRUN.TRUN.TRUN_VALUE:20")
#session.fuzz()
#print(session.num_mutations())
