# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 16:05:41 2019

@author: yogesh.sharma1
"""

# taking run time arguments from user.
import sys
'''
print(len(sys.argv))  # 1 

# sys.argv  : sys is a module that have argv list. this list accepts
# all user arguments at rumtime.
# by default first argument will be script name.

print(sys.argv[0])
print(sys.argv[1])
# to pass value to argv list we will goto Run -- click Configuration per FIle
# select COmmand line options check box to write runtime arguments
# in the given box as space separated list
print(sys.argv[2])
print(sys.argv[3])
print(sys.argv[4])
'''
# arguments passed at runtime will be considered as string so '
# it has t be typecasted as per requirement 

c = int(sys.argv[1]) + int(sys.argv[2])
print(c)





