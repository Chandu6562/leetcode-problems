# # remove duplicats from sorted array

# Brute force

# nums = [1,1,2]
# # nums=set(nums)
# # print(nums,len(nums))

# num=[]
# for i in nums:
#     if i not in num:
#         num.append(i)
# print(len(num))



# optimal solution
nums = [0,0,1,1,1,2,2,3,3,4]            # two pointers
k=0
for i in range(1,len(nums)):
    if nums[k] != nums[i]:
        k+=1
        nums[k]=nums[i]
print(k+1)