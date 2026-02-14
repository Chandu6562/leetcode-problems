# Minimum Index Sum of Two Lists
'''Given two arrays of strings list1 and list2, find the common strings with the least index sum.

A common string is a string that appeared in both list1 and list2.

A common string with the least index sum is a common string such that if it appeared 
at list1[i] and list2[j] then i + j should be the minimum value among all the other common strings.

Return all the common strings with the least index sum. Return the answer in any order.'''

list1=["dixyp","uq","q","KFC"]
list2=["yl","fjugc","rlni","dixyp","uq","q","KFC"]

d1={ ele:index for index,ele in enumerate(list1)}
d2={ ele:index for index,ele in enumerate(list2)}

common_dict={}

for key in d1:
    if key in d2:
        common_dict[key] = d1[key] + d2[key]

min_sum = float("inf")
res = []

for k, v in common_dict.items():
    if v < min_sum:
        min_sum = v
        res = [k]     
    elif v == min_sum:
        res.append(k)

print(res)