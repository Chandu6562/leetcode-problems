# Find Common Elements Between Two Arrays
'''You are given two integer arrays nums1 and nums2 of sizes n and m, respectively. Calculate the following values:

answer1 : the number of indices i such that nums1[i] exists in nums2.
answer2 : the number of indices i such that nums2[i] exists in nums1.
Return [answer1,answer2].'''

nums1 = [2,3,2]
nums2 = [1,2]
l=[]
ans1=0
for i in nums1:
    if i in nums2:
        ans1+=1
l.append(ans1)
ans2=0
for i in nums2:
    if i in nums1:
        ans2+=1
l.append(ans2)
print(l)