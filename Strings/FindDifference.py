# Find the Difference

s = "abcd"
t = "abxcde"
for i in range(len(s)):
    if s[i] in t:
        t=t.replace(s[i],"")
print(t)