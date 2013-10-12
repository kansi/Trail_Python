#!/usr/bin/env python

#this python file shows how to do OOP in python

class DateTimeClass():

  #this funciton is called the initialiser
  #it run when the class is created
  def __init__(self, day, month, year):
      self.day = day
      self.month  = month
      self.year = year

  #the repr is ment to be usable for understanding the object
  #Notice that %r has been used to print or we're defeating the goal of rep
  #the repr is helps differentiate DateTimeClass("3", "4", "2013") and DateTimeClass(3,4,2013)
  def __repr__(self):
      return "%r/%r/%r" % (self.day, self.month, self.year)

  #the goal of __str__ is to readble, hence in implementation str is optional
  #if repr is defined and string is not then repr == str
  #def __str__(self):
  #  return "Custom Print2\n value of day: %s\n value of month: %s\n value of year: %s" % (self.day, self.month, self.year)



instance = DateTimeClass(3,6,2013)
print instance
