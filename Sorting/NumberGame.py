# Minimum Number Game
'''You are given a 0-indexed integer array nums of even length and there is also an empty array arr. 
Alice and Bob decided to play a game where in every round Alice and Bob will do one move. The rules of the game are as follows:

Every round, first Alice will remove the minimum element from nums, and then Bob does the same.
Now, first Bob will append the removed element in the array arr, and then Alice does the same.
The game continues until nums becomes empty.
Return the resulting array arr.'''

# nums = [5,4,2,3]
nums = [2,5]
arr=[]
i=len(nums)//2
while i>0:
    alice=min(nums)
    nums.remove(alice)
    bob=min(nums)
    nums.remove(bob)
    arr.append(bob)
    arr.append(alice)
    i-=1
print(arr)