'''Variable Size Sliding Window.
You are given an array and You should
Find the maximum length of the
subarray which has atmost k ones'''






n=[0,1,3,1,1,6,7,1,0,1]
k =2
temp=0
l=0
ans=0
for r in range(len(n)):
    if n[r] == 1:
        temp+=1
    while temp>k:
        if n[l]==1:
            temp-=1
        l+=1
    ans=max(ans,r-l+1)
print(ans)