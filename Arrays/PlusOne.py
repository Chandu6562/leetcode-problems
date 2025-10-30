'''You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.
Increment the large integer by one and return the resulting array of digits.'''

# Brute Force Approach

# digits = [1,2,3]
# a=""
# for i in range(len(digits)):
#     a+=str(digits[i])
# s=int(a)+1
# l=[]
# while s>0:
#     d=s%10
#     s=s//10
#     l.insert(0,d)
# print(l)

# digits = [1, 2, 3]
# num = int("".join(map(str, digits)))                  # Time: O(n)
# num += 1                                              # Space: O(n)
# result = [int(x) for x in str(num)]
# print(result)


# Optimal Approach (Digit-by-Digit, No Conversion)
digits = [9, 9, 9]

for i in range(len(digits) - 1, -1, -1):
    if digits[i] < 9:                               # Time: O(n) → single pass through the digits
        digits[i] += 1                              # Space: O(1) → in-place modification (except possible extra digit if carry)
        print(digits)
        break
    digits[i] = 0
else:
    digits.insert(0, 1)
print(digits)
