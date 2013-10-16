#!/usr/bin/env python

# This module shows how to create funtions in python

# Below is a simple python function. We use the "def" keyword
# to define a function and return keyword to return a value
def HelloWorld():
  return "Hello World !"

# We can define a function inside an class, module or another function
# Following is how we do this.
def g():
  def f():
    print "f() inner function"
  f()


class Some:
  def f():
    print "f() method"



# Functions in Python are objects. They can be manipulated like other objects
# in Python and these objects can be stored in collections and passed to functions.
def f():
  pass

def g():
  pass

def h(f):
  print hex(id(f))

a = (f, g, h)
# This for loop will print the location in the memory where these functions
# exist.
for i in a:
  print i
print h(f), h(g)


# Since python is dynamic in nature it is possible to redefine an already defined function.
def PrintMessage(msg):
  print msg

PrintMessage("Ready.")
def PrintMessage(msg):
  print "Function redifened",
  print msg

PrintMessage("Processing.")


# Parameters to a function are passed by refference, which is because process is
# faster and mutable objects that are modified in functions are permanently changed.
# The following example shows how we can pass pre-defined arguments to a
# function.
def power(x, y=2):
  r = 1
  for i in range(y):
    r = r * x
    return r

print power(3)
print power(3, 3)


# We can also specify the arguments with keywords, in which case the order of
# the arguments doesnt matter
def display(name, age, sex):
  print "Name: ", name
  print "Age: ", age
  print "Sex: ", sex

display(age=43, name="Lary", sex="M")
display(name="Joan", age=24, sex="F")
# A non-keyword argument may be followed by keyword arguments like display("Joan", sex="F", age=24)
# but non-keyword argument may NOT follow keyword arguments like display(age=24, name="Joan", "F")
# will give error


# We can also define function that can take arbitrary no of documnets.
# * operator to indicate, that the function will accept arbitrary number of arguments
def sum(*args):
  '''Function returns the sum of all values'''
  r = 0
  for i in args:
    r += i
    return r

print sum.__doc__               # output: Function returns the sum of all values
print sum(1, 2, 3)              # 6
print sum(1, 2, 3, 4, 5)        # 15


# We can also use the ** construct to pass dictionaries as argument
# notice that in this case, we can pass as many arguments we want.
def display(**details):
  for i in details:
    print "%s: %s" % (i, details[i])

display(name="Lary", age=43, sex="M")

# Similarly we can pass list as arguments, Below function will take
# the first arg in arg1 and the rest in vartuple.
def printinfo( arg1, *vartuple ):
    "This prints a variable passed arguments"
    print "Output is: "
    print arg1
    for var in vartuple:
        print var
        return;
printinfo( 10 );
printinfo( 70, 60, 50 );


# We can use "global" keyword to reference the variable defined outside the body of the function
name="kansi"
def PrintName():
  global name
  print "My name is", name



# We can create anonymous functions in Python using the keyword "lambda"
square = lambda x: x ** 2
square(2)
# We can use these more elegantly with map and reduce
cs = [-10, 0, 15, 30, 40]
ft = map(lambda t: (9.0/5)*t + 32, cs)
print ft


# Blow we see, how to pass a function as an argument to another function.
def executeFun(fun, *args):
    print fun(*args)
    return

executeFun(square, 2)
eval("square")(2)
