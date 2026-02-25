# Rearrange Array Elements by Sign
'''You are given a 0-indexed integer array nums of even length consisting of an equal number of positive and negative integers.

You should return the array of nums such that the array follows the given conditions:

Every consecutive pair of integers have opposite signs.
For all integers with the same sign, the order in which they were present in nums is preserved.
The rearranged array begins with a positive integer.
Return the modified array after rearranging the elements to satisfy the aforementioned conditions.

 '''
 
nums = [3,1,-2,-5,2,-4]
positive_nums=[]
negative_nums=[]
result=[]
for i in nums:
    if i>0:
        positive_nums.append(i)
    else:
        negative_nums.append(i)
for i in range(len(positive_nums)):
    result.extend([positive_nums[i],negative_nums[i]])
print(result)