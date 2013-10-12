#!/usr/bin/env python

# This module explains the usage of sets in python

# Set are unordered collection of unique objects
setA    = set([1,2,3,3,2])         # set([1,2,3])
setB    = set([3,4,5])             # set([3,4,5])
setC    = set("obtuse")            # set(['b', 'e', 'o', 's', 'u', 't'])

# We can perform various types of operation on sets
# such union, intersection, difference

setA | setB             # set([1,2,3,4,5]) union
setA.union(setB)
setA & setB             # set([3]) intersection
setA.intersection(setB)
setB - setA             # set([1,2]) difference
setB.difference(setA)

# Membership testing
3 in setA               # True
3 in setB               # False
setA.issubset(set([1,2,3,4,5,6,7,8,9])) # True
setA.issuperset(setB)                   # False

# We can also add new elements to a set
setA.update([1,3,10,11])            # set([1,2,3,10,11])
