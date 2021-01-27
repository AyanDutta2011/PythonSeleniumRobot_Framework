# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 14:18:15 2019

@author: yogesh.sharma1
"""

# Class and Objects 
# class is a collection of properties(variables) and behaviours (methods)
# class is a blueprint or a template to define a classifications/ category'
# class is a passive entitiy for which there is no memory allocations

# Object : is an instance of a class. it contains all the class 
# properties and behaviours.

# Human, ANimals, Cars, etc are some examples of classes

'''
Syntax:
    
class ClassName:
    variables
    
    constuctor
    
    method1()
    
    
    method2()
    

object = ClassName()
'''
'''
class Human:
    age = 12
    weight = 45
    height = 4.0
    
    def run(self):
        print("Running")

    def walk(s,name):
        print(name ," is Walking")
        print(name, " is ", s.age, " years old")
    
    def props(z):
        print("Age is ",z.age)
        print("Weight is ",z.weight)
        print("Height is ",z.height)

# self, s, z here in class method are object of class itself
# self type object is a referance to the class properties. it is used to 
# access class' properties within class
        
# it is not necessary to call it like self it can be any other name.
# but it must be a valid identifier.

# self type object must be the first argument while creating function.
# There must be atleast one argument. if we are passing  more than one 
# argumetns by default first argument will be considered as object of class itself

joy = Human()
mike = Human()
adi = Human()

# Age:
print("Age")
print(joy.age)         
print(mike.age)
print(adi.age)

print("Weight")
print(joy.weight)         
print(mike.weight)
print(adi.weight)

print("Height")
print(joy.height)         
print(mike.height)
print(adi.height)

joy.age  = 23
joy.weight = 67
joy.height = 5.4

joy.props()

joy.run()
joy.walk("Joy")
'''

# COnstructor
# there is a private memer in class named __init__(). this is constructor in 
# python. constructor in python does not have same name as class name
'''
class Human:
    a = 20
    b = 30
    
    def abc(self,a,b):
        print(" self.a", self.a)
        print(" self.b", self.b)
        print(" a", a)
        print(" b", b)

    def Human(self):
        print("This is not a constructor")
        
    def xyz(self,a,b):
        self.a = a
        self.b = b
        print(" self.a", self.a)
        print(" self.b", self.b)
        print(" a", a)
        print(" b", b)

h1 = Human()
h1.Human()
h1.abc(100,200)
print("\n_+_+_+_+_+_+_+_+_+\n")
h1.xyz(1002,2002)
print("\n_+_+_+_+_+_+_+_+_+\n")
h1.abc(123,456)
'''
# in class we maintain local namespace, globel namespace and builtin namespace
'''
class Human:
      
    def __init__(self,x=0,y=0):
        print("Constructor Called")
        self.a = x
        self.b = y
        
    def abc(self,a,b):
        print(" self.a", self.a)
        print(" self.b", self.b)
        print(" a", a)
        print(" b", b)

    def Human(self):
        print("This is not a constructor")
        
    def xyz(self,a,b):
        self.a = a
        self.b = b
        print(" self.a", self.a)
        print(" self.b", self.b)
        print(" a", a)
        print(" b", b)


h1 = Human()
# 

x = 19  # declaring and initilizing the varible.
#we have some variables or properties in a class. if we want to initilize
# these properties we will us constructor


h2 = Human(12,12)

h2.abc(1,1)
'''
'''
class Abc:
    
    def __init__(self):
        pass

# we dont use {} to define funtion boundaries. so pass keword is used to 
# create function, class or any other block without any body.
        

class Human:
      
    def __init__(self,*x):
        print("Constructor Called")
        self.a = x
        
    def meth1(self):
        print(type(self.a))
        print(self.a)

# *x : is  a variable length argument. means it acan have 0,1,2....n number of 
# elements. which datastructure can hold more than 1 records/elements
        

a1 = Human()
a2 = Human(12)
a3 = Human(12,13,14)
a4 = Human(12,13,14,"Yogesh", "Sharma")

a1.meth1()
a2.meth1()
a3.meth1()
a4.meth1()
'''

# Static variable and methods
# class or static variables are shared by all objects of the class
# Instance or non-static members are different for each object
# by default all the memebrs defined at class level are static.
'''
class StaticEx:
    st = 15
    
    
print(StaticEx.st)

s1 = StaticEx()
s2 = StaticEx()
s3 = StaticEx()

print(s1.st)
print(s2.st)
print(s3.st)

s1.st = 10
s2.st=17

print(s1.st)
print(s2.st)
print(s3.st)
print(StaticEx.st)

StaticEx.st = 100
print(s1.st)
print(s2.st)
print(s3.st)
print(StaticEx.st)
'''
'''
class Student:
    
    branch = "Programming"
    
    def __init__(self,fname,rollno):
        self.fname = fname
        self.rollno=rollno
        
    
# branch is class memeber which is static
# fname and rollno are instance members which are non-static
        
joy = Student("Joy",123)
mike = Student("Mike",124)

print(joy.branch)
print(joy.fname)
print(joy.rollno)

print(mike.branch)
print(mike.fname)
print(mike.rollno)

# if class members are modified it will affect all objects.
Student.branch = "CSE"
print(joy.branch)
print(joy.fname)
print(joy.rollno)

print(mike.branch)
print(mike.fname)
print(mike.rollno)
'''

# Python static methods.
# static method doesn't take implicit first argument. self object
# is not required
# static method is bound ti the class and not to the object.
# static method can't access or modify class state
# static method can be called directly eith class name.
'''
class String:
    
    def fun1(self):
        print("normal method")

    @staticmethod
    def meth1(s):
        return s

    @staticmethod
    def uniqueWords(s):
        return set(s.split())

print(String.meth1("Radar"))
print(String.uniqueWords("this is a string. this is a string. this is a string."))
s1 = String()
s1.fun1()

String.fun1()
# non static or instance methods can not be called directly with class name
# self will not be considered as object of self class
'''
# Class Method:
# class method receives the class as implicit first argument, like instance
# method receives object of the same class
# class method is bound to the class.
# with class method we ca access state of the class using cls or any other 
# name to the class provided while you are creating the class method.
'''
from datetime import date 
class Person:
    
    def __init__(self,name,age):
        print("Const called")
        self.name = name
        self.age = age
        
    @classmethod
    def fromBirthYear(cls,name,year):
        return cls(name, date.today().year - year )
    
    @staticmethod
    def isAdult(age):
        return age > 18


yogesh = Person("yogesh",32)
joy = Person.fromBirthYear("joy",1999)

print(yogesh.age)
print(joy.age)
'''
'''
# 
def deco(func):
    def inner():
        print("_+_+_+_+_+_+_+_+")
        func()
        print("_+_+_+_+_+_+_+_+")
    return inner

def ob():
    print("Mphasis")

p1 = deco(ob)
p1()

@deco
def ob2():
    print("Mphasis")

ob2()
'''
# class to append, delete or display elements of a list
'''
class ListClass:
    n = []

    def add(self,a):
        self.n.append(a)
    
    def remove(s,b):
        s.n.remove(b)
    
    def display(s):
        return s.n

obj = ListClass()

obj.add(12)
print(obj.display())
'''

# use this object to take user input about add, delete of display data
# run it infinite time till user dont want to exit.


#========================
# Inheritance
# used to reuse properties of a class into another class
'''
class SubClass(SuperClass1, SuperClass2...):
    class 
    implementation

'''
'''
class One:
    v1 = 0
    v2 = 10
    
    def meth1(self):
        print("One::meth1() called")
        
    def meth2(self, a=10, b=20):
        print("One::meth2 called")
        print("addition is {}".format(a+b))

# class Two has meth3() we want to reuse meth1() and meth2() from class
# One here


class Two(One):
    def meth3(s):
        print("Two::meth3() called")

o1 = One()
t1 = Two()

o1.meth1()
o1.meth2(120,345)

t1.meth1()
t1.meth2(123)
t1.meth3()
'''

# Inheritance with Constructor
'''
class One:
    v1 = 0
    v2 = 10

    def __init__(self):
        print("One::constructor")
        
    def meth1(self):
        print("One::meth1() called")
        
    def meth2(self, a=10, b=20):
        print("One::meth2 called")
        print("addition is {}".format(a+b))

class Two(One):

    def __init__(self):
        super()
        print("Two::constructor")
        
    def meth3(s):
        print("Two::meth3() called")

#o1 = One()
t1 = Two()

t1.meth1()
t1.meth2(123)
t1.meth3()

# we dont call constructors explicitly.  so are not inherited.
'''

# overriding
# when both super and sub class have method with same name.
# method of subclass will be preferred
'''
class One:
   
    a = 12
        
    def meth1(self):
        print("One::meth1() called")
        
    def meth2(self, a=10, b=20):
        print("One::meth2 called")
        print("addition is {}".format(a+b))

class Two(One):
    
    def meth1(self):
        print("Two::meth1() called")

    def meth3(s):
        print("Two::meth3() called")

t = Two()

t.a = 1000
print(t.a)

t.meth1()
t.meth2()
t.meth3()
'''
# multilevel inheritacne
'''
class One:
   
    a = 12
        
    def meth1(self):
        print("One::meth1() called")
        
    def meth2(self, a=10, b=20):
        print("One::meth2 called")
        print("addition is {}".format(a+b))

class Two(One):
    
    def meth3(s):
        print("Two::meth3() called")
        

class Three(Two):
    
    def meth4(s):
        print("Three::meth4() called")

t = Three()

t.a = 1000
print(t.a)

t.meth1()
t.meth2()
t.meth3()
t.meth4()
'''

# multilevel inheritance

class One:
   
    a = 12
        
    def meth1(self):
        print("One::meth1() called")
        
    def meth2(self, a=10, b=20):
        print("One::meth2 called")
        print("addition is {}".format(a+b))

class Two:
    
    def meth1(self):
        print("Two::meth1() called")
        
    def meth3(s):
        print("Two::meth3() called")
        

class Three(Two,One):  #(One,Two)
    
    def meth4(s):
        print("Three::meth4() called")

t = Three()

t.a = 1000
print(t.a)

t.meth1()
t.meth2()
t.meth3()
t.meth4()


x = t
x.meth1()


