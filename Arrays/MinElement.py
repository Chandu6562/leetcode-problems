# Minimum Element After Replacement With Digit Sum
'''You are given an integer array nums.

You replace each element in nums with the sum of its digits.

Return the minimum element in nums after all replacements.'''

nums = [999,1,199]
l=[]
for i in range(len(nums)):
    sum=0
    while nums[i]>0:
        d=nums[i]%10
        nums[i]//=10
        sum+=d
    l.append(sum)
print(min(l))