#  Intersection of Two Arrays

nums1 = [1,2,2,1]
nums2 = [2,2]
l=[]
for i in range(len(nums1)):
    if nums1[i] in nums2 and nums1[i] not in l:
        l.append(nums1[i])
print(l)