# Relative Ranks
'''You are given an integer array score of size n, where score[i] is the score of the ith athlete in a competition. 
All the scores are guaranteed to be unique.

The athletes are placed based on their scores, where the 1st place athlete has the highest score, 
the 2nd place athlete has the 2nd highest score, and so on. The placement of each athlete determines their rank:

The 1st place athlete's rank is "Gold Medal".
The 2nd place athlete's rank is "Silver Medal".
The 3rd place athlete's rank is "Bronze Medal".
For the 4th place to the nth place athlete, their rank is their placement number (i.e., the xth place athlete's rank is "x").
Return an array answer of size n where answer[i] is the rank of the ith athlete.
'''


score = [10,3,8,9,4]
# score=[5,4,3,2,1]
score1=sorted(score,reverse=True)
d={}
for i in range(len(score)):
    d[score1[i]]=str(i+1)
res=[]
for i in score:
    if d[i]=='1':
        res.append('Gold Medal')
    elif d[i]=='2':
        res.append('Silver Medal')
    elif d[i]=='3':
        res.append('Bronze Medal')
    else:
        res.append(d[i])
    print(d[i])
print(res)