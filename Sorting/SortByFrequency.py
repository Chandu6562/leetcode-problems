#  Sort Array by Increasing Frequency
'''Given an array of integers nums, sort the array in increasing order based on the frequency of the values. 
If multiple values have the same frequency, sort them in decreasing order.

Return the sorted array.'''

# nums = [1,1,2,2,2,3]
nums = [2,3,1,3,2]
freq = {}
for i in nums:
    count = 0
    for j in nums:
        if i == j:
            count += 1
    freq[i] = count
nums = sorted(nums, key=lambda x: (freq[x], -x))
print(nums)
