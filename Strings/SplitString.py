# Split a String in Balanced Strings
'''Balanced strings are those that have an equal quantity of 'L' and 'R' characters.

Given a balanced string s, split it into some number of substrings such that:

Each substring is balanced.
Return the maximum number of balanced strings you can obtain.'''

# s = "RLRRRLLRLL"
s = "RLRRLLRLRL"
R=0
L=0
count=0
for i in range(len(s)):
    if s[i]=='R':
        R+=1
    else:
        L+=1
    if R==L:
        count+=1
        R,L=0,0
print(count)