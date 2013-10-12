#!/usr/bin/env python

# This module explains the usage of threading module in python
# using Queue.

import threading
import Queue
import time


# PMOTW example
def worker():
    print threading.currentThread().getName(), 'Starting'
    time.sleep(1)
    print threading.currentThread().getName(), 'Exiting'

def my_service():
    print threading.currentThread().getName(), 'Starting'
    time.sleep(1)
    print threading.currentThread().getName(), 'Exiting'

# Below we see the different ways we can call the threading function
# the basic argument is the worker function to which we can pass the
# the name for the Thread.
t = threading.Thread(name='my_service', target=my_service)
w = threading.Thread(name='worker', target=worker)
w2 = threading.Thread(target=worker) # use default name

w.start()
w2.start()
t.start()
print
print

# Below we extend the threading.thread class to declare a
# custom run function

class Worker(threading.Thread):

    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue

    def run(self):
        print "This is the worker thread"
        while True:
            counter = self.queue.get()
            print "Thread will sleep for %d seconds" %(counter)
            time.sleep(counter)
            print "Thread finished its sleeping time of %d" %(counter)
            self.queue.task_done()

queue = Queue.Queue()

for i in range(10):
    print "Deamon worker %d created" %(i)
    worker = Worker(queue)
    worker.setDaemon(True)
    # start will invoker the run funtion of our Worker class
    worker.start()

# now we assign each of these deamon threads
for i in range(10):
    queue.put(i)

queue.join()
