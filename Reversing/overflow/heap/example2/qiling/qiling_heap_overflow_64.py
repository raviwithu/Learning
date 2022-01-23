from qiling import *
from qiling.const import QL_VERBOSE
import sys
malloc_allocated_addr = ""

def _mem_read(ql, addr, size, value,value1, value2): 
    #print("value in " + str(addr) + " - " + str(value))
    #print('>>>>Tracing instruction at 0x%x, instruction size = 0x%x ' %(addr, size))
    print('>>>>Tracing instruction at addr - 0x%x, size - %d, value - 0x%x, value1 - 0x%x, value2 - 0x%x' %(addr, size, value, value1, value2))
    print("reached mem read")

def inst_after_1st_malloc(ql):
    print("size allocated in heap memory", hex(ql.reg.rdx)[2:])
    print("malloc mem addr", hex(ql.reg.rax))
    size_allocated_in_heap = hex(ql.reg.rdx)[2:]
    malloc_allocated_addr = ql.reg.rax





def inst_after_strcpy(ql):
    print("malloc mem addr", hex(ql.reg.rax))
    print("RAX: %s" % ql.mem.read(ql.reg.rax, 11).decode('unicode_escape'))
    print("heap size: %s" % int.from_bytes(ql.mem.read(ql.reg.rax-8, 2),'little'))
    ql.mem.show_mapinfo()
    search_for_userinput = ql.mem.search(payload.encode())
    for each_addr in search_for_userinput:
        print("Found user input in 0x%x" %(each_addr))
        if each_addr == malloc_allocated_addr:           #comparison of addr not working need to look later 
            print( ql.mem.read(each_addr-0x8, 1).hex())

#payload = ("A" * 30) + struct.pack("L", 0x55555555516c).decode()
payload = "A" * 10
path = [sys.argv[1], payload]
rootfs1 = "/"
#ql = Qiling(argv = path, rootfs=rootfs1, verbose=QL_VERBOSE.OFF)
ql = Qiling(argv = path, rootfs=rootfs1)
#0x56556215 instruction after strcpy
ql.hook_address(callback=inst_after_strcpy, address=0x5555555551a0)
ql.hook_address(callback=inst_after_1st_malloc, address=0x55555555516e)

#ql.hook_mem_read(_mem_read, 0x5655a1a0-0x4)
# Enable debugger to listen at localhost address, default port 9999
#ql.debugger = True
#ql.debugger = "127.0.0.1:9999"  # GDB server listens to 127.0.0.1:9999
ql.run()
'''
try:
    ql.run()
except UcError as e:
    print("Error: %s" % e)
    #print("EIP: %s" % ql.unpack64(ql.mem.read(ql.reg.eip, 0x4)))
    #rint("ecx = 0x{:x}".format(ql.reg.eip))
    
    #alue_in_eip = bytearray.fromhex("{:x}".format(ql.reg.eip)).decode()
    #f sys.argv[1].find(value_in_eip,0,len(value_in_eip)) >= 0:
     #  print("Program overflow caused by user input")
'''

