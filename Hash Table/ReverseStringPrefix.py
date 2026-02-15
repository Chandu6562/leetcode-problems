# Reverse String Prefix
'''You are given a string s and an integer k.

Reverse the first k characters of s and return the resulting string.'''

s = "abcd"
k = 2
a=s[:k]
res = a[::-1]+s[k:]
print(res)