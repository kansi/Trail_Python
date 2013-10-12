#!/usr/bin/env python

# This code explains the usage of variables in python.
# that is how to assign variables in different ways

# Single assignment
counter = 100          # An integer assignment
miles   = 1000.0       # A floating point
name    = "John"       # A string

# Multiple Assignments
# the below code will assign the value 1 to a,b,c
# simultaneously
a = b = c = 1

# we can also assign multiple variables different
# values simultaneously
a, b, c = 1, 2, "john"

# Number data types store numeric values. They are immutable
# data types, which means that changing the value of a number
# data type results in a newly allocated object.
# to delete the reference to a number object we can use the del statement
var = 0
del var

# To see the exact memory where the variable is stored we can use the id()
# or use the __repr__ function
id(counter)
# to see the hex value use hex() to convert to hex
hex(id(counter))
# alternate method to see the memory
counter.__repr__
