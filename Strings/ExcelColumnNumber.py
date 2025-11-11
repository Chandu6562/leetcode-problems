# Excel Sheet Column Number
'''Given a string columnTitle that represents the column title as appears in an Excel sheet, return its corresponding column number.'''


s=input("Enter: ")
res=0
for i in s:
    res=res*26
    res+=ord(i)-64
print(res)