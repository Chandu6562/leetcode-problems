# Check if All Characters Have Equal Number of Occurrences
'''Given a string s, return true if s is a good string, or false otherwise.

A string s is good if all the characters that appear in s have the same number of occurrences (i.e., the same frequency).'''

# s = "abacbc"
s = "aaabb"
d={}
for i in s:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
print(len(set(d.values()))==1)