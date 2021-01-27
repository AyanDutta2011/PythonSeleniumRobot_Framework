# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 15:08:45 2019

@author: yogesh.sharma1
"""
# Regular Expression.

'''
\   : to drop the special meaning of char following it.
[]  : represent a char class, [0-9], [aeiou], [0-9]+
^   : to match the begining
$   :  match the end
.   : match any char except newline
|   : provide OR condition
+   :  One or more occurane of a pattern  
*   : 0 or more occurance of a pattern


shordhand chars

to represent all the digits ;  \d   = [0-9]
to match all the non digits  : \D  
to match all the white space char  : \s    

to match all the non-white space char  : \S
to match alphanumeric char : \w  = [a-zA-Z]
to match non-alphanumeric char : \W  
'''
# in python we have module called re to work with regula rexpression

import re

# re package has many methods like
# compile()  :  compiles RE char class.
# to match all the char from a to e

p = re.compile('[a-e]')
s = "this is a class on Python"
p.findall(s)
print(type(p))

# to find all the digits in a string

s1 = "he was born on 1 2:30 Pm, 28 May 2019 1 Jan 2020 my family income is 200000000"

p1 = re.compile("[0-9]+")
p1.findall(s1)
#OR
p1 = re.compile("\d+")
p1.findall(s1)


s2 = "this is a 1231 string *(^&^%& tht contains numbers 12896741378 and special char (*% %^ $ &* also string"

p1 = re.compile("\d+")
p1.findall(s2)

p1 = re.compile("\w+")
p1.findall(s2)

p1 = re.compile("\W+")
p1.findall(s2)

p1 = re.compile("\s+")
p1.findall(s2)

p1 = re.compile("\S+")
p1.findall(s2)

p1 = re.compile("[a-zA-Z]+")
p1.findall(s2)


s3 = "12THis is 12&456 another 09digit is 1 23 41235 ava12ilable 12 5here"
# all the the number with length 4 having first 2 char as 12 and
# next 2 char can be anything

p3 = re.compile("12..")
p3.findall(s3)

# 12 followed by any char then a number.
p3 = re.compile("12.\d")
p3.findall(s3)

# [0-9][0-9][a-zA-Z][a-ZA-Z] : 2 digits followed by 2 alphabets
# 12[a-zA-Z][0-9]

p3 = re.compile("[0-9][0-9][a-zA-Z][a-zA-Z]")
p3.findall(s3)

s4 = "abababaaaaabbbbabababaaaabababbbababaa"

# occurance of ab
p3 = re.compile("ab+")
p3.findall(s4)

s5 = "hello@gmail.com, hi@aol.com, chao@china.com, word@yahoo.in"
# find the domain name from email addresses

r2 = re.findall(r'@\w+.\w+',s5)
print(r2)

#=========================
# re.sub()  substitute/replace a sring with given patterns

# re.sub(pattern, replacementString, SearcInString, count=0, flags=0)

s6  = """I booked uber cab Uber cab provided uber
service via Ola cab ola provides service Ola as uber"""

print(s6)
#s7  = re.sub("uber","ola",s6)
#print(s7)

# provide count=1 to replace only first occuracne
 
s7  = re.sub("uber","ola",s6,count=1)
print(s7)

# dont check case sensitivite

s7  = re.sub("uber","ola",s6,flags=re.IGNORECASE)
print(s7)

s8 = "this is a trand to stand and eat now a days"

#and -> &

s9 = re.sub("\sand\s"," & ",s8)
print(s9)

#============================
emails = ["12hello@gmail.com","hi@aol.com",
          "chao@china","word@yahoo.in"]

string = """12hello@gmail.com
hi@aol.com
chao@china
word@yahoo.in
"""


# [a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+
patt = re.compile("[a-zA-Z_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+")

matches = patt.finditer(string)

for match in matches:
    print(match.group(0))