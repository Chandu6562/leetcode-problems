# Strictly Palindromic Number

'''An integer n is strictly palindromic if, for every base b between 2 and n - 2 (inclusive), 
the string representation of the integer n in base b is palindromic.

Given an integer n, return true if n is strictly palindromic and false otherwise.

A string is palindromic if it reads the same forward and backward.'''

def Palindrome(n):
    for i in range(2,n-1):
        x=n
        binary = []
        while x > 0:
            remainder = x % i
            binary.append(remainder) 
            x = x // i
        if binary != binary[::-1]:
            return False
    return True
n=9
print(Palindrome(n))