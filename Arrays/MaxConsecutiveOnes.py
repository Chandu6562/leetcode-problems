# Max Consecutive Ones
'''Given a binary array nums and an integer k, 
return the maximum number of consecutive 1's in the array if you can flip at most k 0's.'''

# Brute Force
# nums = [1,1,1,0,0,0,1,1,1,1,0]
# k = 2
# max_len = 0
# for i in range(len(nums)):
#     zeros = 0
#     for j in range(i, len(nums)):
#         if nums[j] == 0:
#             zeros += 1
#         if zeros > k:
#             break
#         max_len = max(max_len, j - i + 1)

# print(max_len)


# Optimal Solution
nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
l=0
temp=0
ans=0
for r in range(len(nums)):
    if nums[r] == 0:
        temp+=1
    while temp>k:
        if nums[l] == 0:
            temp-=1
        l+=1
    ans = max(ans,r-l+1)
print(ans)