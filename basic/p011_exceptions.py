#!/usr/bin/env python

# This module explains exception handling in python

# The following code displays exception handling
name = ["kansi","vansh","jhon"]
def exception(order):
  try:
    if order < 10:
      data = name[order]
    else:
      data = NULL
    return data
  except IndexError:
    return "This name is not in the list."

print exception(0)                # kansi
print exception(8)                # This name is not in the list.


# Raising exceptions: Notice in the below code we raise custom exception in our
# code according to the logic of our code
try:
  i=1
  while i < 10:
    for j in xrange(1,5):
      print i,j
      if (i==2) and (j==3):
        raise RuntimeError("This is a custom error\ni=2 and j=3 is a special case.")
    i = i + 1
except Exception as err:
  print err

# Now we see how to use the try/finally and try/else clause in exception handling. The
# finally clause is executed not matter what happens and the else clause is
# execute only when the try clause executes successfully. Notice the line
# "except Exception as e", we can use this when we dont know the type of exception.
def test(a,b):
  try:
    c = a/b
  except Exception as err:
    print err
  else:
    print c
  finally:
    print "This is always executed"

#print "\n---Try/finally try/else usage---\n"
test(5,0)
test(5,1)

# Below code implements user-defined error handling. Notice that MyError class
# inherits the python's Exception handling class and overrides the default init
# and str functions
class MyError(Exception):
  def __init__(self, value):
    self.value = value

  def __str__(self):
    return repr(self.value)

try:
  raise MyError(2*2)
except MyError as e:
  print 'My exception occurred, value:', e.value
