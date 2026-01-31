# Determine if String Halves Are Alike
'''You are given a string s of even length. Split this string into two halves of equal lengths,
and let a be the first half and b be the second half.

Two strings are alike if they have the same number of vowels ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'). 
Notice that s contains uppercase and lowercase letters.

Return true if a and b are alike. Otherwise, return false.'''

# s = "book"
s = "textbook"
l=list(s)
n=len(l)//2
a=l[:n]
b=l[n:]
a_count=0 
b_count=0
for i in range(len(a)):
    if a[i] in "AEIOUaeiou":
        a_count+=1
    if b[i] in "AEIOUaeiou":
        b_count+=1
print(a_count==b_count)