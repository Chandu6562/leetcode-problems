# Intersection of Two Arrays II

nums1 = [1,2,2,1]
nums2 = [2,1]
l=[]
for i in range(len(nums1)):
    if nums1[i] in nums2:
        l.append(nums1[i])
        nums2.remove(nums1[i])
print(l)