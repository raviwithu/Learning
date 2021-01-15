import threading, queue
from scapy.all import *
q = queue.Queue()
global count
count = 0



#incomplete one not working not able to pralleise it
def scapy_sniffer():
    #print(count)
    t = AsyncSniffer(prn=lambda x: x.summary(), store=False, filter="udp", count = 5)
    #pkt = sniff(prn=lambda x: x.summary(), store=False, filter="udp", count=10)

    t.start()
    t.stop()
    wrpcap('file.pcap', t,append=True)
    #count = count + 1

def request_queue():
    while True:
        project = q.get()
        print(f'working on {project}')
        scapy_sniffer() 
        print(f'done{project}')
        q.task_done()
threading.Thread(target=request_queue, daemon=True).start()
for project in range(5):
    q.put(project)
print('project requests sent\n', end='')
q.join()
print('projects completed')
