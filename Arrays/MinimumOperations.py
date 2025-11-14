# Find Minimum Operations to Make All Elements Divisible by Three


nums = [1,2,3,4]
res=0
for i in nums:
    if (i+1)%3==0 or (i-1)%3==0:
        res+=1
print(res)
