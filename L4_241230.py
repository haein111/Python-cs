# even_num = 0
# for i in range(5):
#     # i is 0,1,2,3,4
#     if i%2 == 0:
#         even_num += 1
# print(even_num)



# s = 'abca'
# seen = ''

# for char in s:
#     if char not in seen:
#         seen = seen + char
# print(len(seen))
    

####################
## EXAMPLE:  square root with negative flag
#################### 
# guess = 0
# neg_flag = False
# x = int(input("Enter your positive integer: "))
# if x < 0:
#     neg_flag = True
# while guess**2 < x:
#     guess += 1
# if guess**2 == x:
#     print(f'square root of {x} is {guess}')
# else:
#     print(f'square root of {x} is not a perfect square')
#     if neg_flag:
#         print(f"Did you mean {-x}?")
        
        
        

################ YOU TRY IT ##################
# Hardcode a number as a secret number. Write a program that 
# checks through all the numbers between 1 to 10 and prints the 
# secret value. If it's not found, it doesn't print anything. 

# your code here
# secret = 4

# secret = 15
# found = False
# for i in range(1, 11):
#     if i == secret:
#         found = True
# if not found:
#     print('not found')
# else:
#     print('found')


################################################



###################
# EXAMPLE: word problems
################### 

# for Alyssa in range(11):
#     for Ben in range(11):
#         for Cindy in range(11):
#             two_less = (Ben == Alyssa - 2)
#             twice = (Cindy == Alyssa*2)
#             total = (Ben + Cindy + Alyssa == 10)
#             if two_less and twice and total:
#                 print(f"Alyssa sold {Alyssa}")
#                 print(f"Ben sold {Ben}")
#                 print(f"Cindy sold {Cindy}")
                

# for Alyssa in range(1001):
#     Ben = max(Alyssa - 20 , 0)
#     Cindy = Alyssa * 2
#     if Ben + Cindy + Alyssa == 1000:
#         print("Alyssa", str(Alyssa))
#         print("Ben", str(Ben))
#         print("Cindy", str(Cindy))



####################################################
##################### AT HOME ######################
######################################################
# Write code that counts how many unique common characters there are between 
# two strings. For example below, the common characters count is 8: 
# text1 = "may the fourth be with you"
# text2 = "revenge of the sixth"
# Hint, start to write your code with a smaller example, then test it on the above text.

# text1 = "may the fourth be with you"
# text2 = "revenge of the sixth"
# seen = ''
# for char in text1:
#     if char not in seen:
#        seen = seen + char
#        for char2 in text2:
#            if char2 not in seen:
#                seen = seen + char2
# print(seen)
# print(len(seen))

####################################################
##################### END AT HOME ######################
######################################################

# Finger Exercises Lecture 4
# Assume you are given a positive integer variaböe named N.
# Write a piece of Python code that finds the cube root of N.
# The code prints the cube root
# if N is a perfect cube or it prints error if N is not a perfect cube.
# Hint: use a loop that increments a counter -- you decide when the counter shouöd stop.

# N = int(input("Choose your integer number: "))
# guess = 0
# while guess**3 < N:
#     guess += 1
# if guess**3 == N:
#     print(f'Your number is {guess}')
# else:
#     print('Error')
    



