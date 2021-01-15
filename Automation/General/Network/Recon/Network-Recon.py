import subprocess, sys, os, time, datetime, signal, queue
from multiprocessing import Process, Event, Queue
from termcolor import colored
iface = 'eth0'

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


#print(f"{bcolors.WARNING}Run with Sudo command")
if os.geteuid() != 0:
    print(colored('Run with Sudo command', 'red'))
    exit()

#######################################################
'''
#TO DO LIST
    1. Identify TCP and UDP port script with slow scan and active stack fingerprinting
        a.  SYN scan                        -       Included
        b.  TCP connect                     -       Not cinluded(SYN scan is good enough)
        c.  ping sweep                      -       NI
        d.  UDP scan                        -       NI
        e.  FIN scan                        -       Included
        f.  NULL scan                       -       Included
        g.  XMAS scan                       -       included
        h.  Bounce scan                     -       NI
        I.  RPC scan                        -       NI
        J.  Windows Scan                    -       NI
        K.  Idle scan                       -       NI
        L.  TCP Reverse Ident Scan          -       NI
        M.  UDP ICMP port scan              -       NI
        N.  sctp scan                       -       Included (SCTP enabled machines, Telecom oriented machines carrying SS7 and SIGTRAN over IP)
        O.  Maimon scan                     -       Included (BSD-derived systems simply drop the packet if the port is open)
        P.  Protocol Scan                   -      Included 

    2. use nmap-vulners,vulscan,vuln to identify CVEs
        a.  To install vulscan follow below steps
            i.  git clone https://github.com/scipag/vulscan scipag_vulscan
            ii. ln -s `pwd`/scipag_vulscan /usr/share/nmap/scripts/vulscan
        b.  to Install Nmap-vulners follow below steps
            i.  cd /usr/share/nmap/scripts/
            ii. git clone https://github.com/vulnersCom/nmap-vulners.git
    3. Capture shell outputs logs and network packets logs using scapy
        a.  Use multithreading to capture 
    4. Filter required logs
    5. Currently subprocess stout is piped and it can be written directly to a file. Refer
    https://stackoverflow.com/questions/4856583/how-do-i-pipe-a-subprocess-call-to-a-text-file
    Also use nmap command to directly output the stdout to a file.

'''
######################################################


#process = subprocess.Popen(['echo', 'More output'],
#                     stdout=subprocess.PIPE, 

#                     stderr=subprocess.PIPE)
#stdout, stderr = process.communicate()
#print(stdout)
#print(stderr)


list_port = []
host_MAC_Addr = ''
count = 0

#array for doing different scan
scan_array = ['-sS', '-sF', '-sX', '-sN', '-sW', '-sM', '-sY', '-sO', '-sT', '-sU']


def tcpdump_capture(exit_event, work_queue, filename_pcap):
    while not exit_event.is_set():
        try: work = work_queue.get(timeout=1.0)
        except queue.Empty: continue

        print("Starting tcpdump..")
        p = subprocess.Popen(['sudo','tcpdump', '-i', iface, 'host', sys.argv[1],'-s', '65535',
                  '-w', filename_pcap], stdout=subprocess.PIPE)

    print("Stopping tcpcapture ...")
    p.send_signal(subprocess.signal.SIGTERM)



