# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 15:42:05 2025

@author: jungh
"""

############### YOU TRY IT #######################
# Write a function that meets the specification:
# def make_ordered_list(n):
#     """ n is a positive int
#     Returns a list containing all ints in order 
#     from 0 to n (inclusive)
#     """
#     # your code here
#     result = []
#     for i in range(n+1):
#         result.append(i)
#     return result
    
# print(make_ordered_list(6))  # prints [0, 1, 2, 3, 4, 5, 6]

#####################################################

############ YOU TRY IT ###############
# def remove_elem(L, e):
#     """ 
#     L is a list
#     Returns a new list with elements in the same order as L
#     but without any elements equal to e. 
#     """
#     # your code here
#     mylist = []
#     for i in L:
#         # i is 1 then 2 then 2 then 2
#         if i != e:
#             mylist.append(i)
#     return mylist
  
# L = [1,2,2,2]
# print(remove_elem(L, 2))    # prints [1]
# L = [1,2,2,2]
# print(remove_elem(L, 1))    # prints [2,2,2]
# L = [1,2,2,2]
# print(remove_elem(L, 0))    # prints [1,2,2,2]


#######################################



############## YOU TRY IT #################
# Write a function that meets this specification
# def sort_words(sen):
#     """ sen is a string representing a sentence 
#     Returns a list containing all the words in sen but
#     sorted in alphabetical order. """
#     # your code here
#     words = sen.split(' ')
#     return len(words)

# s = "look at this photograph"
# print(sort_words(s))    # prints ['at', 'look', 'photograph', 'this']

# s = "now this is a story all about how my life got flipped turned upside down"
# print(sort_words(s))

##########################################


############## YOU TRY IT #################
# # Write a function that meets this specification
# def sort_words(sen):
#     """ sen is a string representing a sentence 
#     Returns a list containing all the words in sen but
#     sorted in alphabetical order. """
#     # your code here
#     words = sen.split(' ')
#     words.sort()
#     return words

# s = "look at this photograph"
# print(sort_words(s))    # prints ['at', 'look', 'photograph', 'this']

# s = "now this is a story all about how my life got flipped turned upside down"
# print(sort_words(s))

##########################################


#######################################
############ AT HOME ###############
#######################################
# # Question 1
# L1 = ['re']
# L2 = ['mi']
# L3 = ['do']
# L4 = L1 + L2
# #L4 = ['re', 'mi']
# L3.extend(L4)
# #L3 = ['do', 're', 'mi']
# L3.sort()
# #L3 = ['do', 'mi', 're']
# del(L3[0])
# #L3 = ['mi', 're']
# L3.append(['fa', 'la'])
# #L3 = ['mi', 're', ['fa', 'la']] ## fa, la are list
# # What's the value of L3 here?

# Question 2
# L1 = ['bacon', 'eggs']
# L2 = ['toast', 'jam']
# brunch = L1
# L1.append('juice')
# brunch.extend(L2)
# # What's the value of brunch here? ## bruch equals L1

## Question 3. 
def apply_to_each(L, f):
    """ L is a list of numbers 
        f is a function that takes in a number and returns a number
    Mutate L such that you apply function f to every element in L """
    # your code here
    for i in range(len(L)):
        L[i] = f(L[i])
        
test = [1,-2,3]
apply_to_each(test, lambda x: x**2)
print(test)   # prints [1,4,9]

test = [-7, 8, 5, -8, -3]
apply_to_each(test, abs)
print(test)   # prints [7, 8, 5, 8, 3]







