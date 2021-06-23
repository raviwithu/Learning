from qiling import *
from os import environ

EXEC_FILE = ["./stackoverflow64"]
#ROOTFS = "{}/x86_linux".format(environ["QILING_ROOTFS"])
ROOTFS = "/"
FLAG = []

def on_hook(ql : core.Qiling) -> None:
    addr_flag = ql.reg.eax
    FLAG.append(ql.mem.read(addr_flag, 0x13))

def my_sandbox(path, rootfs):
    ql = Qiling(path, rootfs)
    
    # remove systrace logs
    #ql.filter = []

    #ql.hook_address(on_hook, 0x804853d)
    ql.run()

    flag = FLAG[0][:0x12].decode() + FLAG[1][:7].decode()
    print(flag)

if __name__ == "__main__":
    my_sandbox(EXEC_FILE, ROOTFS)
