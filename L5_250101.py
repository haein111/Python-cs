# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 14:06:03 2025

@author: jungh
"""

#############
## EXAMPLE
# protip: use Python Tutor to go step-by-step: http://pythontutor.com/
#############

x = 0.625
p = 0
while ((2**p)*x)%1 != 0:
    # print(f'{str((2**p)*x - int((2**p)*x))}')
    p += 1
    # print(p)
num = int(x*2**p)

result = ''
if num == 0:
    result = '0'
while num > 0:
    result = str(num%2) + result
    num = num//2

for i in range(p - len(result)):
    result = '0' + result
    
result = result[0:-p] + '.' + result[-p:]
print(result)

#################################################
######################## AT HOME ##########################
#################################################
# 1. If you are incrementing from 0 by 0.022, how many increments 
# can you do before you get a floating point error? 

# x = 0
# count = 20     # check different numbers here
# for i in range(count):
#     x += 0.022 # increment
#     print(x)      # check this value for floating point error


# 2. Automate the code from the previous problem. Suppose you are 
# just given an increment value. Write code that automatically
# determines how many times you can add increment to itself 
# until you start to get a floating point error.

# your code here

# n = 1
# inc = 0.022
# x = inc
# while n * inc == x:
#     print(x)
#     x += inc
#     n += 1

#################################################
#################################################
#################################################


# Finger Exercises Lecture 5

# my_str = "abcdefg"
# fin_str = ''
# for char in range(0, len(my_str), 2):
#     fin_str += my_str[char]
# print(fin_str)