# Compute Alternating Sum

# nums = [1,3,5,7]
nums = [100]
even=0
odd=0
for i in range(len(nums)):
    if i%2==0:
        even+=nums[i]
    else:
        odd+=nums[i]
print(even-odd)
