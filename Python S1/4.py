# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 14:03:16 2019

@author: yogesh.sharma1
"""

# nested loop 
# to accept 3 distinct numbers and print all possible ombinations 
#123
# 132
#213
# 231
#312
#321
'''
d = []

for i in range(0,3):
    d.append(int(input("Enter a number")))

print(d)

for i in range(0,3):
    for j in range(0,3):
        for k in range(0,3):
            if(i!=j & j!=k & k!=i):
                print(d[i],d[j],d[k])

'''

# create a list of n elements, where n is number of elements user
# wants. divide this list into list of even numbers and odd numbers
'''
n = int(input("Enter number of elements you want in list"))
d = []

for i in range(0,n):
    d.append(int(input("Enter a number")))

print("Original List : ", d)

even = []
odd = []

for item in d:
    if item%2==0:
        even.append(item)
    else:
        odd.append(item)

print("Even List : ", list(set(even)))
print("Odd List : ", list(set(odd)))
'''

# create a list of 5 elements and swap first and last elements.

'''
d = []

for i in range(0,5):
    d.append(int(input("Enter a number")))

# we can reverse the list
#print(d[::-1])

#print(list(reversed(d)))

t = d[0]
d[0]=d[4]
d[4]=t

print(d)
'''
'''
l1 = [12,8,9,4,6,2,7,8,5,6,8,3,9,7,8,9,2,1,4]
#[12,18,9,14,6,12,7,18,5,16,8,13,9,17,8,19,2,11,4]
# add 10 to value at odd index of this list l1
l3 = []

for a in range(0,len(l1)):
    #print(a)
    if a%2==1:
        b = l1[a] + 10
        l3.append(b)
    else:
        l3.append(l1[a])

print("Original List : ", l1)
print("new List : ", l3)
'''
# for a given string create a key,value pair of 
# firstletterofword,listOfWordsStartsWithLetter


s1 = "this,is,a,string"
l1 = s1.split(",")
print(type(l1))
print(l1)

# split the string to get words from it. 
# spit() method splits string based on space by default.
#

s = """this string contains some words these words are starting
with different letters. some letters are this that there alone apart
stop start with where who whom"""

# (t, [this,these,this,that,there])
# (a,[a,are,alone,apart]
# (w
# (s
# (l


l = s.split()
#print(l)

d= {}

for word in l:
    #print(word[0])
    if(word[0] not in d.keys()):
        d[word[0]] = []
        d[word[0]].append(word)
    else:
       if(word not in d[word[0]]): 
          d[word[0]].append(word)

print(d)

# from string s remove following words is, am, are, was were, a, the

st = set(["is", 'am', 'are', 'who', 'with', 'a', "that",'this','the'])
print(st)

lst = set(s.split())

print(lst - st)




