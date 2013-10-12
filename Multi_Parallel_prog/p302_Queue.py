#!/usr/bin/env python

# This module explains the usage of Queues in python
# The Queue module provides a FIFO implementation suitable for multi-threaded
# programming. It provides a convenient way of moving Python objects between
# different threads. The queue module provides 3 types of Queues: FIFO, LIFO,
# PriorityQueue.


import Queue

q_fifo = Queue.Queue()
q_lifo = Queue.LifoQueue()

for i in range(5):
    # elements are added using put
    q_fifo.put(i)
    q_lifo.put(j)
#
def print_q( Qtype , q):
    print Qtype
    while not q.empty():
        # elements are removed using get
        print q_fifo.get()

print_q("FIFO Queue", q_fifo)
print_q("LIFO Queue", q_lifo)

# Notice below that the if the priority clashes then second item of the tuple
# can be used as a secondary priority.
prioQ = Queue.PriorityQueue()
prioQ.put((2, 8, 'super blah'))
prioQ.put((1, 4, 'Some thing'))
prioQ.put((1, 3, 'This the first One'))
prioQ.put((5, 1, 'blah'))

while not prioQ.empty():
    item = prioQ.get()
    print('%s.%s - %s' % item)

# Below is another usage of PriorityQueue.
# Source: PYMOTW
class Job(object):
    def __init__(self, priority, description):
        self.priority = priority
        self.description = description
        print 'New job:', description
        return

    def __cmp__(self, other):
        return cmp(self.priority, other.priority)

q = Queue.PriorityQueue()
q.put( Job(3, 'Mid-level job') )
q.put( Job(10, 'Low-level job') )
q.put( Job(1, 'Important job') )

while not q.empty():
    next_job = q.get()
    print 'Processing job:', next_job.description
##

