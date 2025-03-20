# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 04:36:13 2025

@author: jungh
"""

############ YOU TRY IT ###############
# This one is similar to remove_elem from lec10 except that remove_elem 
# returns a new list and this one mutates the parameter L (and returns None)
# def remove_all(L, e):
#     """ 
#     L is a list
#     Mutates L to remove all elements in L that are equal to e
#     Returns None.
#     """
#     # your code here
#     # make a copy
#     Lnew = L[:]
#     # clear the list
#     L.clear() # L becomes []
#     # add back elements that do not equal e
#     for i in Lnew:
#         if i != e:
#             L.append(i)

# Lin = [1,2,2,2]
# remove_all(Lin, 2)
# print(Lin)    # prints [1]

# Lin = [1,2,2,2]
# remove_all(Lin, 1)
# print(Lin)    # prints [2, 2, 2]

# Lin = [1,2,2,2]
# remove_all(Lin, 0)
# print(Lin)    # prints [1, 2, 2, 2]

#######################################

# # EXAMPLE: aliasing
# warm = ['red', 'yellow', 'orange']
# hot = warm
# hot.append('pink')
# print(hot)
# print(warm)

# # EXAMPLE: cloning
# cool = ['blue', 'green', 'grey']
# chill = cool[:]
# chill.append('black')
# print(chill)
# print(cool)

# # EXAMPLE: sorting with/without mutation
# warm = ['red', 'yellow', 'orange']
# sortedwarm = warm.sort()
# print(warm)
# print(sortedwarm)

# cool = ['grey', 'green', 'blue']
# sortedcool = sorted(cool)
# print(cool)
# print(sortedcool)

# # EXAMPLE: lists of lists of lists...
# warm = ['yellow', 'orange']
# hot = ['red']
# brightcolors = [warm]
# brightcolors.append(hot)
# print(brightcolors)
# hot.append('pink')
# print(hot)
# print(brightcolors)


############ YOU TRY IT AT HOME ###################
# Step through the code below without running it
# Write down what values each variable has
# Draw the memory diagram to help you keep track of aliases and clones

# cool = ['blue', 'green']
# warm = ['red', 'yellow', 'orange']
# print(cool)
# print(warm)

# colors1 = [cool]
# print(colors1)
# colors1.append(warm)
# print('colors1 = ', colors1)

# colors2 = [['blue', 'green'],
#           ['red', 'yellow', 'orange']]
# print('colors2 =', colors2)

# warm.remove('red') 
# print('colors1 = ', colors1)
# print('colors2 =', colors2)

# for e in colors1:
#     print('e =', e)

# for e in colors1:
#     if type(e) == list:
#         for e1 in e:
#             print(e1)
#     else:
#         print(e)

# flat = cool + warm
# print('flat =', flat)

# print(flat.sort())
# print('flat =', flat)

# new_flat = sorted(flat, reverse = True)
# print('flat =', flat)
# print('new_flat =', new_flat)

# cool[1] = 'black'
# print(cool)
# print(colors1)

###############################

## Finger Exercises Lecture 11

# Impöement the function that meets the specification beöow.:
def remove_and_sort(Lin, k):
     """ Lin is a list of ints
     k is an int >= 0
     Mutates Lin to remove the first k elements in Lin and
    then sorts the remaining elements in ascending order.
     If you run out of items to remove, Lin is mutated to an empty list.
     Does not return anything.
     """
     # Your code here
     if len(Lin) <= k:
         Lin.clear()
         return
     for i in range(k):
         del(Lin[0])
     Lin.sort()
     
# Examples:
L = [1,6,3]
k = 2
remove_and_sort(L, k)
print(L) # prints the list [3, 6]









