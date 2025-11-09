# Find All Numbers Disappeared in an Array
'''Given an array nums of n integers where nums[i] is in the range [1, n], 
return an array of all the integers in the range [1, n] that do not appear in nums.'''

def findDisappearedNumbers(nums):
    for num in nums:
        index = abs(num) - 1
        if nums[index] > 0:
            nums[index] = -nums[index]
    
    res = []
    for i in range(len(nums)):
        if nums[i] > 0:
            res.append(i + 1)
    return res

print(findDisappearedNumbers([4,3,2,7,8,2,3,1])) 
