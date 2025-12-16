# Running Sum of 1d Array
'''Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.'''

nums = [1,2,3,4]
result=[]
sum=0
for i in range(len(nums)):
    sum+=nums[i]
    result.append(sum)
print(result)