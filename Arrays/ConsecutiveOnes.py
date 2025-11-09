# Max Consecutive Ones

nums = [1,1,0,1,1,0,1,1,1]
temp=0
ans=0
for i in range(len(nums)):
    if nums[i]==1:
        temp+=1
    else:
        temp=0
    ans=max(ans,temp)
print(ans)