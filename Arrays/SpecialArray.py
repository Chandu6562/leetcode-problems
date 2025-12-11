# Special Array I
'''An array is considered special if the parity of every pair of adjacent elements is different. 
In other words, one element in each pair must be even, and the other must be odd.

You are given an array of integers nums. Return true if nums is a special array, otherwise, return false'''

nums = [4,3,1,6]
flag=True
if len(nums)>1:
    for i in range(len(nums)-1):
        a=nums[i]
        b=nums[i+1]
        if (a%2==0 and b%2!=0) or (b%2==0 and a%2!=0):
            flag = True
        else:
            flag = False
            break
print(flag)