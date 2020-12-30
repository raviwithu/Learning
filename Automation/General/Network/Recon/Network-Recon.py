import subprocess, sys, os, time, datetime
from termcolor import colored


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
#The Follwoing functionality needs to be done
    1. Identify TCP and UDP port script with slow scan
        a.  Collect port open via SYN scan
        b.  TCP connect
        c.  ping sweep
        d.  UDP scan
        e.  FIN scan
        f.  NULL scan
        g.  XMAS scan
        h.  Bounce scan
        I.  RPC scan
        J.  Windows Scan
        K.  Idle scan

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

'''
######################################################


#process = subprocess.Popen(['echo', 'More output'],
#                     stdout=subprocess.PIPE, 
#                     stderr=subprocess.PIPE)
#stdout, stderr = process.communicate()
#print(stdout)
#print(stderr)

'''

print("SYN Scan...")
process = subprocess.run(['sudo', 'nmap','-sS','-p8000-8500',sys.argv[1]], 
                         stdout=subprocess.PIPE, 
                         universal_newlines=True)
print(len(process.stdout))
print("SYN scan done")
print(process.stdout)

'''

list_port = []
host_MAC_Addr = ''
count = 0

#array for doing different scan
scan_array = ['-sS', '-sF', '-sX', '-sN', '-sW']


#loop to do each scan
for each_scan_options in scan_array:

    #creating log file with time stamp
    ts = time.time()
    suffix = datetime.datetime.fromtimestamp(ts).strftime('%Y%m%d-%H%M%S')
    filename = "Nmap"+ each_scan_options + "-" + str(suffix) + ".txt"
    mode = 'a' if os.path.exists(filename) else 'w'
    file_desc = open(filename, mode) 

    #open subproces for scan
    process = subprocess.Popen(['sudo', 'nmap',each_scan_options,'-p-',sys.argv[1]],
                         stdout=subprocess.PIPE, 
                         stderr=subprocess.PIPE)
    #stdout, stderr = process.communicate()
    print(process.stdout.readline())

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
                    #list_port.append(str(line.rstrip().decode('utf-8')[0:index_find]))
                    count = count + 1
                #print(str(line.rstrip().decode('utf-8')[0:index_find]))

                else:
                    list_port.append(str(line.rstrip().decode('utf-8')[0:index_find]))
        if line.rstrip().decode('utf-8').find('Address:') > 0:
            #print(line.rstrip().decode('utf-8'))
            host_MAC_Addr = (line.rstrip().decode('utf-8')[line.rstrip().decode('utf-8').find('Address:')+len('Address:'):]).strip()
    file_desc.close()
'''
file_desc.write(str(list_port))
file_desc.write('\n')
file_desc.write(str(host_MAC_Addr))
file_desc.write('\n')
'''
'''
for each_line in stdout.readline():
    print(each_line)
    if each_line.find('tcp') and each_line.find('/'):
        index_find = each_line.find('/')
        #print("index find ", index_find)
        if index_find > 0:
            print(index_find)
            print(each_line[0:index_find])

'''


ts = time.time()
suffix = datetime.datetime.fromtimestamp(ts).strftime('%Y%m%d-%H%M%S')
filename = "Nmap-vulners-log" + str(suffix) + ".txt"
mode = 'a' if os.path.exists(filename) else 'w'
file_desc = open(filename, mode) 


print("identified port - ", str(list_port))
print("Running nmap-vulners script....")
process = subprocess.run(['sudo', 'nmap','--script','nmap-vulners','-sV',sys.argv[1],'-p','22222'], 
                         stdout=subprocess.PIPE, 
                         universal_newlines=True)
print(process.stdout)






print("Running default NSE, vulnscan script....")
process = subprocess.run(['sudo', 'nmap','--script','vuln,vulscan','-sV',sys.argv[1],'-p','22222'], 
                         stdout=subprocess.PIPE, 
                         universal_newlines=True)
print(process.stdout)
file_desc.close()

