# Minimum Operations to Exceed Threshold Value I
'''You are given a 0-indexed integer array nums, and an integer k.

In one operation, you can remove one occurrence of the smallest element of nums.

Return the minimum number of operations needed so that all elements of the array are greater than or equal to k.'''

nums = [2,11,10,1,3]
k = 10
operations=0
for i in nums:
    if i < k:
       operations+=1
print(operations)