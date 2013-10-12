#!/usr/bin/env python

import smtplib
from getpass import getpass

toAdrr     = raw_input("To : ")
senderAddr = raw_input("From : ")
msg        = raw_input("Message :\n")

# Gmail credentials
print "Please provide your gmail username and password"
username = raw_input("username : ")
password = getpass("Password : ")

# Send Mail
server = smtplib.SMTP('smtp.gmail.com:587')
## Required by gmail
server.starttls()
server.login(username,password)
server.sendmail(senderAddr, toaddrs, msg)
##
server.quit()
