# Missing Number
'''Given an array nums containing n distinct numbers in the range [0, n], 
return the only number in the range that is missing from the array.'''

# Brute Force
# nums = [0,3,1]
# for i in range(len(nums)+1):
#     if i not in nums:
#         print(i)
#         break


# Optimal Solution

nums = [3,0,1]
n=len(nums)
a=n*(n+1)//2
b=sum(nums)
print(a-b)