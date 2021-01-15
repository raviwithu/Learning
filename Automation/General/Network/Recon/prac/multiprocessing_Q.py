#!/usr/bin/env python3
import time
import queue
import signal
from multiprocessing import Process, Event, Queue


# The worker is intentionally too much lazy!
def lazy_ass_worker(exit_event, work_queue):
    while not exit_event.is_set():
        try: work = work_queue.get(timeout=1.0)
        except queue.Empty: continue

        print("I did job {} already! :)".format(work))
        print("A small nap won't hurt anyone!")
        time.sleep(1.0)

    print("Doing cleanup before leaving ...")

# Save a reference to the original signal handler for SIGINT.
default_handler = signal.getsignal(signal.SIGINT)

# Set signal handling of SIGINT to ignore mode.
signal.signal(signal.SIGINT, signal.SIG_IGN)

exit_event = Event()
work_queue = Queue()

# Spawn the worker process.
cp= Process(target=lazy_ass_worker, args=(exit_event, work_queue),)
cp.start()

# Since we spawned all the necessary processes already,
# restore default signal handling for the parent process.
signal.signal(signal.SIGINT, default_handler)


# Send some integers to the worker process.
for x in range(100):
    work_queue.put(x)

# We wait for CTRL+C from the user.
try: signal.pause()
except KeyboardInterrupt:
    # Since our worker is too delicate, we should notify it with the
    # exit event and then wait for it's safe arraival / joining.
    exit_event.set()
    cp.join()
