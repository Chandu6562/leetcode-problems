# Count Substrings That Satisfy K-Constraint I

'''You are given a binary string s and an integer k.

A binary string satisfies the k-constraint if either of the following conditions holds:

The number of 0's in the string is at most k.
The number of 1's in the string is at most k.
Return an integer denoting the number of substrings of s that satisfy the k-constraint.'''

s = "10101"
k = 1
l=0
temp=0
zero=0
one=0
count=0
for r in range(len(s)):
    if s[r] == '0':
        zero+=1
    else:
        one+=1
        
    while zero>k and one>k:
        if s[l]=='0':
            zero-=1
        else:
            one-=1
        l+=1
    count+=r-l+1
print(count)