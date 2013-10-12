#!/usr/bin/env python

from threading import Thread
import urllib
import re

# this function takes url as the arg. and gets the title site
# read func. reads the html response of the site.

def th(url):
    base = "http://in.finance.yahoo.com/q?s="+url
	regex = '<span id="yfs_184_'+url+'">.+?</span>'
	pattern = re.compile(regex)
	html = urllib.urlopen(base).read()
	results = re.findall(pattern, html)
	print results

# one need to have the keword used for different stocks to get the data
# suppose we have those in the variable symbolsist

threadlist = []

for u in symbolslist:
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
