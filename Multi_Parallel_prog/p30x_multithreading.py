#!/usr/bin/env python

from threading import Thread
import urllib
import re

# this function takes url as the arg. and gets the title site
# read func. reads the html response of the site.
def th(url):
  regex = "<title>.+?</title>"
  pattern = re.compile(regex)
  html = urllib.urlopen(url).read()
  results = re.findall(pattern, html)
  print results


# list of sites to open
urls = "http://google.com/ http://cnn.com/ http://yahoo.com/ http://www.wikipedia.org/".split()

threadlist = []

for u in urls:
# to create a thread function we use the "Thread" function
# this function takes a target which is a function and the args
# that we nee to pass to the func.
# Notice the "," after the arg "u"
  t = Thread(target=th, args=(u,))
  t.start()
  threadlist.append(t)

# this for loop join back the threads back to main memory
for b in threadlist:
  b.join()
