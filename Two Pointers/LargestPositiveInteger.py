# Largest Positive Integer That Exists With Its Negative

'''Given an integer array nums that does not contain any zeros, find the largest positive 
integer k such that -k also exists in the array.

Return the positive integer k. If there is no such integer, return -1'''

nums = [-9,-43,24,-23,-16,-30,-38,-30]
nums=set(nums)
nums = [i*(-1) if i<0 else i for i in nums ]
nums.sort()
r=len(nums)-1
l=len(nums)-2
while l>=0:
    if nums[r] == nums[l]:
        print(nums[r])
        break
    else:
        r-=1
        l-=1
else:
    print(-1)