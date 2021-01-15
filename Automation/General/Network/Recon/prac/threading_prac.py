from threading import Thread 
def threaded_function(arg): 
    for i in range(arg): 
        print("python guides")


thread = Thread(target = threaded_function, args = (3, ))
thread.start()
thread.join()
print("Thread Exiting...")
