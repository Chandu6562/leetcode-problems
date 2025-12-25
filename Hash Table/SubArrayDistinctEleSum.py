# Subarrays Distinct Element Sum of Squares I
'''You are given a 0-indexed integer array nums.

The distinct count of a subarray of nums is defined as:

Let nums[i..j] be a subarray of nums consisting of all the indices from i to j such that 0 <= i <= j < nums.length. 
Then the number of distinct values in nums[i..j] is called the distinct count of nums[i..j].
Return the sum of the squares of distinct counts of all subarrays of nums.

A subarray is a contiguous non-empty sequence of elements within an array.'''

nums = [1, 2, 1]
n = len(nums)
ans = 0
for i in range(n):
    distinct = set()
    for j in range(i, n):
        distinct.add(nums[j])
        ans += len(distinct) * len(distinct)
print(ans)
