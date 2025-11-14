#  Shuffle the Array

'''Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].

Return the array in the form [x1,y1,x2,y2,...,xn,yn].'''


nums = [2,5,1,3,4,7]
n = 3
n1=nums[:n]
n2=nums[n:]
l=[]
for i in range(n):
    l.append(n1[i])
    l.append(n2[i])
print(l)