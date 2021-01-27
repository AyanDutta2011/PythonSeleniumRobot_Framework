# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 16:18:24 2019

@author: yogesh.sharma1
"""

# function is a self contaied block of statements
'''
# definition 
def functionName(Optional Arguments):
    statemet - 1
    statemet - 1
    statemet - 1
    BLock: 
        statemet - 1
        statemet - 1

'''


'''
def fun1():
    print("One")
    print("Two")
    print("Three")
    print("Four")
    print("Five")

# Calling the function
fun1()
fun1()
fun1()
fun1()
fun1()
'''
'''
def print1(s):
    print("+_+_+_+_+_+_")
    print(s)
    print("+_+_+_+_+_+_")


print1("This is a string")
'''

# FUNCTION WITH ARGUMENTS
'''
def abc(x,y):
    c = x + y
    print("Addition is ", c)

abc(12,12)
abc("abc","xyz")
abc(12,12.67)
'''
# funtion with default arguments
# y in following function has a default value so if you are not passing 
# any value to y it will take 10 by default
'''
def abc(x,y=10):
    c = x + y
    print("Addition is ", c)

abc(12)
abc("abc","xyz")
abc(12.67)
'''
# we can pass any number of default arguments
'''
def abc(x,y,p,q=10,r=20):
    c = x + y + p + q + r
    print("Addition is ", c)

abc(12,12,13,r=29)
#abc("abc","xyz","Hello")
abc(12,12.67,123)
abc(q=100,p=12,x=12.67,y=123)
'''
# while passing default arguments to function in python, defined args
# must be after undefined args.
# following will not work
'''
def abc(x=10,y):
    c = x + y
    print("Addition is ", c)

abc(12)
abc("abc","xyz")
abc(12.67)
'''

# function can return an value

def abc(x,y=10):
    c = x + y
    return c

a = abc(12)
b = abc(90,65.0)
c = abc(12.67)

# we return a value to perform any aditional operation on the result
d = (a * 2)  + (b * 2) + c
print(d)

# recursive function 

def fact(n):
    if n in (0,1):
        return 1
    else:
        return fact(n-1) * n

print(fact(5))


# nested funciton

def fun5(a,b):
    def fun(x):
        return x * x
    return fun(a) + fun(b)

i = fun5(3,4)
print(i)   # ???

def add(a,b):
    print(a + b)

def multi(a,b):
    print(a * b)

def sub(a,b):
    print(a - b)

def div(a,b):
    print(a / b)


# as user to 
    
n = int(input("""Enter you choice 
              0. add
              1. multi
              2. sub
              3. div
              """))

a = int(input("Enter first number"))
b = int(input("Enter second number"))
'''
if n ==0:
    add(a,b)
elif n ==1:
    multi(a,b)
elif n ==2:
    sub(a,b)
elif n ==3:
    div(a,b)
else:
    print("Invalid input")
'''

op = {0:add,
      1:multi,
      2:sub,
      3:div}

op[n](a,b)

============
# variable length arguments

def adder(a,b,c):
    print(a+b+c)
    
adder(1,2,2)
#adder(12,19,28,23)
#adder(1,2)    
# this function adder can take exactly 3 args. it will not take anything less than that

# we have a functionality in python know as varargs. using this we 
# can pass any nunber of args to a function.
# to define variable length argument we use * folloed by a valid identifier
    
    
def adder1(*num):
    t = 0
    for i in num:
        t = t + i
    print(t)

adder1(18,9,3,4,6,25)
adder1(18,9,3)
adder1(18,9,3,4,6,25,3,4,932,4,6,7,8)

# when you want to pass variable length arguments with key,value
# keyword arguments. kwargs
# kwargs can be defined using ** followed by valid identifier

def in1(**data):
    for k,v in data.items():
        print("{} is {}".format(k,v))


print("\n_+_+_+_+_\n")
in1(FN="Joy",LN='K',age=32,salary=200000,country='India')


d = {1:2,3:4,4:3}
print(1 in d.keys())

#==========

def fun12():
    print("fun12() called")
    
def newFun(f):
    print("newFun()")
    f()
    
newFun(fun12)



