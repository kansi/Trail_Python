#!/usr/bin/env python

# This code explains the usage of strings in python

name    = "Jhon"       # Assings Jhon to name var
name    = 'Jhon'
mltiLn  = """This sting spans
             multiple lines """

stn     = "Ian\nBell"   # This is string having an escape sequence
print stn               # This will print Ian in 1st line and Bell in 2nd
stn     = r"Ian\nBell"  # r tell python that this is a raw string
print stn               # Ian\nBell

uni     = u'kansi'      # u tells python that this is a unicode string
ToStn   = str(uni)      # converts a given var to string
ToUni   = unicode(name) # converts to unicode

# Strings are immutable objects that is once assigned they cant be changed !!

str1    = "bar"
print str1[0]           # b
str1[0] = c             # this will give an error
str1    = "car"         # This will work because now the pointer points to whole new str object

bffr    = "A"*5         # AAAAA

# Below are some string methods that we can use to perform
# different operations on the string
mltiLn.split()            # ['This', 'sting', 'spans', 'multiple', 'lines']
mltiLn.find("kansi")      # -1
mltiLn.find("string")     # 4

# String Formating
print "My name is %s and i luv %s" % ("kansi", "python")
print "My name is %(name)s and i luv %(language)s" % {"name":"kansi", "language":"python"}
