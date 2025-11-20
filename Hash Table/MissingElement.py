# Find Missing Elements
'''Originally, nums contained every integer within a certain range. However, some integers might have gone missing from the array.

The smallest and largest integers of the original range are still present in nums.

Return a sorted list of all the missing integers in this range. If no integers are missing, return an empty list.'''


nums = [5,1]
m=max(nums)
n=min(nums)
l=[]
for i in range(n,m):
   if i not in nums:
       l.append(i)
print(l)