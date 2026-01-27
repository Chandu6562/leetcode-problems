#Make Two Arrays Equal by Reversing Subarrays
'''You are given two integer arrays of equal length target and arr. In one step, 
you can select any non-empty subarray of arr and reverse it. You are allowed to make any number of steps.

Return true if you can make arr equal to target or false otherwise.'''

target = [3,7,9]
arr = [3,7,11]
if arr == target:
    print('True')
else:
    arr.sort()
    target.sort()
    print(arr == target)