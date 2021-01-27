# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 16:10:12 2019

@author: yogesh.sharma1
"""

# Decision Making and Looping

'''
if condition:
    statement - 1
    statement - 2
    statement - 3
elif condition:
    statement - 1
    statement - 2
else:
    statement - 1
    statement - 2

'''
'''
a = int(input("Enter a Number"))

if a>0:
    print("Number is Positive")
elif a<0:
    print("Number is Negative")
else:
    print("Number is Zero")
'''

'''
a = int(input("Enter a Number"))
if a==0:
    print("Number is Zero")
elif a<0:
    print("Number is Negative")
else:
    print("Number is Positive")
'''

'''
a = int(input("Enter a Number"))
if a==0:
    print("Number is Zero")
else:
   if a<0:
      print("Number is Negative")
   else:
      print("Number is Positive")
'''

# we can write any number of conditions
'''
a = int(input("Enter a Number"))
if a==1:
    print("One")
elif a==2:
    print("Two")
elif a==3:
    print("Three")
elif a==4:
    print("Four")    
else:
    print("Invalid")
'''

# find grade of a student based on score
'''
x = input("Enter a Number")
if x.isnumeric()==True:
    x = int(x)
else:
    print("Not a valid input")

if x>100 or x<0:
    print("Not a valid score")
elif x>=90 and x<=100:
    print("A+")
else:
    if x>=80 and x<90:
        print("A")
    else :
        if x>=70 and x<80:
            print("B+")
        else:
            if x>=60 and x<70:
                print("B")
            else:
                print("C")

'''
'''
x = input("Enter a Number")
if x.isnumeric()==True:
    x = int(x)
else:
    print("Not a valid input")

if x>100 or x<0:
    print("Not a valid score")
elif x>=90 and x<=100:
    print("A+")
elif x>=80 and x<90:
    print("A")
elif x>=70 and x<80:
    print("B+")
elif x>=60 and x<70:
    print("B")
else:
    print("C")
'''
# =========================
# when we want to iterate over a set of statements, block multiple
# times
# each loop has 3 parts initilization, condition and inc/dec

# run a loop 10 times to pritn hello
'''
d =1   # initilization

while d<=10:  # condition
    print("Hello ",d)
    d += 1  # inc
'''

'''
d =10   # initilization

while d>=1:
    print("Hello ",d)
    d -= 1  # dec
'''

# ask user to enter a number and check if number is even or odd. do it 5 times
'''
c = int(input("How many times you want to check"))

i =1

while i<=c:
    x = input("Enter a number")
    if x.isnumeric()==True:
      x = int(x)
      if x % 2==0:
          print("Even")
      else:
          print("Odd")
    else:
     print("Not a valid input")
    i +=1

'''
'''
while True:
    x = input("Enter a numberto check or an alphabat to exit")
    if x.isnumeric()==True:
      x = int(x)
      if x % 2==0:
          print("Even")
      else:
          print("Odd")
    else:
     print("Exit")
     break;
'''
'''
while True:
    x = input("Enter a number")
    if x.isnumeric()==True:
      x = int(x)
      if x % 2==0:
          print("Even")
      else:
          print("Odd")
    else:
     print("Not a valid input")
     continue

    c = input("Enter Exit to quit")
    if c == 'Exit':
        print("Exiting")
        break
    else:
        continue
'''
# take a number from user and print all the even numbers from 0
# till that number.
# Input : 15
# Output : 2,4,6,8,10,12,14

# FIbonacci series

n = int(input("Enter a number"))

n1 = 0
n2 = 1

c = 0

while c < n:
    print(n1)
    x = n1 + n2
    n1 = n2
    n2 = x
    c += 1

# for() loop in python is not an alternate to while loop.
# for loop in python is used to travers over a sequence like list, string, tuple, set, dictionary

'''
for item in sequence:
    operation on item
'''

# to add 10 to each elemetn of a list

l1 = [1, 20, 4, 7, 3, 2, 6, 8, 5, 7, 4, 5, 7, 8, 41, 2]

for item in l1:
    print(item + 10)

s = "This iS a STRING where SOME lettERS are CapiTal"

# find all the capital letters from s

for item in s:
    if item.isupper():
        print(item)

l2 = [1.3, 8, 9, 4, 'aaa', 'bbb', 'mphasis', 6, 2, 7, 8.5, 42, 5, 'joy', 'ful', 445]

# how many numeric values are there in list l2

print(type(l2[0]))

t = 0

for item in l2:
    if str(item).isalpha():
        continue
    else:
        t += 1

print("There are {} numeric values".format(t))

# create a list of numbers and count how many numbers are greter than 20 in the list

# # create a list of numbers and add 100 to all the numbers greter than 20 in the list

# find cumulative sum of first n natural numbers

# 5  15
'''
n = int(input("Enter a number"))

t = 0

while n >= 0:
    t = t + n
    print(t)
    n -=1
'''
# print(t)

# find cumulative sum and put it in a list
n = int(input("Enter a number"))

temp = []
t = 0
while n > 0:
    t = t + n
    temp.append(t)
    n -= 1
print(temp)

# to find number of occurance of each digit in a list

l3 = [1, 1, 1, 1, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 3, 3, 2, 2, 2, 4, 4, 4, 4, 4, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3,
      3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# print(l3)

# remove the duplicate elements, take unique elements

ss = set(l3)
print(ss)
l = []
for item in ss:
    if item in l3:
        # print("{} occured {} times".format(item,l3.count(item)))
        l.append(l3.count(item))

l2 = list(ss)
print(l)
print(l2)

di = dict(zip(l2, l))

print(di)


