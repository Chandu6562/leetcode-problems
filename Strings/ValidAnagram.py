s = "anagram"
t = "nagaram"
flat=True
if sorted(s) == sorted(t):
    flag=True
else:
    flag=False
print(flag)