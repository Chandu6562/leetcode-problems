# Count Number of Pairs With Absolute Difference K

'''Given an integer array nums and an integer k, return the number of pairs (i, j) where i < j such that |nums[i] - nums[j]| == k.'''

nums = [1,2,2,1]
k = 1
count=0
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if abs(nums[i]-nums[j])==k:
            count+=1
print(count)