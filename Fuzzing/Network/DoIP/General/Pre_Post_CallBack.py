import os, sys,time,subprocess,signal, queue, datetime, platform
response =  ""
from multiprocessing import Process, Event, Queue
count = 0
from boofuzz import *
#global cp,p,default_handler, exit_event,work_queue
#######################################################################################################
#section for initiating multiprocessing worker and queue for capturing network logs
mylogger = FuzzLoggerText()


def tcpdump_capture(exit_event, work_queue, filename_pcap):
    while not exit_event.is_set():
        try: work = work_queue.get(timeout=1.0)
        except queue.Empty: continue

        print("Starting tcpdump..")
        p = subprocess.Popen(['sudo','tcpdump', 'host', sys.argv[1],'-s', '65535',
                  '-w', filename_pcap], stdout=subprocess.PIPE)

    print("Stopping tcpcapture ...")
    p.send_signal(subprocess.signal.SIGTERM)


def post_test_callback(target, fuzz_data_logger, session, sock, *args, **kwargs):
 
    '''
    #####################################################################################################

    #adding this sleep time to avoid slow spawning worker process. increase sleep time if tcpdump process kill command executed before process open
    #time.sleep(1) #this may not be required for now since nmap scan will take time
    exit_event.set()
    cp.join()
    '''
    print("In post test callback fill me here")
    #response = os.system("ping -c 1 " + sys.argv[1])
    response = subprocess.Popen(["ping","-c","1",sys.argv[1]],
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    print("ping response - " + str(response.stdout.readline()))
    while True:
        line = response.stdout.readline()
        if line.rstrip().decode('utf-8').find('time=') > 0:
            print(line.rstrip().decode('utf-8').split('time=')[1])
            if float(line.rstrip().decode('utf-8').split('time=')[1].replace(" ms", ""))>3.000:
                print("Delayed reponse")
                break
            else:
                break

def pre_test_callback(target, fuzz_data_logger, session, sock, *args, **kwargs):
    print("in pre test")
    print(fuzz_data_logger._cur_test_case_id)
    suffix = '{0:%Y%m%d_%H%M%S}'.format(datetime.datetime.now())
    filename_pcap = sys.argv[0].replace(".py","") + str(suffix)+".pcap"
    '''
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

    '''

    print("In pre test callback fill me here")
    # pre test callback called after TCP syn connection is created or right before sending fuzzing payload
    print(sys.argv[0])
    if sys.argv[0] != "DoIP_RoutingActivation_Request.py":
        target.send(b"2fd00050000000b0e00000000000000000000") # this sends routing activation request
        time.sleep(1)
        if sys.argv[0] != "Req_Tester_Pre.py":
            target_send(b"02fd8001000000060e00e4003e80")
            time.sleep(1)
            if sys.argv[0] != "Req_Diag_Sess_Ctrl.py":
                target.send()




# a monitor to verify if the target is still alive
# noinspection PyMethodOverriding
# noinspection PyMethodParameters
class spaceTargetMonitor(NetworkMonitor):
    def alive():
        global g_target_ip_addr
        g_target_ip_addr = sys.argv[1]
        param = "-n" if platform.system().lower() == "windows" else "-c"
        # Russian Sub Commander Marco Ramius requests one ping only
        command = ["ping", param, "1", g_target_ip_addr]
        # noinspection PyTypeChecker
        message = "alive() sending a ping command to " + g_target_ip_addr
        mylogger.log_info(message)
        try:
            subprocess.run(command, timeout=3)
        except subprocess.TimeoutExpired:
            return False
        else:
            mylogger.log_info("PING success")
            return True

    def pre_send(target=None, fuzz_data_logger=None, session=None, **kwargs):
        if sys.argv[0] != "DoIP_RoutingActivation_Request.py":
            target.send(b"2fd00050000000b0e00000000000000000000") # this sends routing activation request
            time.sleep(1)
            if sys.argv[0] != "Req_Tester_Pre.py":
                target_send(b"02fd8001000000060e00e4003e80")
                time.sleep(1)
                if sys.argv[0] != "Req_Diag_Sess_Ctrl.py":
                    target.send()
        return

    def post_send(target=None, fuzz_data_logger=None, session=None, **kwargs):
        return True

    def retrieve_data():
        return

    def start_target():
        return True

    def set_options(*args, **kwargs):
        return

    def get_crash_synopsis():
        return "get_crash_synopsis detected a crash of the target."

    def restart_target(target=None, **kwargs):
        mylogger.log_info("restart_target sleep for 12")
        time.sleep(12)
        if spaceTargetMonitor.alive() is True:
            mylogger.log_info("restart_target ok")
            return True
        else:
            mylogger.log_info("restart_target failed")
            return False

    def post_start_target(target=None, fuzz_data_logger=None, session=None, **kwargs):
        return
