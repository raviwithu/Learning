from qiling import *
from qiling.const import QL_VERBOSE
import sys, subprocess, chardet
from unicorn import *
from capstone import *
shellcode= 0xeb1e5e4831c0b0014889c74889fa4883c2220f054831c04883c03c4831ff0f05e8ddffffff48656c6c6f20576f726c6420746f2074686520534c41452d363420436f757273650a


#shell code is not working
shellcode_hex = "\xeb\x1e\x5e\x48\x31\xc0\xb0\x01\x48\x89\xc7\x48\x89\xfa\x48\x83\xc2\x22\x0f\x05\x48\x31\xc0\x48\x83\xc0\x3c\x48\x31\xff\x0f\x05\xe8\xdd\xff\xff\xff\x48\x65\x6c\x6c\x6f\x20\x57\x6f\x72\x6c\x64\x20\x74\x6f\x20\x74\x68\x65\x20\x53\x4c\x41\x45\x2d\x36\x34\x20\x43\x6f\x75\x72\x73\x65\x0a"

def generate_bof_pattern_string(length):
    process = subprocess.Popen(['/usr/share/metasploit-framework/tools/exploit/pattern_create.rb','-l', length],
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    #stdout, stderr = process.communicate()
    process.wait()
    ret_val = process.stdout.readline().rstrip().decode('utf-8')
    return ret_val

def func_func(ql):
    print("func function called")

def func_func_ret(ql):
    ql.mem.show_mapinfo()
    size = 16
    print("func function called")
    print("EIP durning return to main from funcFunc", hex(ql.reg.rip))
    print("ESP durning return to main from funcFunc", hex(ql.reg.rsp))
    #print("EIP: %s" % ql.unpack64(ql.mem.read(ql.reg.eip, 0x4)))
    print("rsp = 0x{:x}".format(ql.reg.rsp))
    #value_in_rsp = bytearray.fromhex("{:x}".format(ql.reg.rsp)).decode('')
    value_in_rsp = ql.mem.read(ql.reg.rsp, 4).decode('unicode_escape')
    #value_in_rsp = bytearray.fromhex("{:x}".format(ql.reg.rsp))
    print(value_in_rsp)
    #ql.stack_push(0x909090909090)
    ql.stack_push(0x55555555516c) #need more research to inject shellcode, rightnow only chekced for redirection
    #ql.stack_push(shellcode)
    #address = ql.reg.rsp
    # read current instruction bytes
    #data = ql.mem.read(address, size)
    # initialize Capstone
    #md = Cs(CS_ARCH_X86, CS_MODE_64)
    # disassemble current instruction
    #for i in md.disasm(data, address):
    #    print("[*] 0x{:08x}: {} {}".format(i.address, i.mnemonic, i.op_str))



def main_func(ql):
    print("main function called")

def hook_code(ql,address,size,user_data):
    print('>>>>Tracing instruction at 0x%x, instruction size = 0x%x ' %(address, size))

def my_memory_manager(ql, *args):
    saved_args = locals()
    print("saved args:", saved_args)
    if ql.mem.is_available(addr, size):
        ql.mem.map(addr, size,info = [my_first_map])
###########################################################################
'''
#prac code
length = "100"
print(generate_bof_pattern_string(length))
print("argu - " + sys.argv[2])
arg1_val = sys.argv[2]
path = [sys.argv[1], arg1_val]
rootfs1 = "/"
ql = Qiling(argv = path, rootfs=rootfs1, verbose=QL_VERBOSE.OFF)


#ql.multithread = True
#ql.mem.show_mapinfo()
#ql.hook_add(UC_HOOK_CODE, hook_code)
#ql.hook_mem_unmapped(my_memory_manager)
#ql.hook_address(callback=main_func, address=0x5555555561bd)
ql.hook_address(callback=func_func, address=0x555555555135)
ql.hook_address(callback=func_func_ret, address=0x000055555555516c)
'''
#########################################################################3




#identify_overflow_len = ["100","200","300","500","1000"]
identify_overflow_len = ["100"]

for each_len in identify_overflow_len:

    #payload = generate_bof_pattern_string(each_len)
    #payload = "A" * 30 + "BCDEF"
    payload = "A" * 30 + shellcode_hex
    print("payload - " + payload)
    path = [sys.argv[1], payload]
    rootfs1 = "/"
    ql = Qiling(argv = path, rootfs=rootfs1, verbose=QL_VERBOSE.OFF)
    ql.hook_address(callback=func_func_ret, address=0x000055555555516c)

    # Enable debugger to listen at localhost address, default port 9999
    ql.debugger = True
    ql.debugger = "127.0.0.1:9999"  # GDB server listens to 127.0.0.1:9999

    try: 
        ql.run()
    except UcError as e:
        #ql.mem.show_mapinfo()
        #value_in_rsp = bytearray.fromhex("{:x}".format(ql.reg.rsp))
        #if chardet.detect(value_in_rsp)['encoding'] == "ascii":
        value_in_rip = bytearray.fromhex("{:x}".format(ql.reg.rip)).decode('unicode_escape')
        #inversed because of little endian, may be there is better way to do it
        index = payload.find(value_in_rip[::-1],0,len(payload))
        if index >= 0:
            print("Program overflow caused by user input")
            print("identified offset - ",index)
            break;
