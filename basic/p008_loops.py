#!/usr/bin/env python

# This module explains the usage of loops in python

# Below is a simple for and while loop
for x in range(0, 3):
  print "We're on time %d" % (x)

x = 1
while x<10:
    print "We're on %d now!" % (x)
    x += 1

# xrange is used much more frequently than range. This is for
# one reason only - resource usage. The range function generates
# a list of numbers all at once, where as xrange generates them
# as needed. This means that less memory is used, and should the for
# loop exit early, there's no need to waste time creating the unused numbers
for x in xrange(1, 11):
  for y in xrange(1, 11):
    print '%d * %d = %d' % (x, y, x*y)

# The else stub is executed only when the or loop is not
# completely executed, which may be to some break satement
# xrange(lower, upper, jump)
for x in xrange(3):
  print x
else:
  print 'Final x = %d' % (x)

while x > 10:
  print x
  break
else:
  print 'Final x = %d' % (x)

# We can also iterated over objects
list_of_lists = [ [1, 2, 3], [4, 5, 6], [7, 8, 9]]
for list in list_of_lists:
  for x in list:
    print x

