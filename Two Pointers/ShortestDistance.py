# Shortest Distance to a Character
'''Given a string s and a character c that occurs in s, 
return an array of integers answer where answer.length == s.length and answer[i] is the distance 
from index i to the closest occurrence of character c in s.

The distance between two indices i and j is abs(i - j), where abs is the absolute value function.'''

# s = "loveleetcode"
# c = "e"
# res=[]
# for i in range(len(s)):
#     temp=float("inf")
#     for j in range(len(s)):
#         if s[j]==c:
#             temp=min(temp,abs(i-j))
#     res.append(temp)
# print(res)


s = "loveleetcode"
c = "e"
left_distance=0
last_seen = float("-inf")
res=[]
for i in range(len(s)):
    if s[i] == c:
        last_seen=i
    left_distance=i-last_seen
    res.append(left_distance)    
right_distance=0
last_seen = float("inf")
for i in range(len(s)-1,-1,-1):
    if s[i] == c:
        last_seen=i
    right_distance=last_seen-i
    res[i] = min(res[i],right_distance)   
print(res)