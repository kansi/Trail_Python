#!/usr/bin/env python

""" This class shows   """
class Date:
  def __init__(self, month, day, year):
    self.month = month
    self.day   = day
    self.year  = year


  def display(self):
    return "{0}-{1}-{2}".format(self.month, self.day, self.year)


  @staticmethod
  def millenium(month, day):
    return Date(month, day, 2000)

new_year = Date(1, 1, 2013)               # Creates a new Date object
millenium_new_year = Date.millenium(1, 1) # also creates a Date object.

# Proof:
new_year.display()           # "1-1-2013"
millenium_new_year.display() # "1-1-2000"

isinstance(new_year, Date) # True
isinstance(millenium_new_year, Date) # True



