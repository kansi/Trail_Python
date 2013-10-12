#!/usr/bin/env python

# This module describes the basics of OOP in python

# Below is a sample declaration of a class. We use the class keyword to declare
# a class. Notice that the class name begins with capital "C", this is purely
# convention, but it is fairly widely used and the class methods begin with
# lowecase letters.
class Calculator:
    # The following funtions is executed when we create an
    # create an object from a class (also reffered to as constructor).
    # Notice that the first argument to a function is the class itself.
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.ans

    def add(self):
        return self.ans = self.a + self.b

    def multiply(self):
        return self.ans = self.a * self.b

    #the repr is ment to be usable for understanding the object
    #Notice that %r has been used to print or we're defeating the goal of rep
    #the repr is helps differentiate DateTimeClass("3", "4", "2013") and DateTimeClass(3,4,2013)
    def __repr__(self):
          return "Answer is %r" % (self.ans)

    #the goal of __str__ is to readble, hence in implementation str is optional
    #if repr is defined and string is not then repr == str
    #def __str__(self):
    #  return "Custom Print2\n value of day: %s\n value of month: %s\n value of year: %s" % (self.day, self.month, self.year)

    # special method __del__(), called a destructor, that is invoked when
    # the instance is about to be destroyed.
    def __del__(self):
        class_name = self.__class__.__name__
        print class_name, "destroyed"

calculation = Calculator(10,20)

print calculation.add()
print calculation.multiply()
del calculation

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
    #    return "Custom Print2\n value of day: %s\n value of month: %s\n value of year: %s" % (self.day, self.month, self.year)

instance = DateTimeClass(3,6,2013)
print instance
