#!/usr/bin/env python


# from io import StringIO
from cStringIO import StringIO

# module StringIO allows you to treat a data stream like a file
# if you do a lot of processing, memory streams are much faster then file streams

# Below example shows how to use and stringIO and when not to use it. As when u
# run this code you will see that meth3() is the fastest because here we are just
# multiplying a string a 100 times, but If you want to create a bunch of strings,
# and then join them, meth1() is the correct way.
# StringIO is namely a string with a file-like stream interface.

def meth1(string):
  a = []
  for i in range(100):
    a.append(string)
  return ''.join(a)

def meth2(string):
  a = StringIO()
  for i in range(100):
    a.write(string)
  return a.getvalue()

def meth3(string):
  return string * 100

if __name__ == '__main__':
  from timeit import Timer
  string = "This is test string"
  print(Timer("meth1(string)", "from __main__ import meth1, string").timeit())
  print(Timer("meth2(string)", "from __main__ import meth2, string").timeit())
  print(Timer("meth3(string)", "from __main__ import meth3, string").timeit())

# It's used when you have some API that only takes files, but you need to use a
# strings. Below is an advanced example
import gzip
import StringIO

stringio = StringIO.StringIO()
gzip_file = gzip.GzipFile(fileobj=stringio, mode='w')
gzip_file.write('Hello World')
gzip_file.close()

stringio.getvalue()

# Following is a usage mentioned on stack-overflow
# http://stackoverflow.com/questions/7996479/what-is-stringio-in-python-used-for-in-reality

# Whole-file caching. I have a script that reads PDFs and does validation of
# various things about them. The PDF library I'm using takes an open file in
# its document constructor. I originally just opened the PDF I was interested
# in reading, however when I changed it to read the entire file at once into
# memory then pass a StringIO object to the PDF library, the running time of
# my script was cut in half.
