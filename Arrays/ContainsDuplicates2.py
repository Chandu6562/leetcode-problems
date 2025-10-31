'''Given an integer array nums and an integer k, 
return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k'''

# Brute Force

# nums = [1, 2, 3, 1]
# k = 3
# found = False
# for i in range(len(nums)):
#     for j in range(i + 1, len(nums)):
#         if nums[i] == nums[j] and abs(i - j) <= k:
#             found = True
#             break
# print(found)


# Optimal Approach
nums = [1, 2, 3, 1]
k = 3
dici={}
flag=False
for i in range(len(nums)):
    if nums[i] in dici and i-dici[nums[i]]<=k:
        flag= True
    dici[nums[i]]=i
print(flag)
