# brute force appraoch
# nums = [2,7,11,15]
# target = 9                                # Time Complexity - O(n²) - Two nested loops checking all pairs
# for i in range(len(nums)):                # Space Complexity - O(1) - No extra space used beyond a few variables
#     for j in range(i+1,len(nums)):
#         if nums[i]+nums[j] == target:
#             print([i,j])

# optimal solution
nums = [2,7,11,15]
target = 9
dict={}
for i in range(len(nums)):                  # Time Complexity - O(n) - Single pass with O(1) lookups
    a=target-nums[i]                        # Space Complexity - O(n) - Dictionary stores up to n elements
    if a in dict:
        print([dict[a],i])
    else:
        dict[nums[i]]=i