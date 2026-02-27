# Sort Array By Parity
'''Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.

Return any array that satisfies this condition.'''

nums = [3,1,2,4]
l=0
for r in range(len(nums)):
    if nums[r]%2 ==0:
        nums[l],nums[r] = nums[r],nums[l]
        l+=1
print(nums)