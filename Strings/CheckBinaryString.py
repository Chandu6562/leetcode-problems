# Check if Binary String Has at Most One Segment of Ones
'''Given a binary string s ​​​​​without leading zeros, return true​​​ if s contains at most one contiguous segment of ones. 
Otherwise, return false.'''

def checkBinaryString(s):
    for i in range(1,len(s)):
        if s[i] == '1' and s[i-1] == '0':
            return False
    return True
s = "110"
print(checkBinaryString(s))