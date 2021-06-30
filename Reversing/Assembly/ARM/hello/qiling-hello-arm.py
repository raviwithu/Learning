from qiling import *
from qiling.const import QL_VERBOSE
import sys

def hook_syscall(ql):
    print("load addr", ql.profile.get("OS64", "load_address"))
    print("r2 = %s"% ql.mem.read(ql.reg.r1,0x7))


path = [sys.argv[1]]
rootfs1 = "/home/kali/Desktop/misc/Emulator/qiling/examples/rootfs/"
ql = Qiling(argv = path, rootfs=rootfs1, verbose=QL_VERBOSE.OFF)
ql.hook_address(callback=hook_syscall, address=0x1007c)


ql.run()
