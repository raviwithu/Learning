#!/usr/bin/env python3


from boofuzz import *
csv_log = open("fuzz_results.csv","wb")
my_logger = [FuzzLoggerCsv(file_handle=csv_log)]

def post_test_callback(target, fuzz_data_logger, session, sock, *args, **kwargs):
    target.send(bytes.fromhex("e000"))

def pre_test_callback(target, fuzz_data_logger, session, sock, *args, **kwargs):
    target.send(bytes.fromhex("102300044d5154540402003c00176d6f73712d7956775054673776707a624f366f36567158"))

def pre_test_callback_For_DisCon(target, fuzz_data_logger, session, sock, *args, **kwargs):
    target.send(bytes.fromhex("102300044d5154540402003c00176d6f73712d7956775054673776707a624f366f36567158"))
    #t_end = time.time() + 30 # setting time for 30 seconds
    #while time.time() < t_end:






s_initialize("MQTT_CONNECT_COMMAND")
if s_block_start("MQTT_CONNECT_HEADER"):
    s_string("\x10", fuzzable=True,name="COMMAND") #connect command
    s_size("MQTT_CONNECT_HEADER_SIZE", length=1,endian="<",fuzzable=True, name="HEADER_SIZE") #size
    if s_block_start("MQTT_CONNECT_HEADER_SIZE"):
        s_size("MQTT_PROTO_NAME_SIZE",length=2,endian=">",fuzzable=True, name="PROTO_NAME_SIZE") #Protocol Name size

        if s_block_start("MQTT_PROTO_NAME_SIZE"):
            s_string("MQTT", fuzzable=True, name="PROTO_NAME") #Proto Name
        s_block_end()

        s_string("\x04",fuzzable=True, name="PROTO_VER") #Protocol version
        s_string("\x02",fuzzable=True,name="CONN_FLAG")  #Clean session connect flag
        s_string("\x00\x3c",fuzzable=True,name="KEEP_ALIVE")
        s_size("MQTT_CLIENT_ID_SIZE",length=2,endian='>',fuzzable=True,name="CLIENT_ID_SIZE")
        if s_block_start("MQTT_CLIENT_ID_SIZE"):
           s_string("mosq-1OXLax7Tm9edbdtEQh",fuzzable=True,name="CLIENT_ID")
        s_block_end()
    s_block_end()
s_block_end()



s_initialize("MQTT_PUB_MESSAGE")
if s_block_start("MQTT_PUB_MSG"):
    s_string("\x30",fuzzable=True,name="MQTT_PUB_HDR_TYPE") #PUB
    s_size("MQTT_PUB_MSG_LEN", length=1,endian='>',fuzzable=True,name="PUB_MSG_LEN")
    if s_block_start("MQTT_PUB_MSG_LEN"):
        s_size("MQTT_PUB_TOPIC_LEN", length=2,endian='>',fuzzable=True,name="TOPIC_LEN")
        if s_block_start("MQTT_PUB_TOPIC_LEN"):
            s_string("ULUL",fuzzable=True,name="TOPIC_NAME")
        s_block_end()
        s_string("MESSAGE_MESSAGE",fuzzable=True,name="MSG")
    s_block_end()
s_block_end()


s_initialize("MQTT_DISCON_REQUEST")
if s_block_start("MQTT_DISCON_REQ"):
    s_string("\xe0",fuzzable=False,name="DISCON_HDR")
    s_string("\x00",fuzzable=False,name="DISCON_MSG_LEN")
s_block_end()

#session = Session(target=Target(connection=TCPSocketConnection("5.196.95.208",1883)),post_test_case_callbacks=[post_test_callback],pre_send_callbacks=[pre_test_callback])#,fuzz_loggers=my_logger)
#session = Session(target=Target(connection=TCPSocketConnection("192.168.129.200",1883)),post_test_case_callbacks=[post_test_callback],pre_send_callbacks=[pre_test_callback],sleep_time=2)
#,fuzz_loggers=my_logger)
#efine_proto_static(session=session)
#session.feature_check()
#     if session.last_recv == b' \x02\x00\x00':
#        print("Connect Ack recev")
#        PUBLISH_MSG(session=session)
#        session.feature_check()
#        DISCONNECT_REQ(session)
#        session.feature_check()
#session.fuzz()

#session.feature_check()
#session.connect(s_get("MQTT_CONNECT_COMMAND"),s_get("MQTT_PUB_MESSAGE"),s_get("MQTT_DISCON_REQUEST"))
#session.connect(session.root,s_get("MQTT_CONNECT_COMMAND"))

session = Session(target=Target(connection=TCPSocketConnection("192.168.129.200",1883)),sleep_time=2,post_test_case_callbacks=[post_test_callback])
session.connect(s_get("MQTT_CONNECT_COMMAND"))
session.fuzz()
#session.feature_check()



session1 = Session(target=Target(connection=TCPSocketConnection("192.168.129.200",1883)),post_test_case_callbacks=[post_test_callback],pre_send_callbacks=[pre_test_callback],sleep_time=2)
session1.connect(s_get("MQTT_PUB_MESSAGE"))
#session.connect(s_get("MQTT_DISCON_REQUEST"))
#session.feature_check()
session1.fuzz()

'''
Need to add for disconnect
session2 = Session(target=Target(connection=TCPSocketConnection("192.168.129.200",1883)),post_test_case_callbacks=[post_test_callback],pre_send_callbacks=[pre_test_callback],sleep_time=2)
session2.connect(s_get("MQTT_PUB_MESSAGE"))
#session.connect(s_get("MQTT_DISCON_REQUEST"))
#session.feature_check()
session2.fuzz()'''
