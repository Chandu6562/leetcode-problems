# Number of Arithmetic Triplets
'''You are given a 0-indexed, strictly increasing integer array nums and a positive integer diff.
A triplet (i, j, k) is an arithmetic triplet if the following conditions are met:

i < j < k,
nums[j] - nums[i] == diff, and
nums[k] - nums[j] == diff.
Return the number of unique arithmetic triplets.'''

nums = [0,1,4,6,7,10]
diff = 3

num_set = set(nums)
count = 0

for x in nums:
    if (x + diff) in num_set and (x + 2*diff) in num_set:
        count += 1

print(count)