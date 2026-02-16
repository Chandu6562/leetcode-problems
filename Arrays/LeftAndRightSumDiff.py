# Left and Right Sum Differences

'''You are given a 0-indexed integer array nums of size n.

Define two arrays leftSum and rightSum where:

leftSum[i] is the sum of elements to the left of the index i in the array nums. If there is no such element, leftSum[i] = 0.
rightSum[i] is the sum of elements to the right of the index i in the array nums. If there is no such element, rightSum[i] = 0.
Return an integer array answer of size n where answer[i] = |leftSum[i] - rightSum[i]|.'''

nums = [10,4,8,3]

left = []
right = []
res=[]
lsum=0
for i in range(len(nums)):
    left.append(lsum)
    lsum+=nums[i]
rsum=0
for i in range(len(nums)-1,-1,-1):
    right.insert(0,rsum)
    rsum+=nums[i]
for i in range(len(nums)):
    res.append(abs(left[i]-right[i]))
print(res)