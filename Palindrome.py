# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 10:06:33 2020

@author: user
"""
##remove punctuations and space in the string
def toChars(s):
    s = s.lower()
    ans = ''
    for c in s:
        if c in 'abcdefghijklmnopqrstuvwxyz':
            ans = ans + c
    return ans

### is a string a palindrome
def isPalindrome_recursion(s):
    if len(s) <= 1:
        return True
    else:
        return s[0] == s[-1] and isPalindrome_recursion(s[1:-1])
    
## is a strinng a palindrom using iteration
def isPalindrome_iteration(str):
    for i  in range(0, len(str)//2):
        if str[i] != str[len(str) - i-1]:
            return False        
    return True

### is string a palindrome by reversing a string
def isPalindrome_reversing(s):
    if s != reverse(s):
        return False
    
    return True
    ##reverse a string    
def reverse(s):
    return s[::-1]
 
#print(isPalindrome_recursion(toChars('able was I, ere I saw Elba')))  
print(isPalindrome_reversing(toChars('Able was I ere I saw elba')))
    
