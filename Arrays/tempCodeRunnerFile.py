or i in range(len(nums)-1,-1,-1):
    if nums[i] == 0:
        nums.append(nums[i])
        nums.pop(i)
print(nu