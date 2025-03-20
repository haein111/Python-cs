# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 01:54:02 2025

@author: jungh
"""

############## YOU TRY IT ###################
# Write code that satisfies the following specification:
# def div_by(n, d):
#     """ n and d are ints > 0
#         Returns True if d divides n evenly and False otherwise 
#     """
#     # your code here
#     if n%d == 0:
#         return True
#     else:
#         return False

# # For example: 
# print(div_by(10,3))     # print False
# print(div_by(195,13))   # returns True

##############################################

############## YOU TRY IT ###################
# Write code that satisfies the following specification:
# Hint, use paper and pen for a strategy before coding!
# def is_palindrome(s):
#     """ s is a string
#     Returns True if s is a palindrome and False otherwise
#     """
#     # your code here
#     for i in range(len(s)//2):
#         if s[i] == s[len(s)-i-1]:
#             return True
#         else:
#             return False

# s = "carac"
# print(is_palindrome(s))
################################################


################################################
################ YOU TRY IT AT HOME #####################
################################################
# 1. Write code that satisfies the following specs:
# def keep_consonants(word):
#     """ word is a string of lowercase letters
#         Returns a string containing only the consonants 
#         of word in the order they appear
#     """
#     # your code here
#     vowel = "aeiou"
#     consonants = ""
#     for char in word:
#         if char not in vowel:
#             consonants = consonants + char
#     return consonants

        
# # For example
# print(keep_consonants("abcd"))  # prints bcd
# print(keep_consonants("aaa"))  # prints an empty string
# print(keep_consonants("babas"))  # prints bbs



# 2. Write code that satisfies the following specs:
def first_to_last_diff(s, c):
    """ s is a string, c is single character string
        Returns the difference between the index where c first
        occurs and the index where c last occurs. If c does not 
        occur in s, returns -1. 
    """
    # your code here
    # first = ""
    # last = ""
    if c not in s:
        return -1
    for i in range(len(s)):
        if c == s[i]:
            # first = i
            break
    for j in range(len(s)-1, -1, -1):
        if c == s[j]:
            # last = j
            break
    return print(j-i)

# For example
print(first_to_last_diff('aaaa', 'a'))  # prints 3
print(first_to_last_diff('abcabcabc', 'b'))  # prints 6
print(first_to_last_diff('xyz', 'b'))  # prints -1