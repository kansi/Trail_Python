#!/usr/bin/env python

# This module explains the usage of threading module in python

import threading
import Queue
import time

# Below is the most basic usage of threads
def worker(num):
    print '%s : %s' % ( threading.currentThread().getName(), num)
    return

threads = []
# Notice that Thread() method takes the function and the args to the function
# as its arguments. Also notice that incase of a single argument to the
# function "," has been used
for i in range(5):
    t = threading.Thread(name = 'Worker '+str(i), target=worker, args=(i,))
    threads.append(t)
    # start() method starts a thread by calling the run method. this method will
    # raise a RuntimeError if called more than once on the same thread object.
    t.start()

# Below is the implemetation of a new thread. Notice that this class inherits
# threading module. Notice that upon execution of this code the parent process
# exists before its child processes.
# Souce : http://www.tutorialspoint.com/python/python_multithreading.htm
exitFlag = 0
class myThread (threading.Thread):
    # We define a custom init function in which we call the parent init func
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    # Below we define our custom run method which will be called when we
    # execute the thread i.e. self.start()
    def run(self):
        print "Starting " + self.name
        print_time(self.name, self.counter, 5)
        print "Exiting " + self.name

def print_time(threadName, delay, counter):
    while counter:
        if exitFlag:
            thread.exit()
        time.sleep(delay)
        print "%s: %s" % (threadName, time.ctime(time.time()))
        counter -= 1

# Create new threads
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

# Start new Threads
thread1.start()
thread2.start()

print "Exiting Main Thread"
