#!/usr/bin/env python

# This module explains the usage of cpickle.
# Pickle is an important module whenever you need persistence between user sessions.
# The concept of pickling is known variously as serialisation, marshalling, or flattening.
# cPickle is coded in C to provide better performance
#
# Source : http://www.ibm.com/developerworks/library/l-pypers/index.html

import cPickle as pickle

# Pickle library provides a a way to convert a python object (list, dict, etc.)
# into a character stream. The idea is that this character stream contains all
# the information necessary to reconstruct the object in another python script.

t1 = ('this is a string', 42, [1, 2, 3], None)

# dumps(object) returns a string containing an object in pickle format
p1 = pickle.dumps(t1)
print repr(p1)                              # "(S'this is a string'\nI42\n(lp1\nI1\naI2\naI3\naNtp2\n."

# optional argument that, if True, specifies that pickles will be created using a faster and smaller binary representation
p2 = pickle.dumps(t1, True)
print repr(p2)                              # "(U\x10this is a stringK*]q\x01(K\x01K\x02K\x03eNtq\x02."

# loads(string) returns the object contained in the pickle string
t2 = pickle.loads(p1)
print repr(t2)                              # ('this is a string', 42, [1, 2, 3], None)


# Below we see the uasge of dump() and load() functions. dump() function allows you to dump several
# objects to the same file, one after the other. Subsequent calls to load() will retrieve the objects in the same order.
a1 = 'apple'
b1 = {1: 'One', 2: 'Two', 3: 'Three'}
c1 = ['fee', 'fie', 'foe', 'fum']
f1 = open('temp.pkl', 'wb')
pickle.dump(a1, f1, True)
pickle.dump(b1, f1, True)
pickle.dump(c1, f1, True)
f1.close()

# load(file) returns the object contained in the pickle file
f2 = open('temp.pkl', 'rb')
a2 = pickle.load(f2)
print a2                    # 'apple'
b2 = pickle.load(f2)
print b2                    # {1: 'One', 2: 'Two', 3: 'Three'}
f2.close()


