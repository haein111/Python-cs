# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 05:36:53 2025

@author: jungh
"""

################# YOU TRY IT #######################
# Write code to use bisection search to find the cube 
# root of positive cubes to within some epsilon

cube = 27
epsilon = 0.01
low = 0
high = cube

# your code here
guess = (high + low)/2
while abs((guess**3) - cube) >= epsilon:
    if guess**3 > cube:
        # guess to high
        high = guess
    else:
        low = guess
    guess = (high + low)/2
print(f'The answer is {str(guess)}')



#####################################################