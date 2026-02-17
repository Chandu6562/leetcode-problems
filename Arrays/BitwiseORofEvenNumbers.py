# Bitwise OR of Even Numbers in an Array
'''You are given an integer array nums.

Return the bitwise OR of all even numbers in the array.

If there are no even numbers in nums, return 0.'''

nums = [1,8,16]
res =0
even =0
for i in range(len(nums)):
    if nums[i]%2 == 0:
        even =nums[i]
    res= res |even
print(res)