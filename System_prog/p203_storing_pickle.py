#!/usr/bin/env python

# This module explains the usage of pickle module in python.
# Pickle is an important module whenever you need persistence between user sessions.
# The concept of pickling is known variously as serialisation, marshalling, or flattening.
#

import pickle

# Pickle library provides a a way to convert a python object (list, dict, etc.)
# into a character stream. The idea is that this character stream contains all
# the information necessary to reconstruct the object in another python script.

dic1 = {'I':1,'II':2,'III':3,'IV':4,'V':5,'VI':6,'VII':7,'VIII':8,'IX':9,'X':10}

# to save a Python object like a dictionary to a file
# and load it back intact you have to use the pickle module

print "Printing original dictionary ..."
print dic1

file = open("roman1.dat", "w")
# Below we store the pickle object in a file
pickle.dump(dic1, file)
file.close()

# Now we load back the pickled object.
file = open("roman1.dat", "r")
dic2 = pickle.load(file)
file.close()
print "Dictionary after pickle.load() from roman1.dat"
print dic2
