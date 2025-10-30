'''Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.'''


# Brute Force Approach (O(n))
# nums = [1,3,5,6]
# target = 4
# flag=0
# for i in range(len(nums)):
#     if nums[i]==target:
#         print(i)
#     elif nums[i]<target:
#         flag=i+1
# print(flag)

# nums = [1, 3, 5, 6]
# target = 2
# for i in range(len(nums)):
#     if nums[i] >= target:
#         print(i)
#         break
# else:
#     print(len(nums))



# Optimal Approach (O(log n)) — Binary Search

nums = [1, 3, 5, 6]
target = 2
left, right = 0, len(nums) - 1
while left <= right:
    mid = (left + right) // 2
    if nums[mid] == target:
        print(mid)
        break
    elif nums[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
else:
    print(left)
