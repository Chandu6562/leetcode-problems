# Single Number

nums = [2,2,1,2]
d={}
for i in nums:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
for j in d:
    if d[j]==1:
        print(j)