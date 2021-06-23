from qiling import *

# initialize emulator (x86-64 linux)
ql = Qiling(["./stackoverflo64_ns_static"], 
            rootfs="/")
#ql = Qiling(["/mnt/hgfs/F/Work/Data/Emulation/qiling/examples/rootfs/x8664_linux/bin/x8664_hello"], 
#            rootfs="/mnt/hgfs/F/Work/Data/Emulation/qiling/examples/rootfs/x8664_linux")
ql.run()

