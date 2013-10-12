#!/usr/bin/env python

# This module explains the usage of threads in python
import thread
import time

def thread(id):
  print "Thread with ID %d has been created" %(id)

  count = 1
  while True:
    print "Thread with ID %d has counter value %d" %(id, count)
    time.sleep(1)
    count += 1

# Below is how we start a new Thread.
for i in xrange(5):
  thread.start_new_thread(thread, (i,))

