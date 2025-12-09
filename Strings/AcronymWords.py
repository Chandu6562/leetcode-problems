# Check if a String Is an Acronym of Words
'''Given an array of strings words and a string s, determine if s is an acronym of words.

The string s is considered an acronym of words if it can be formed by concatenating the first character of each string in words in order.
For example, "ab" can be formed from ["apple", "banana"], but it can't be formed from ["bear", "aardvark"].

Return true if s is an acronym of words, and false otherwise.'''

# words = ["never","gonna","give","up","on","you"]
# s = "ngguoy"
words = ["dvn","acafe"]
s = "dp"
word_len=len(words)
string_len=len(s)
if word_len == string_len:
    flag=False
    for i in range(word_len):
        if s[i] ==words[i][0]:
            flag=True
        else:
            flag = False
            break
    print(flag)
else:
    print(False)