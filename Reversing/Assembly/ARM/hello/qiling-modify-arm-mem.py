from qiling import *
from qiling.const import QL_VERBOSE
import sys

modified_string = b'Hellow all all' + b'\n'

def hook_syscall(ql):
    #print("load addr", ql.profile.get("OS64", "load_address"))
    print("r1 = %s"% ql.mem.read(ql.reg.r1,0x7))
    print("r2 = %d" %ql.reg.read("r2"))
    ql.mem.write(ql.reg.r1,modified_string)
    print(type(len(modified_string)))
    ql.reg.write("r2", len(modified_string)) #Need to look into this, reg.write)
    print("r1 = %s"% ql.mem.read(ql.reg.r1,ql.reg.r2))
    print("r2 = %d" %ql.reg.read("r2"))


path = [sys.argv[1]]
rootfs1 = "/home/kali/Desktop/misc/Emulator/qiling/examples/rootfs/"
ql = Qiling(argv = path, rootfs=rootfs1, verbose=QL_VERBOSE.OFF)
ql.hook_address(callback=hook_syscall, address=0x1007c)


ql.run()
