#Remove Element

# Brute force
# nums=[0,1,2,2,3,0,4,2] 
# val=2
# new_list=[]
# for i in range(len(nums)):
#     if nums[i] != val:
#         new_list.append(nums[i])
# for i in range(len(new_list)):
#     nums[i]=new_list[i]
# print(len(new_list))


# optimal solution
nums=[0,1,2,2,3,0,4,2] 
val=2
i=0
for j in range(len(nums)):
    if nums[j] != val:
        nums[i] = nums[j]
        i+=1
print(i)