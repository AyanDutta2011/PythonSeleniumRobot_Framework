#Array are similar to lists. But difference is Array need to have all values of same type.
#Array dont have fixed size. We can expand or reduce the size.

#import array as arr
#arr.array()

from array import *  #it will import all the functions of array
vals = array('i', [1,2,3,5,6,7])

print(vals)
print(vals.buffer_info()) #it will give address and size
print(vals.typecode) #it will give type

newarr = array(vals.typecode, (a for a in vals))

for e in newarr:
    print(e)

char = array ('u', ['a','e','i','o','u'])
print(char)
char.remove('e')
print(char)
char.append('@')
print(char)

i = 0
while i<len(char):
    print(char[i])
    i += 1
