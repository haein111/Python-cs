# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 12:34:58 2025

@author: jungh
"""

############### YOU TRY IT #####################
# Write a function that meets these specifications:
# def char_counts(s):
#     """ s is a string of lowercase chars 
#     Returns a tuple where the first value is the 
#     number of vowels in s and the second value 
#     is the number of consonants in s 
#     """
#     # your code here
#     vowels = "aeiou"  ##    
#     (c, v) = (0,0)  ##
#     for char in s:  ##
#         # chars is 'a' then 'b' then 'c'
#         if char in vowels: # vowels count
#             v += 1
#         else:   # cos count
#             c += 1
#     return (v, c)

# print(char_counts("abcd"))  # prints (1,3)
# print(char_counts("zcght"))  # prints (0,5)

##################################################

def sum_and_prod(L):
    """ L is a list of numbers 
    Return a tuple where the first value is the 
    sum of all elements in L and the second value 
    is the product of all elements in L 
    """
    # your code here
    s, p = 0, 1  ## I can write in one line
    for i in L:
        s += i
        p *= i
    return (s,p)  ## Not List, it's Tuple.. why
 

print(sum_and_prod([4,6,2,5]))   # prints (17, 240)