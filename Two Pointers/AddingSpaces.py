# Adding Spaces to a String
'''You are given a 0-indexed string s and a 0-indexed integer array spaces that describes the indices in the original string where spaces will be added. Each space should be inserted before the character at the given index.

For example, given s = "EnjoyYourCoffee" and spaces = [5, 9], we place spaces before 'Y' and 'C', which are at indices 5 and 9 respectively. Thus, we obtain "Enjoy Your Coffee".
Return the modified string after the spaces have been added.'''


# s = "icodeinpython"
# spaces = [1,5,7,9]
# res = []
# j = 0  # pointer for spaces

# for i in range(len(s)):
#     # If current index matches a space position
#     if j < len(spaces) and i == spaces[j]:
#         res.append(' ')
#         j += 1
    
#     res.append(s[i])

# print(''.join(res))

s = "icodeinpython"
spaces = [1,5,7,9]
i=0
j=0
res=[]
while (i<len(s) and j<len(spaces)):
    if i == spaces[j]:
        res.append(" ")
        j+=1
    else:
        res.append(s[i])
        i+=1
res.append(s[i:])
print("".join(res))