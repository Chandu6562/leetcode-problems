# Merge Strings Alternately
'''You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1.
If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.'''

word1 = "ab"
word2 = "pqrs"

n=min(len(word1),len(word2))
res=""
for i in range(n):
    res+=word1[i] 
    res+=word2[i]
if len(word1)<len(word2):
    res+=word2[n:]
else:
    res+=word1[n:]
print(res)