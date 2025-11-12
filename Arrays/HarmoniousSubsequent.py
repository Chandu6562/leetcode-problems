# Longest Harmonious Subsequence
'''We define a harmonious array as an array where the difference between its maximum value and its minimum value is exactly 1.

Given an integer array nums, return the length of its longest harmonious subsequence among all its possible subsequences.'''


# nums = [1,3,2,2,5,2,3,7]
# nums = [1,2,3,4]
nums = [1,1,1,1]
nums.sort()
d={}
for i in nums:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print(d)
ans=0
for j in d:
    if j+1 in d:
        ans=max(ans,d[j]+d[j+1])
print(ans)
