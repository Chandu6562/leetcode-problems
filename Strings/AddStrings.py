# Add Strings
'''Given two non-negative integers, num1 and num2 represented as string, 
return the sum of num1 and num2 as a string.

You must solve the problem without using any built-in library for handling large integers (such as BigInteger). 
You must also not convert the inputs to integers directly.'''


def addStrings(num1, num2):
    i, j = len(num1) - 1, len(num2) - 1
    carry = 0
    result = []

    while i >= 0 or j >= 0 or carry:
        x = ord(num1[i]) - ord('0') if i >= 0 else 0
        y = ord(num2[j]) - ord('0') if j >= 0 else 0
        total = x + y + carry
        result.append(chr(total % 10 + ord('0')))
        carry = total // 10
        i -= 1
        j -= 1

    return ''.join(reversed(result))

print(addStrings("456", "77"))  # Output: "533"
