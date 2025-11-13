# Reverse Degree of a String

a='zaza'
res=0
for i in range(len(a)):
    res+=(123-ord(a[i]))*(i+1)
print(res)