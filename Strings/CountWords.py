# Counting Words With a Given Prefix


words = ["leetcode","win","loops","success"]
pref = "code"
l=len(pref)
count=0
for i in words:
    if i[:l]==pref:
        count+=1
print(count)