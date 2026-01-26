# Sum of Unique Elements
'''You are given an integer array nums. The unique elements of an array are the elements that appear exactly once in the array.

Return the sum of all the unique elements of nums.'''

nums = [1,2,3,2,5]
sum=0
for i in nums:
    if nums.count(i)<=1:
        sum+=i
print(sum)