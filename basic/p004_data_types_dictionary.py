#!/usr/bin/env python

# This code explains the usage of dictonaries in
# python.
# Python dictionaries are kind of hash table type and
# consist of key-value pairs

# Declaring and adding key value pairs to dict can be done
# in the following way
dict1 = {}
dict1['one'] = "This is one"
dict1[2]     = "This is two"

week = {"Wed":"Wednesday", "Sun": "Sunday", "Mon": "Monday", "Tue":"Tuesday", "Thu": "Thursday", "Fri": "Friday", "Sat":"Saturday"}

# Following are the methods that can be perfored on a dict
## Get all the keys of a dict
week.keys()                 # ['Wed', 'Sun', 'Fri', 'Tue', 'Mon', 'Thu', 'Sat']
## Get values related to all the keys in a dict
week.values()               # ['Wednesday', 'Sunday', 'Friday', 'Tuesday', 'Monday', 'Thursday', 'Saturday']
## Check if the dict has a particular key or not
week.has_key("Mon")         #True
## Return all of the items in the dict as a sequence of (key,value) tuples.
## Note that these are returned in no particular order.
week.items()  # [('Wed', 'Wednesday'), ('Sun', 'Sunday'), ('Fri', 'Friday'), ('Tue', 'Tuesday'),
              #  ('Mon', 'Monday'), ('Thu', 'Thursday'), ('Sat', 'Saturday')]

## clear all the keys of a dict.
dict1.clear()

## remove a key,value pair from dict
week.pop("Mon")             # {'Fri': 'Friday', 'Sat': 'Saturday', 'Sun': 'Sunday', 'Thu': 'Thursday',
                            #  'Tue': 'Tuesday', 'Wed': 'Wednesday'}

del week["Tue"]             # {'Fri': 'Friday', 'Sat': 'Saturday', 'Sun': 'Sunday', 'Thu': 'Thursday', 'Wed': 'Wednesday'}

## To change the value of a key
week["Wed"] = "New day"     # {'Fri': 'Friday', 'Sat': 'Saturday', 'Sun': 'Sunday', 'Thu': 'Thursday',
                            #  'Tue': 'Tuesday', 'Wed': 'New day'}
