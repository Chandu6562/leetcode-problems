# 1984 Minimum difference between lowest and highest of k scores
'''You are given a 0-indexed integer array nums, where nums[i] represents the score of the ith student. You are also given an integer k.
Pick the scores of any k students from the array so that the difference between the highest and the lowest of the k scores is minimized.
Return the minimum possible difference.'''

# Brute force 
# nums = [9,4,1,7]
# nums.sort()
# k=2
# print(nums)
# ans=float("inf")
# for i in range(len(nums)):
#     for j in range(i,len(nums)):
#         temp=[]
#         for m in range(i,j+1):
#             temp.append(nums[m])
#         if len(temp)==k:
#             first=temp[0]
#             last=temp[-1]
#             ans=min(ans,last-first)
# print(ans)

# optimal solution
nums = [9,4,1,7]
nums.sort()
k=2
l=0
ans=float("inf")
for r in range(len(nums)):
    if r-l ==k:
        l+=1
    if r-l+1==k:
        ans=min(ans,nums[r]-nums[l])
print(ans)