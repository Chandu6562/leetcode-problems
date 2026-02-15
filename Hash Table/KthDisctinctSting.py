# Kth Distinct String in an Array
'''A distinct string is a string that is present only once in an array.

Given an array of strings arr, and an integer k, return the kth distinct string present in arr. 
If there are fewer than k distinct strings, return an empty string "".

Note that the strings are considered in the order in which they appear in the array.'''

def KthDistictString(arr,k):
    d={}
    for i in arr:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    count = 0
    for j in arr:
        if d[j] == 1:
            count+=1
            if count == k:
                return j
    return ""
arr = ["aaa","aa","a"]
k = 1
print(KthDistictString(arr,k))