# 2942. Find Words Containing Character

words = ["abc","bcd","aaaa","cbc"]
x = "e"
ans=[]
for i in range(len(words)):
    if x in words[i]:
        ans.append(i)
print(ans)