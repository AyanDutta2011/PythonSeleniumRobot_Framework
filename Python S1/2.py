# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 14:12:37 2019

@author: yogesh.sharma1
"""

# copy()

#assignment operator will not create a new object but will
#point to the same object. if we modify any of the object it will affect
# the other
'''
a = [12,4,2,45,3,46]
print("id(a) : ", id(a))
b = a 
print("id(b) : ", id(b))
b.remove(12)
print(a)
print(b)
'''

#

a = [12,4,2,45,3,46]
print("id(a) : ", id(a))
b = a.copy()
print("id(b) : ", id(b))
b.remove(12)
print(a)
print(b)

#=========
# Normal Set : unordered, have unique elements, mutable
# frozen set : immutable

# there is no index supprted by set

s = {2,3,8,9,4,6,8,5,6,4,7,8,6,2,4,2,4,5}
print(s)

p = set()
p.add(1)
p.add(1)
p.add(25)
p.add(33)
p.add(41)
p.add(12)
p.add(11)
p.add(2)
p.add(14)

print(p)
p.remove(14)
print(p)

# set is used when we want to find intersection, union of 2 data
# structurs

p1 = set((5,7,13,20,25))
p2 = set((5,7,11,35,50,89,13))

print("p1 : ", p1)
print("p2 : ", p2)

print("p1|p2 (union) : ", p1|p2)
print("p1&p2 (intersection) : ", p1&p2)
print("p1-p2 (anti-intersection) : ", p1-p2)
print("p2-p1 (anti-intersection) : ", p2-p1)
print("p1^p2 (anti-intersection) : ", p1^p2)

a1 = set('abcababrdrabrdrrrda')
a2 = set('abiiitttdffgwrrr')

print("a1 : ", a1)
print("a2 : ", a2)

print("a1|a2 (union) : ", a1|a2)
print("a1&a2 (intersection) : ", a1&a2)
print("a1-a2 (anti-intersection) : ", a1-a2)
print("a2-a1 (anti-intersection) : ", a2-a1)
print("a1^a2 (anti-intersection) : ", a1^a2)


l1 = ['apple','mango','banana']
l2 = ['pineapple','pears','orange','apple','banana']

ls1 = set(l1)
ls2 = set(l2)
print(ls1)
print(ls2)


fs1 = frozenset([5,7,13,20,25])
fs2 = frozenset([5,7,13,120,35,89,43])

# fs1.add(112)
# fs1.remove(7)

print("fs1 : ", fs1)
print("fs2 : ", fs2)

print("fs1|fs2 (union) : ", fs1|fs2)
print("fs1&fs2 (intersection) : ", fs1&fs2)
print("fs1-fs2 (anti-intersection) : ", fs1-fs2)
print("fs2-fs1 (anti-intersection) : ", fs2-fs1)
print("fs1^fs2 (anti-intersection) : ", fs1^fs2)

# ===========================
# Dictionary: collectio of key:value pairs
# key and value can be of any type
# key can't be non-hashable element like list, tuple etc
# key and values will be delimited by :
# dictionary elements will be delimited by comma


d = {1:"One",2:'Two',3:'Three'}

d2 = {'name':'Yogesh','marks':[123,325,340]}

# we can create a dictionary using tuple of 2 elements. where first
# element is a key and second element is a value

l =  [('Yogesh','Pune'),('Mike','NY'),('Kumar','Chennai')]
l1 = [(100,1000),(20,1000),(30,9000),(23,67000),(12,67000)]

print(type(l))
print(type(l1))

dl1 = dict(l)
dl2 = dict(l1)

print(type(dl1))
print(type(dl2))
print(dl1)
print(dl2)

d5 = dict(Abc=1,pqr=2,joy=3)
print(type(d5))
print(d5)

# you can pass 2 lists of equal elements and zip() them to convert into a dictionary

l11 = ['A','B','C','D']
l12 = [1,2,3,4,5,6]

d6= dict(zip(l11,l12))
print(type(d6))
print(d6)

d7= dict(zip(l12,l11))
print(type(d7))
print(d7)

print(d7[1])

print(d6['A'])

print(d6.keys())
print(dl1.keys())

print(d6.values())

print('A' in d6.keys())
print('A' in d6.values())
print(1 in d6.values())


print(d7)
d7.popitem()
print(d7)

d7.pop(1)
print(d7)

d7.update({1:'A'})
d7.update({100:'Z'})
d7.update({14:'G'})
print(d7)

# keys must be unique in dictionary so if we duplicate any key it
# will overwrite the existing one.

d7.update({1:'ABC'})
print(d7)