#loop for doing each scan
for each_scan_options in scan_array:

    #creating log file with time stamp
    ts = time.time()
    suffix = datetime.datetime.fromtimestamp(ts).strftime('%Y%m%d-%H%M%S')
    filename = "Nmap"+ each_scan_options + "-" + str(suffix) + ".txt"
    mode = 'a' if os.path.exists(filename) else 'w'
    file_desc = open(filename, mode) 


    # starting time
    start = time.time() 

    print("Starting ", each_scan_options, " scan...")
    #open subproces for scan
    process = subprocess.Popen(['sudo', 'nmap',each_scan_options,'-p-',sys.argv[1], '-e', iface],
                         stdout=subprocess.PIPE, 
                         stderr=subprocess.PIPE)
    #stdout, stderr = process.communicate()
    #print(process.stdout.readline())
    #print("Command passed is {}".format(process.args))


    #loop for readingout each stdout
    while True:
        line = process.stdout.readline()
        file_desc.write(line.rstrip().decode('utf-8'))
        file_desc.write("\n")
        if not line:
            break
        #print(line.rstrip().decode('utf-8'))
        if line.rstrip().decode('utf-8').find('tcp') > 0 and line.rstrip().decode('utf-8').find('/') > 0 : 
            index_find = line.rstrip().decode('utf-8').find('/')
            #str(line.rstrip().decode('utf-8').find("Address:")) + list_port
            #print("index find ", index_find)
            if index_find > 0:
                if count == 0:
                    if not str(line.rstrip().decode('utf-8')[0:index_find]) in list_port:
                        list_port.append(str(line.rstrip().decode('utf-8')[0:index_find]))
                    count = count + 1
                #print(str(line.rstrip().decode('utf-8')[0:index_find]))

                else:
                    if not str(line.rstrip().decode('utf-8')[0:index_find]) in list_port:
                        list_port.append(str(line.rstrip().decode('utf-8')[0:index_find]))
        if line.rstrip().decode('utf-8').find('Address:') > 0:
            #print(line.rstrip().decode('utf-8'))
            host_MAC_Addr = (line.rstrip().decode('utf-8')[line.rstrip().decode('utf-8').find('Address:')+len('Address:'):]).strip()
    print(each_scan_options, " scan completed.")
    file_desc.close()
    

    # end time
    end = time.time()
    # total time taken
    print("Runtime for  ", str(each_scan_options), "scan is ", "{0:02.0f}:{1:02.0f}".format(*divmod((end - start) * 60, 60)))


if not list_port:
    print("No open/filtered ports are identified")
    sys.exit()

#iterating through each vulnerability scan
vuln_scan_array = ['nmap-vulners', 'vul','vulscan']

#loop through each vuln scan
for each_scan in vuln_scan_array:

    print("Creating file for vuln scanning logs")
    ts = time.time()
    suffix = datetime.datetime.fromtimestamp(ts).strftime('%Y%m%d-%H%M%S')
    filename = "Nmap-" + each_scan + "-" + str(suffix) + ".txt"
    filename_pcap = "Nmap-"+ each_scan + "-" + str(suffix) + ".pcap"
    mode = 'a' if os.path.exists(filename) else 'w'
    file_desc = open(filename, mode) 


    length = len(list_port)
    i = 0
    list_ports=[]
    

    print("Creating list for identified ports")
    while i < length:
        if i == 0 :
            list_ports = list_port[i]
        else :
            list_ports = list_ports + "," + list_port[i]
        i = i + 1
    print(list_ports)


    #######################################################################################################
    #section for initiating multiprocessing worker and queue for capturing network logs


    # Save a reference to the original signal handler for SIGINT.
    default_handler = signal.getsignal(signal.SIGINT)

    # Set signal handling of SIGINT to ignore mode.
    signal.signal(signal.SIGINT, signal.SIG_IGN)


    exit_event = Event()
    work_queue = Queue()


    # Spawn the worker process.
    cp= Process(target=tcpdump_capture, args=(exit_event, work_queue, filename_pcap),)
    cp.start()

    # Since we spawned all the necessary processes already,
    # restore default signal handling for the parent process.
    #signal.signal(signal.SIGINT, default_handler)


    # Send some integers to the worker process.
    work_queue.put(0)


    ######################################################################################################



    #Need to include logs capture to a file
    print("identified port - ", str(list_ports))
    print("Running nmap-vulners script....")
    process = subprocess.Popen(['sudo', 'nmap','--script',each_scan,'-sV',sys.argv[1],'-p',list_ports, '-e', iface],
                             stdout=subprocess.PIPE, 
                             stderr=subprocess.PIPE)

    while True:
        line = process.stdout.readline()
        file_desc.write(line.rstrip().decode('utf-8'))
        file_desc.write("\n")
        if not line:
            break
    file_desc.close()
    

    #####################################################################################################

    #adding this sleep time to avoid slow spawning worker process. increase sleep time if tcpdump process kill command executed before process open
    #time.sleep(1) #this may not be required for now since nmap scan will take time
    exit_event.set()
    cp.join()



    ####################################################################################################


