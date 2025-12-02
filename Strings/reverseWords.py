# Reverse Words in a String III
'''Given a string s, reverse the order of characters in each word within a sentence 
while still preserving whitespace and initial word order'''

s = "Let's take LeetCode contest"
l=s.split()
string=[]
for i in l:
    string.append(i[::-1])
print(" ".join(string))