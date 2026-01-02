# Maximum Product of Two Elements in an Array
'''Given the array of integers nums, you will choose two different indices i and j of that array. 
Return the maximum value of (nums[i]-1)*(nums[j]-1).'''

nums = [3,4,5,2]
res=0
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        a=nums[i]-1
        b=nums[j]-1
        res=max(a*b,res)
print(res)