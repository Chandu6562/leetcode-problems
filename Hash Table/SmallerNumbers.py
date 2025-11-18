# How Many Numbers Are Smaller Than the Current Number
'''Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it.
That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].

Return the answer in an array.'''

nums = [8,1,2,2,3]
l=[]
count =0
for i in range(len(nums)):
    for j in range(len(nums)):
        if nums[i]>nums[j]:
         count+=1
    l.append(count)
    count=0
print(l)