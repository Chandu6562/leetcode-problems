# Third Maximum Number
'''Given an integer array nums, return the third distinct maximum number in this array.
If the third maximum does not exist, return the maximum number.'''

def third_m():
    nums.sort()
    temp=0
    third_max=float('inf')
    for i in range(len(nums)-1,-1,-1):
        if nums[i]<third_max:
            third_max=nums[i]
            temp+=1
        if temp==3:
            return nums[i]
    return max(nums)
nums = [1,2]
print(third_m())