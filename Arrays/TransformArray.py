# Transform Array by Parity

nums=[4,3,2,1]
for i in range(len(nums)):
    if nums[i]%2==0:
        nums[i]=0
    else:
        nums[i]=1
print(sorted(nums))