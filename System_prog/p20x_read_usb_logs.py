#!/usr/bin/env python

# This is practice code that reads usb messages from /var/log/messages

fd = open("/var/log/messages", "r")

for line in fd.xreadlines():
  if "usb" in line.lower().split():
    print line.strip('\n')

fd.close()
