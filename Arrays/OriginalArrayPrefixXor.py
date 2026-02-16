# Find The Original Array of Prefix Xor

'''You are given an integer array pref of size n. Find and return the array arr of size n that satisfies:

pref[i] = arr[0] ^ arr[1] ^ ... ^ arr[i].
Note that ^ denotes the bitwise-xor operation.

It can be proven that the answer is unique.'''

pref = [5,2,0,3,1]
res=[]
for i in range(len(pref)):
    a=pref[i]^pref[i-1]
    res.append(a)
res[0]=pref[0]
print(res)