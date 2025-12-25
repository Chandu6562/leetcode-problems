# Convert an Array Into a 2D Array With Conditions
'''You are given an integer array nums. You need to create a 2D array from nums satisfying the following conditions:

The 2D array should contain only the elements of the array nums.
Each row in the 2D array contains distinct integers.
The number of rows in the 2D array should be minimal.
Return the resulting array. If there are multiple answers, return any of them.

Note that the 2D array can have a different number of elements on each row.'''

# nums = [1, 3, 4, 1, 2, 3, 1]
nums = [1,2,3,4]
freq = {}
for num in nums:
    freq[num] = freq.get(num, 0) + 1
result = []
while True:
    row = []
    for num in freq:
        if freq[num] > 0:
            row.append(num)
            freq[num] -= 1
    if not row:
        break
    result.append(row)
print(result)
