# Two Out of Three
'''Given three integer arrays nums1, nums2, and nums3, 
return a distinct array containing all the values that are present in at least two out of the three arrays. 
You may return the values in any order.'''

nums1 = [3,1]
nums2 = [2,3]
nums3 = [1,2]
n1=set(nums1)
n2=set(nums2)
n3=set(nums3)
a=n1.intersection(n2)
b=n2.intersection(n3)
c=n3.intersection(n1)

x=a.union(b)
y=b.union(c)
print(list(x.union(y)))