# Unique Number of Occurrences
'''Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.'''

# arr = [1,2,2,1,1,3]
arr = [-3,0,1,-3,1,1,1,-3,10,0]
d={}
for i in arr:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
l=[]
for j in d.values():
    if j not in l:
        l.append(j)
print(len(d)==len(l))