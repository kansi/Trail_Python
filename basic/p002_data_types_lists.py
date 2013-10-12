#!/usr/bin/env python

# This code doc explains the List datatype in python

# A list can be composed of different datatypes
# like string, int, float.
# Following are a few different ways in which we inititalize a list
list1 = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
list2 = [66.25, 333, 333, 13, 1, 1234.5]
zeros = [0]*5                               # output will be  [0 ,0, 0, 0, 0]
listoflists= [[1, 2, 3]] * 3                # [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
listoflists[0][2]=4                         # [[1, 2, 4], [1, 2, 4], [1, 2, 4]]

# to get the length of list
lenght = len(list1)

# we can add new items to the list in the following ways

## Below we can see two different ways of adding an element to
## a list, the difference being in the performence
## append is twice as fast. In general case append will add one item
## to the list, while += will copy all elements of right-hand-side
## list into the left-hand-side list.
## append adds one entry to the list, while += adds as many as there are in the other list
list1.append("new item")
list1 += ["new item"]

list2.insert(2, -1)             # [66.25, 333, -1, 333, 13, 1, 1234.5]
list2.remove(1234.5)            # [66.25, 333, -1, 333, 13, 1]
list2.pop()                     # [66.25, 333, -1, 333, 13]
list2.pop(0)                    # [333, -1, 333, 13]
del list1[4]                    # [ 'abcd', 786 , 2.23, 'john' ]

# we can also exetend a list by merging to lists
a = [1,2,3]
b = [4,5,6]
c = [1,2]
a.extend(b)             # [1, 2, 3, 4, 5, 6]
a + b                   # [1, 2, 3, 4, 5, 6]
c.append(b)             # [1, 2, [4, 5, 6]]

# To find the location of an element in a list
list1.index(786)            # 1

# To sort the elements of a list
list2.sort()
sorted(list2)

# We can reverse the elements of a list
list1.reverse()

# we can count the number of instances a element has occured in
# the list in the following way
list2.count(333)        # 2

# We can extract all the elements of a list using the following
# but note that the variables on the left side should be equal to
# the number of elements in the list
a = ['spam', 'eggs', 100, 1234]
[a1, a2, a3, a4] = a

# we can access the elements of a list in the following
# different ways
whole = list1                   # access complete list
first_element =list1[0]         # access first element of the list
one_to_three = list1[1:3]       # access elements starting from 2nd till 3rd
two_to_end = list1[2:]          # access elements starting from 3rd element

# It is also possible to get non-continuous parts of an array. If one wanted to
# get every n-th occurrence of a list, one would use the :: operator. The syntax
# is a:b:n where a and b are the start and end of the slice to be operated upon.
num_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list[1:7:2]                                 # [1, 3, 5]

# we can get the maximum, minimum element and the sum of the list
# with the help of the following functions
max_element = max(num_list)
min_element = min(num_list)
sum_list = sum(num_list)
