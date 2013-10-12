#!/usr/bin/env python

# This module explains the directory traversal and listing contents of a dir.

import os

# to list the content of a given dir.
print os.listdir('/')

# below we check that a given item in the list is dir or file
for item in os.listdir('/'):

  if os.path.isfile(item):
    print "file \t %s" %(item)
  elif os.path.isdir(item):
    print "dir \t %s" %(item)
  else
    print "unknown \t %s" %(item)


# Below we see the basic usage of glob module in python. glob is a module which is
# used to list files on the filesystem with names matching a pattern.
import glob

for item in glob.glob(os.path.join(".", "*")):
  print item

# below is single character wild card
for name in glob.glob('./p00?.py'):
  print name

for name in glob.glob('./p0[0-9][0-9]*.py'):
  print name

# When we have a very lage file listing glob is not a good option, so we use
# fnmatch
import fnmatch

# fnmatch() method returns true or false for a given input name and the pattern
for item in os.listdir('.'):
  # to do case-sensitive search use fnmatch.fnmatchcase()
  if fnmatch.fnmatch(item, 'p00[0-9]*.py')
    print item

# filter() return a list of all the name that matched the given pattern
for item in fnmatch.filter(os.listdir('.'), 'p00[0-9]*.py'):
  print item

# below we se how fnmatch internally converts the given pattern to a regex
# using the re module
pattern = 'p00?_*.py'
print 'Pattern :', pattern
print 'Regex   :', fnmatch.translate(pattern)
