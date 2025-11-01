# Move Zeros
'''Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.'''

# Brute Force
# nums = [0,0,1]
# for i in range(len(nums)-1,-1,-1):
#     if nums[i] == 0:
#         nums.append(nums[i])
#         nums.pop(i)
# print(nums)

# Optimal Solution
nums=[0,0,1]
j = 0  
for i in range(len(nums)):
    if nums[i] != 0:
        nums[i], nums[j] = nums[j], nums[i]
        j += 1
print(nums)