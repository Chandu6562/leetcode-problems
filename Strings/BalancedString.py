# Check Balanced String
'''You are given a string num consisting of only digits. 
A string of digits is called balanced if the sum of the digits at even indices is equal to the sum of digits at odd indices.

Return true if num is balanced, otherwise return false.'''

num = "24123"
even_sum = 0
odd_sum = 0
for i in range(len(num)):
    if i%2==0:
        even_sum+=int(num[i])
    else:
        odd_sum+=int(num[i])
if even_sum == odd_sum:
    print(True)
else:
    print(False)