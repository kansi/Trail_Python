#!/usr/bin/env python

# This module explains encapsulation in OOP python

# In python we every thing is public. Even though we cannot have private
# attributes in Python, you can use the following agreements.
# Attributes preceded with a single underscore (for example, _n) are to be
# viewed as internal variables, not to be used externally and those starting
# with double underscores (for example, __n) aren't explicitly exported. They
# are renamed to _Class__Variablenamewhen byte compiled.

class Number:
  def __init__(self, value):
    self._n = value
    self.__n = value

  def __repr__(self):
    return '%s(%s)'% (self.__class__.__name__, self._n)

  def add(self, value):
    self._n = self._n + value

  def incr(self):
    self._n = self._n + 1

a = Number(20)
print a                 # Number(20)
print a._n              # 20
print a._Number__n      # 20

# Below we will see how we can use default arguments in storing the environment
# variables in a variable from the class namespace, the next example
# initializes the value of the variable n by using a default argument. The
# value of n is assigned at the time of defining the function and is stored at
# the class namespace
v=10
class C:
  def storen(self, n=v):
    return n

objA = C()
objA.storen()           # 10
v=20
objB = C()
objB.storen()           # 10

# Next we hide the a() method definition by preceding it with two underscores.
# Note that if you later need to access this method (and you don't want to rename it),
# you must create a reference to the method, as shown in the following example
class C:
  def __a(self):
    print "ni!"

  b = __a

a=C()
a.b()           # ni!
