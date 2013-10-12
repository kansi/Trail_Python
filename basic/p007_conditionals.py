#!/usr/bin/env python

# this module explains the usage of conditionals in python

name = raw_input("What is ur name? ")

print "Welcome %s" % name


# we use any type of complex conditionals after if.
# the else stub is optional, it is used to specify what
# the program should do in case "if" fails

if name == "kansi":
  print "You are the admin"
else
  print "You are a guest user"


x = raw_input("Enter interger b/w 0-2: ")
# We can also use "elif" instead of using "else if"
if x==0:
    print "Hello"
elif x==1:
    print "bye"
elif x==2:
    print "Wait..."
else:
    print "Nothing"

