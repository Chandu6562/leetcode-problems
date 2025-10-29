# 1876 Substrings of size three with Distnict characters.

# Brute Force 
# s='aababcabc'
# res=0
# for i in range(len(s)):
#     for j in range(i+1,len(s)):
#         temp=""
#         for k in range(i,j+1):
#             temp+=s[k]
#         if len(temp)==3 and len(set(temp)) == 3:
#             res+=1
# print(res)


# optimal solution
s='aababcabc'
l=0
res=0
dict={}
k=3
for r in range(len(s)):
    if s[r] in dict:
        dict[s[r]]+=1
    else:
        dict[s[r]]=1
    if r-l == k:
        dict[s[l]]-=1
        if dict[s[l]]==0:
            dict.pop(0)
        l+=1
    if len(dict)==k:
        res+=1
print(res)