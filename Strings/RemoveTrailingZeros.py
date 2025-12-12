# Remove Trailing Zeros From a String
'''Given a positive integer num represented as a string, return the integer num without trailing zeros as a string.'''

num = "51230100"
# num='123'
i = len(num) - 1
while i >= 0 and num[i] == '0':
    i -= 1
print(num[:i+1])