# 3289. The Two Sneaky Numbers of Digitville

# nums = [0,3,2,1,3,2]
# res = []
# for i in range(len(nums)):
#     for j in range(i + 1, len(nums)):
#         if nums[i] == nums[j] and nums[i] not in res:
#             res.append(nums[i])
# print(res)

nums = [0,3,2,1,3,2]
seen = set()
res = []
for num in nums:
    if num in seen:
        res.append(num)
    else:
        seen.add(num)
print(res)