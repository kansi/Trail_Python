#!/usr/bin/env python

# This module explains the operator/method overloading in OOP python

# Notice in this class we override the __str__ method to create our own custom
# display for this class. So now when we call print __str__ method is invoked
# to print the output. Remember that similar results can be achieved using
# __repr__ method which utilised by __str__ to in its implemention.
# just remember that __str__ is used to generate human friendly output.
# http://satyajit.ranjeev.in/2012/03/14/python-repr-str.html
# http://stackoverflow.com/questions/1436703/difference-between-str-and-repr-in-python/2626364#2626364
class Vector:
  def __init__(self, a, b):
    self.a = a
    self.b = b

  def __str__(self):
    return 'Vector (%d, %d)' % (self.a, self.b)

  # This function overrides the default addition operator
  def __add__(self,other):
    return Vector(self.a + other.a, self.b + other.b)

v1 = Vector(2,10)
v2 = Vector(5,-2)
print v1 + v2           # Vector(7,8)
