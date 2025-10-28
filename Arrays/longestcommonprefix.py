# Brute force 

# strs = ["dog","racecar","car"]
# # strs = ["flower","flow","flight"]
# if not strs:
#     print("")
# else:
#     for i in range(len(strs)):
#         ch = strs[0][i]
#         for s in strs[1:]:
#             if i >= len(s) or s[i] != ch:
#                 print(strs[0][:i])
#                 exit()
# print(strs[0])


# optimal solution
# strs = ["dog","racecar","car"]
strs = ["flower","flow","flight"]
strs.sort()
res=""
for i in range(len(strs[0])):
    if strs[0][i] == strs[-1][i]:
        res+=strs[0][i] 
    else:
        break
print(res)