# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 10:06:33 2020

@author: user
"""

## fibonacci using recursive algorithmn
###How many female rabbits are there at the end of one year?
## find the full description of the problem in the README.md file
def fibo_recursive(n):
    "fibonacci series using recursion"
    if n == 0 or n == 1:
        return n
    else:
        return fibo_recursive(n-1) + fibo_recursive(n-2)

###fibonacci using an iterative algorithm
val=int(input("Input the term "))
def fibo_iterative(val):
    first_num, second_num = 1, 1
    for i in range(n + 1):
        first_num, second_num = second_num, first_num+second_num
    return second_num
print(fibo_recursive(val))
