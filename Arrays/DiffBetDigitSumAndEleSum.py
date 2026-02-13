# Difference Between Element Sum and Digit Sum of an Array
'''You are given a positive integer array nums.

The element sum is the sum of all the elements in nums.
The digit sum is the sum of all the digits (not necessarily distinct) that appear in nums.
Return the absolute difference between the element sum and digit sum of nums.

Note that the absolute difference between two integers x and y is defined as |x - y|.'''

nums = [1,15,6,3]
digit_sum=0
for i in nums:
    while i>0:
        digit= i%10
        i=i//10
        digit_sum += digit
ele_sum = sum(nums)
print(abs(ele_sum-digit_sum))
