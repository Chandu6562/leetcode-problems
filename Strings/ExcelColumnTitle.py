# Excel Sheet Column Title
'''Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.'''

columnNumber=int(input("Enter a Number: "))
result=''
while columnNumber>0:
    columnNumber-=1
    remainder=columnNumber%26
    result = chr(remainder+65)+result
    columnNumber//=26
print(result)