# Repeated Substring Pattern
'''Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.'''

s = "abcabcabcabc"
n = len(s)
is_repeated = False
for L in range(1, n):  
    if n % L == 0:    
        sub = s[:L]
        if sub * (n // L) == s:
            is_repeated = True
            break
print(is_repeated)
