# First Unique Character in a String


# Brute Force
# s = "leetcode"
# for i in range(len(s)):
#     count=0
#     for j in range(len(s)):
#         if i != j and s[i] == s[j]:
#             count+=1
#     if count == 0:
#         print(i)
#         break
# else:
#     print(-1)

# optimal Solution
s = "leetcode"
d={}
for i in s:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
for i,j in enumerate(s):
    if d[j]== 1:
        print(i)
        break
else:
    print(-1)