# Sum of Elements With Frequency Divisible by K

'''You are given an integer array nums and an integer k.

Return an integer denoting the sum of all elements in nums whose frequency is divisible by k, or 0 if there are no such elements.

Note: An element is included in the sum exactly as many times as it appears in the array if its total frequency is divisible by k.'''

nums = [4,4,4,1,2,3]
k = 3
sum=0
d={}
for i in nums:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
for x,v in d.items():
    if v%k==0:
        sum+=x*v
print(sum)