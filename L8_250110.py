# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 14:54:18 2025

@author: jungh
"""

############ YOU TRY IT ####################
# Fix this buggy code so it works according to the specification:
# def is_triangular(n):
#     """ n is an int > 0 
#         Returns True if n is triangular, i.e. equals a continued
#         summation of natural numbers (1+2+3+...+k) 
#     """
#     total = 0
#     for i in range(n+1):
#         total += i
#         # print(i)
#         # print(f"total: {total}")
#         if total == n:
#             return True
#     return False
    

# # start by runing it on simple test cases
# print(is_triangular(4))  # print False
# print(is_triangular(6))  # print True
# print(is_triangular(1))  # print True

##############################################
# def bisection_root(x):
#     epsilon = 0.01
#     low = 0
#     high = x
#     ans = (low + high)/2
#     while abs(ans**2 - x) >= epsilon:
#         if ans**2 < x:
#             low = ans
#         else:
#             high = ans
#         ans = (low + high)/2
#     return ans


###################### YOU TRY IT ######################
# def count_nums_with_sqrt_close_to(n, epsilon):
#     """ n is an int > 2
#         epsilon is a positive number < 1
#     Returns how many integers have a square root within epsilon of n """
#     # your code here
#     count = 0
#     for i in range(n**3):
#         sqrt = bisection_root(i)
#         if abs(n-sqrt) < epsilon:
#             #know that eps guess within eps
#             print(n, sqrt)
#             count += 1
#     return count

# print(count_nums_with_sqrt_close_to(10, 0.1))

#############################################################


def apply(criteria,n):
    """
    * criteria is a func that takes in a number and returns a bool
    * n is an int
    Returns how many ints from 0 to n (inclusive) match
    the criteria (i.e. return True when run with criteria)
    """
    # your code here
    count = 0
    for i in range(n+1):
        if criteria(i): # is a bool
            count += 1
    return count

def is_even(x):
    return x%2==0

def is_five(x):
    return x==5
    
how_many = apply(is_even,10)
how_many2 = apply(is_five,10)
print(how_many)
print(how_many2)


