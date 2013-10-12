#!/usr/bin/env python

# This moodule explains file handling in python

import sys

# The following code opens the file in w (write) mode. Note that in write mode
# if the file doesnt exist, file is created and if the file exists then its
# contents will be overwritten. Other modes are r (read), a (append) etc.
# Notice that we have userd to write() to write line to file, we can also
# writelines() to write a "list of strings" to the file
fd = open("new_file.txt", "w")
print "Opening file %s in %s mode" % (fd.name, fd.mode)
for i in xrange(10):
  fd.write("This is line number " + str(i) + "\n" )

fd.close()

# We can use readlines() function which will return a list of all the lines in the
# file, but this could fail in case of BIG files as we might run out of memory. So we use
# xreadlines() which does not return a list of lines, but an iterator, which
# returns one line at a time, when the for loop calls it. Another method to
# read a file would be using the read() method which when passed arguments will
# try to read as many bytes and if not then will try to read as much bytes it
# can or till the EOF.
fd = open("new_file.txt", "r")
for line in fd.xreadlines():
  print line
fd.close()

# or we can also do the following
for line in open('new_file.txt'):
#  sys.stdout.write(line.rstrip())
    print line

# Below we see how we can locate and change the position of the file descriptor
fd = open("new_file.txt", "r+")
strn = fd.read(10);
print "Read String is : ", strn
print "Current file position : ", fd.tell()
# Reposition pointer at the beginning, the first argument indicates the number
# of bytes to be moved and the second argument specifies the reference position
# from where the bytes are to be moved
fd.seek(0, 0)
print fd.tell()
fd.close()
