import multiprocessing, subprocess,time
#Refer https://www.quantstart.com/articles/Parallelising-Python-with-Threading-and-Multiprocessing/

def tcpdump():
    p = subprocess.Popen(['sudo','tcpdump', '-i', 'eth0', '-s', '65535',
                  '-w', 'cap.pcap'], stdout=subprocess.PIPE)
    time.sleep(5)
    p.send_signal(subprocess.signal.SIGTERM)
    print("tcpdump completed")


def lss():    
    lsp =  subprocess.Popen(['ls',
                   '-la'], stdout=subprocess.PIPE)
    time.sleep(1)
    lsp.send_signal(subprocess.signal.SIGTERM)
    print("ls completed")


jobs=[]

process1 = multiprocessing.Process(target=tcpdump,)
process2 = multiprocessing.Process(target=lss,)

jobs.append(process1)
jobs.append(process2)


for j in jobs:
    j.start()


for j in jobs:
    j.join()
