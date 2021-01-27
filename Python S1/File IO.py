# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 14:44:38 2019

@author: yogesh.sharma1
"""

# File IO

# open(fileName,mode) is a function to open a file in Python

'''
there are following modes available in File IO

"r"  : Read : - default mode. open a file for reading. will give error if file does not existes
"a"  : Append  :  open file for appending. adding text to the end of file.
        create the fiel if doesn't exist
"w"  :  Write  :  open file for writing from beginning. will overwrite the file
        if already exist and create file if doesn't exist.
"x"  :  Create  : will create a new blank file if doesn't exist. will give error if file exist.

# we need to pass "t" if we want to rad data as text and "b" if we want to read data as binary
# when we seek over a file it has to be "b" mode        
'''

# create a file in present working directory
open("tmp.txt","x")

f = open("tmp.txt","a")
print(type(f))
f.write("this is line one")
f.write("\n")
f.write("this is 28th April line Two")
f.write("\n\n")
f.write("this is line one")
f.write("\n\n\n\n")
f.write("this is 123 line one")
f.write("\n")
f.write("today is 9 Dec 2019")
f.write("\n")
f.close()


f = open("tmp.txt","r")
print(f.read())   # will read whole file and print it on console

f = open("tmp.txt","r")
print(f.read(10))

f = open("tmp.txt","r")
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())

for x in f:
    print(x)
# by default python will read data from present directory
# Read data from a given Location using chdir() function in os module
   
import os

os.chdir("C:\Python_S1")
f = open("temp.txt","r")
for x in f:
    print(x)

# if you don't want to import os package then use absolute file path

f = open("C:/Python_S1/Day_6/tmp.txt","r")
for x in f:
    print(x)

f = open("C:\\Python_S1\\Day_6\\tmp.txt","r")
for x in f:
    print(x)

#===========================================
# count number of lines in a file
   
os.chdir("C:\Python_S1\Day_6")
n = 0

with open("tmp.txt",'r') as f:
    for line in f:
        n +=1
       
print("Number of Lines = ", n)

# count all the blank lines and non-blank lines

n = 0   # non-blank lines
m = 0   #blank lines

with open("tmp.txt",'r') as f:
    for line in f:
        if line.startswith("\n"):
            m +=1
        else:
            n +=1
print("Number of Non-Blank Lines = ", n)
print("Number of Blank Lines = ", m)

# write all the non-blank lines to a list

l = []

n = 0   # non-blank lines
m = 0   #blank lines

with open("tmp.txt",'r') as f:
    for line in f:
        if line.startswith("\n"):
            m +=1
        else:
            l.append(line)

print(l)



# read all blank lines and arite the lines to new File
n = 0   # non-blank lines
m = 0   #blank lines

with open("tmp.txt",'r') as f:
    for line in f:
        if line.startswith("\n"):
            m +=1
        else:
            f1 = open("newFile.txt","a")
            f1.write(line)
           

# count number of times a word occured in a file
#get all the words and keep them in a list
           
words = []

with open("tmp.txt","r") as f:
    for line in f:
        l1 = line.split(" ")
        words.extend(l1)

print(words)

temp = 0
word = input("Which word you want to search")
for i in words:
    if i==word:
        temp  +=1

print("{} occured {} times".format(word,temp))

# read all the data from one file and write it to another file

n = input("Enter input file name")

with open(n,"r") as f:
    with open("result.txt",'w') as f1:
        for line in f:
            f1.write(line)

# read all the line that starts with a from one file and write it to another file

n = input("Enter input file name")

with open(n,"r") as f:
    with open("result.txt",'w') as f1:
        for line in f:
            if line.startswith("a"):  
                f1.write(line)
                f1.close()
    f.close()


# count how many times a word occured without using explicit list

word = input("Which word you want to count")
ct = 0
   
with open("tmp.txt",'r') as f:
    for line in f:
        words = line.split()
        for x in words:
            if x==word:
                ct +=1
               
print("{} occured {} times".format(word,ct))

# count how many times a letter occured in a file

ltr = input("Which letter you want to count")
ct = 0
   
with open("tmp.txt",'r') as f:
    for line in f:
        words = line.split()
        for x in words:
            for letter in x:
                if letter==ltr:
                   ct +=1
               
print("Letter '{}' occured {} times".format(ltr,ct))

#======================
# seek(to,where)

import os

# SEEK_CUR  :
# SEEK_SET :
# SEEK_END

# tell() : get the current pointer/offset location

with open("tmp.txt",'rb') as f:
    print(f.tell())  # what is current pointer location
    print(f.readline())  # I accessed FIrst line.    
    print(f.tell())  # what is current pointer location after accessing first line

    f.seek(-10, os.SEEK_CUR)  # move 10 chars back from current location
    print(f.tell())  # what is current pointer location
    print(f.readline())  # I accessed FIrst line.    
    print(f.tell())

    f.seek(0, os.SEEK_SET)  # move back to offset 0 location
    print(f.tell())  # what is current pointer location
    print(f.readline())  # Fist line.    
    print(f.tell())

    f.seek(-10, os.SEEK_END)  # move to 10chars before end of the file
    print(f.tell())  # what is current pointer location
    print(f.readline())  # I accessed FIrst line.    
    print(f.tell())


    