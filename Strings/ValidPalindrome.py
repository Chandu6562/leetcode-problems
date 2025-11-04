'''A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and 
removing all non-alphanumeric characters,
it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.'''





# s = "A man, a plan, a canal: Panama"
# a=s.lower()
# res1=""
# for i in a:
#     if i.isalnum():
#         res1+=i
# res2=res1[::-1]
# if res1 == res2:
#     print(True)
# else:
#     print(False)
    
    
    
    
s = "A man, a plan, a canal: Panama"
left, right = 0, len(s) - 1

while left < right:
    # Move left pointer until alphanumeric
    while left < right and not s[left].isalnum():
        left += 1
    # Move right pointer until alphanumeric
    while left < right and not s[right].isalnum():
        right -= 1
    
    # Compare after converting to lowercase
    if s[left].lower() != s[right].lower():
        print(False)
        break

    left += 1
    right -= 1
else:
    print(True)