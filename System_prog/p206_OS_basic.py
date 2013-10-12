#!/usr/bin/env python

import os

# This module explains the basic usage of the OS module in python

# os.environ list all the environment vars
for item in os.environ:
  print item, os.environ[item]

# getenv gets the environment var specified. similar results can achieved with
# os.environ["HOME"]
print os.getenv("HOME")

# get current working dir and we can change the cwd by using os.chdir(path)
print os.getcwd()
print os.uname()
# create single dir
os.mkdir("pyDir", 0666)
# Recursive directory creation
os.makedirs( "inside/pydir")

os.remove("pyDir")
os.removedirs("/tmp/inside")

# Files and dirs

# os.access(path, mode) is used to check the accessbility of a path on varoius
# parameters like existance, readbility, writability etc. There are 4 modes
# F_OK : to test the existence of path, R_OK : readability of path,
# W_OK : writability of path, X_OK : path can be executed.

if os.access("myfile", os.R_OK):
  with open("myfile") as fp:
    return fp.read()
else:
  return "some default data"

# os.listdir(path) returns a list all the files and folder in given path
print os.listdir('.')

# Working with file attributes using os module
def dump(st):
  mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime = st
  print "- size:", size, "bytes"
  print "- owner:", uid, gid
  print "- created:", time.ctime(ctime)
  print "- last accessed:", time.ctime(atime)
  print "- last modified:", time.ctime(mtime)
  print "- mode:", oct(mode)
  print "- inode/dev:", ino, dev

import time
# get stats for a filename, i.e. it return the various types of stats for that file.
st = os.stat(file)
print "stat", file
dump(st)

# get stats for an open file. fstat return status for file descriptor fd
fp = open(file)
st = os.fstat(fp.fileno())
print "fstat", file
dump(st)


