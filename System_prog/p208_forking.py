#!/usr/bin/env python

# The module explains forking and spawning fo process in python
import os

# fork() operation creates a copy of the process that called it, in a separate
# address space for the child. The child process has an exact copy of all the
# memory of the parent process. The execution of the parent and child process is
# independent of each other. With the return value of fork() we can decide in which
# process we are: 0 means that we are in the child process while a positive return
# value means, that we are in the parent process.


def child():
    print 'A new child ',  os.getpid( )
    os._exit(0)

def parent():
    while True:
        newpid = os.fork()
        if newpid == 0:
            child()
        else:
            pids = (os.getpid(), newpid)
            print "parent: %d, child: %d" % pids

    if raw_input( ) == 'q': break

print "Forking a new process"
parent()

print "Spawning a new process"
# Notice that the first argument in the list is the process itself
os.execvp("ping", ["ping", "127.0.0.1"])
# Below how we spawn a new process. To this we use the exec*() family of
# functions :
# os.execl(path, arg0, arg1, ...)
# os.execle(path, arg0, arg1, ..., env)
# os.execlp(file, arg0, arg1, ...)
# os.execlpe(file, arg0, arg1, ..., env)
# os.execv(path, args)
# os.execve(path, args, env)
# os.execvp(file, args)
# os.execvpe(file, args, env)
# The difference is that the new process spawned will replace the current or
# the parent process. They do not return to the program which has called them.
# They even receive the same process ID as the calling program.
# Source : http://www.python-course.eu/forking.php
