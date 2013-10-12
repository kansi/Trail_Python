#!/usr/bin/env python

# This module explains the polymorphism in OOP python

# When two objects of different classes support the same set of messages but with
# their own corresponding methods then we can treat them identically but the objects
# will behave differently. This ability to behave differently to the same input
# messages is known as polymorphism.

class Square:
  def __init__(self, side):
    self.side = side

  def calculateArea(self):
    return self.side**2

class Circle:
  def __init__(self, radius):
    self.radius = radius

  def calculateArea(self):
    import math
    return math.pi*(self.radius**2)

lst = [Circle(5),Circle(7),Square(9),Circle(3),Square(12)]
for shape in lst:
  print "The area is: ", shape.calculateArea()
