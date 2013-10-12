#!/usr/bin/python

# This module demonstrates how to get command line flags/arguments

import sys, getopt

def Usage ():
  print "arguments.py [-v][-p][-h]"

try:
  optlist, list = getopt.getopt(sys.argv[1:], ’:vph’)
except getopt.GetoptError:
  Usage()
  print "incorrect argument given"
  sys.exit(1)

for opt in optlist:
  if opt[0] == ’-h’:
    Usage()
  if opt[0] == ’-v’:
    print "verbose found"
  if opt[0] == ’-p’:
    print "probeonly found"


