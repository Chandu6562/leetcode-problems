# Valid Parentheses
'''Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.'''


# Using Sting

# s = "([)]"
# pair=['{}','[]','()']
# while True:
#     flag=False
#     for i in pair:
#         if i in s:
#             s=s.replace(i,'')
#             flag=True
#     if not flag:
#         break
# print(len(s)==0)


# Using Stack
s = "()"
stack=[]
pair={']':'[','}':'{',')':'('}
for i in s:
    if i in pair:
        if stack and stack[-1]==pair[i]:
            stack.pop()
        else:
            print(False)
            break
    else:
        stack.append(i)
print(len(stack)==0)