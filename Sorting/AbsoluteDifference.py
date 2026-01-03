# Absolute Difference Between Maximum and Minimum K Elements
'''You are given an integer array nums and an integer k.

Find the absolute difference between:

the sum of the k largest elements in the array; and
the sum of the k smallest elements in the array.
Return an integer denoting this difference.'''

nums = [5,2,2,4]
k = 2
nums.sort()
a=nums[:k]
b=nums[-k:]
x=abs(sum(a)-sum(b))
print(x)