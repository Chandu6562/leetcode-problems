'''Given an integer array nums, return true if any value appears at least twice in the array, 
and return false if every element is distinct'''

# Brute Force

# nums = [1,2,3,4]
# nums.sort()
# flag=False
# for i in range(len(nums)-1):
#     if nums[i]==nums[i+1]:
#         flag=True
# print(flag)


# Optimal Approach

nums = [1, 2, 3, 1]

seen = set()
for num in nums:
    if num in seen:
        print(True)
        break
    seen.add(num)
else:
    print(False)
