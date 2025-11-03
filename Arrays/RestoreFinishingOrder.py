# 3668. Restore Finishing Order

order = [3,1,2,5,4]
friends = [1,3,4]
ans=[]
for i in range(len(order)):
    if order[i] in friends:
        ans.append(order[i])
print(ans)