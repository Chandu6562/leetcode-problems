# Find the Difference of Two Arrays
'''Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:

answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
answer[1] is a list of all distinct integers in nums2 which are not present in nums1.
Note that the integers in the lists may be returned in any order.'''

nums1 = [1,2,3]
nums2 = [2,4,6]
n1=set(nums1)
n2=set(nums2)
x=list(n1.difference(n2))
y=list(n2.difference(n1))
print([x,y])