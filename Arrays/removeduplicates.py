# # remove duplicats from sorted array

# Brute force

# The brute force solution takes O(n²) time because for every element in the array,
# you are searching through another list to check if it already exists.
# space O(n)
'''nums = [0,0,1,1,1,2,2,3,3,4]         
num=[]
for i in nums:
    if i not in num:
        num.append(i)
for i in range(len(num)):
    nums[i] = num[i]
k=len(num)
print(k)'''



# optimal solution
'''nums = [0,0,1,1,1,2,2,3,3,4]            # two pointers
k=0
for i in range(1,len(nums)):            # time O(n)
    if nums[k] != nums[i]:              # space O(1)
        k+=1
        nums[k]=nums[i]
print(k+1)'''