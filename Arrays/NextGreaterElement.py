# 496. Next Greater Element I

# Using HashMap
# nums1 = [2,4]
# nums2 = [1,2,3,4]
# dict = {}
# l = len(nums2)

# for i in range(l):                
#     one = nums2[i]
#     for j in range(i+1, l):       
#         two = nums2[j]
#         if two > one:
#             dict[one] = two
#             break
#     else:
#         dict[one] = -1

# print(dict)

# res = []
# for num in nums1:                 
#     res.append(dict[num])
# print(res)




nums1 = [4,1,2]
nums2 = [1,3,4,2]
ans=[]
for i in nums1:
    index=nums2.index(i)
    next_greater=-1
    for j in range(index+1,len(nums2)):
        if nums2[j]>i:
            next_greater=nums2[j]
            break
    ans.append(next_greater)
print(ans)