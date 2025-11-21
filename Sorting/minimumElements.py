# Minimum Average of Smallest and Largest Elements
'''You have an array of floating point numbers averages which is initially empty.
You are given an array nums of n integers where n is even.

You repeat the following procedure n / 2 times:

Remove the smallest element, minElement, and the largest element maxElement, from nums.
Add (minElement + maxElement) / 2 to averages.
Return the minimum element in averages'''

def fun(nums):
    arr=[]
    i=len(nums)//2
    while i>0:
        x=min(nums)
        y=max(nums)
        arr.append((x+y)/2.0)
        nums.remove(x)
        nums.remove(y)
        i-=1
    return min(arr)
nums = [7,8,3,4,15,13,4,1]
print(fun(nums))