#!/usr/bin/env python3
import time, queue, signal, subprocess
from multiprocessing import Process, Event, Queue


def tcpdump_capture(exit_event, work_queue):
    while not exit_event.is_set():
        print("Entering while loop")
        try: work = work_queue.get(timeout=1.0)
        except queue.Empty: continue

        print("Starting tcpdump..")
        p = subprocess.Popen(['sudo','tcpdump', '-i', 'eth0', '-s', '65535',
                  '-w', 'cap' + str(work) + '.pcap'], stdout=subprocess.PIPE)

    print("Stopping tcpcapture ...")
    p.send_signal(subprocess.signal.SIGTERM)
    print("tcpdump completed")



# Save a reference to the original signal handler for SIGINT.
default_handler = signal.getsignal(signal.SIGINT)

# Set signal handling of SIGINT to ignore mode.
signal.signal(signal.SIGINT, signal.SIG_IGN)


exit_event = Event()
work_queue = Queue()

print("exit_event  - " + str(exit_event.is_set()))

# Spawn the worker process.
cp= Process(target=tcpdump_capture, args=(exit_event, work_queue),)
cp.start()

# Since we spawned all the necessary processes already,
# restore default signal handling for the parent process.
signal.signal(signal.SIGINT, default_handler)


# Send some integers to the worker process.
for x in range(2):
    work_queue.put(x)

print("Setting exit event")

#adding this sleep time to avoid slow spawning worker process. increase sleep time if tcpdump process kill command executed before process open
time.sleep(1)
exit_event.set()
cp.join()



