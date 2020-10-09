#Emulate Binary

from qiling import *


def prints(ql):
    addr_arg0=ql.os.function_arg[0] 
    addr_arg1=ql.os.function_arg[1]
    addr_arg2=ql.os.function_arg[2]
    addr_arg3=ql.os.function_arg[3]
    addr_arg4=ql.os.function_arg[4]
    addr_arg5=ql.os.function_arg[5]
    #print("printf fun %s"%ql.mem.string(addr_arg0))
    print("Printf address 0x{:08x}:".format(addr_arg0))
    print("Printf address 0x{:08x}:".format(addr_arg1))
    print("Arg1 - " + str(ql.unpack64(ql.mem.read(addr_arg1, 8))))
    print("Printf address 0x{:08x}:".format(addr_arg2))
    print("Printf address 0x{:08x}:".format(addr_arg3))
    print("Printf address 0x{:08x}:".format(addr_arg4))
    print("Printf address 0x{:08x}:".format(addr_arg5))
    #print("No of arg" + len(ql.os.function_arg))
    #print("eip info 0x{:08x}:".format(ql.reg.eip))
    print("Reg cr0 - "+ str(ql.reg.cr0))
    print("Reg fp0 - "+ str(ql.reg.cr0))
    print("Reg xmm0 - "+ str(ql.reg.cr0))
    #print("heap - "+ str(ql.loader.heap))
    print("mmap - 0x{:08x}".format(ql.loader.mmap_address))
    #print("Reg cr0 - "+ str(ql.reg.cr0))


ql = Qiling(filename=["/mnt/hgfs/F/Work/mygithub/Learning/Reversing/ghidra/Program/05_Local_Variable_Types/x64/05_Local_variable_Types_o1_x64"],
            rootfs="/mnt/hgfs/F/Work/Data/Emulation/qiling/examples/rootfs/x8664_linux/",
            console=False,
            #output="disasm",
            log_dir=".")
ql.set_api("printf", prints)
print("Entry point - 0x{:08x}".format(ql.loader.entry_point))
ql.run()
