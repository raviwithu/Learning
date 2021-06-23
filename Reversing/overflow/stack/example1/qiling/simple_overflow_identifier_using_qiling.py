from qiling import *
import sys
from unicorn import *

def func_func(ql):
    print("func function called")


def main_func(ql):
    print("main function called")

def hook_code(ql,address,size,user_data):
    print('>>>>Tracing instruction at 0x%x, instruction size = 0x%x ' %(address, size))

def my_memory_manager(ql, *args):
    saved_args = locals()
    print("saved args:", saved_args)
    if ql.mem.is_available(addr, size):
        ql.mem.map(addr, size,info = [my_first_map])

print("argu - " + sys.argv[1])
path = ["stackoverflow64", sys.argv[1]]
rootfs1 = "/"
ql = Qiling(argv = path, rootfs=rootfs1)

#ql.multithread = True
#ql.mem.show_mapinfo()
#ql.hook_add(UC_HOOK_CODE, hook_code)
#ql.hook_mem_unmapped(my_memory_manager)
#ql.hook_address(callback=main_func, address=0x5555555561bd)
ql.hook_address(callback=func_func, address=0x555555555135)

try: 
    ql.run()
except UcError as e:
    print("Error: %s" % e)
    #print("EIP: %s" % ql.unpack64(ql.mem.read(ql.reg.eip, 0x4)))
    print("ecx = 0x{:x}".format(ql.reg.eip))
    value_in_eip = bytearray.fromhex("{:x}".format(ql.reg.eip)).decode()
    if sys.argv[1].find(value_in_eip,0,len(value_in_eip)) >= 0:
        print("Program overflow caused by user input")
