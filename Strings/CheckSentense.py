# Check if the Sentence Is Pangram

'''A pangram is a sentence where every letter of the English alphabet appears at least once.

Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.'''

# sentence = "thequickbrownfoxjumpsoverthelazydog"
sentence='leetcode'
alphabets="abcdefghijklmnopqrstuvwxyz"
flag=False
if len(sentence)>=26:
    for i in alphabets:
        if i in sentence:
            flag=True
        else:
            flag=False
            break
print(flag)