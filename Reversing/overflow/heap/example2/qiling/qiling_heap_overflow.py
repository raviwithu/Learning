from qiling import *
from qiling.const import QL_VERBOSE
import sys


def _mem_read(ql, addr, size, value,value1, value2): 
    #print("value in " + str(addr) + " - " + str(value))
    #print('>>>>Tracing instruction at 0x%x, instruction size = 0x%x ' %(addr, size))
    print('>>>>Tracing instruction at addr - 0x%x, size - %d, value - 0x%x, value1 - 0x%x, value2 - 0x%x' %(addr, size, value, value1, value2))
    print("reached mem read")

def inst_after_strcpy(ql):
    print("malloc mem addr", hex(ql.reg.eax))
    #print("EAX: %s" % ql.mem.read(ql.reg.eax-0x4, 8).decode('unicode_escape'))
    print("EAX: %s" % int.from_bytes(ql.mem.read(ql.reg.eax-0x4, 2),'little'))
    print(ql.mem.show_mapinfo())

#payload = ("A" * 30) + struct.pack("L", 0x55555555516c).decode()
payload = "A" * 10
path = [sys.argv[1], payload]
rootfs1 = "/"
ql = Qiling(argv = path, rootfs=rootfs1, verbose=QL_VERBOSE.OFF)
#0x56556215 instruction after strcpy
ql.hook_address(callback=inst_after_strcpy, address=0x56556215)
#ql.hook_mem_read(_mem_read, 0x5655a1a0-0x4)
# Enable debugger to listen at localhost address, default port 9999
#ql.debugger = True
#ql.debugger = "127.0.0.1:9999"  # GDB server listens to 127.0.0.1:9999

ql.run()

