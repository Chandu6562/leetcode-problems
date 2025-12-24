# Count Elements With Maximum Frequency
'''You are given an array nums consisting of positive integers.

Return the total frequencies of elements in nums such that those elements all have the maximum frequency.

The frequency of an element is the number of occurrences of that element in the array.'''

# nums = [1,2,2,3,1,4]
nums=[10,12,11,9,6,19,11]
d={}
for i in nums:
    if i not in d:
        d[i]= nums.count(i)
freq=max(d.values())
count=0
for v in d.values():
    if v==freq:
        count+=v
print(count)