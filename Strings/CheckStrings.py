# Check If Two String Arrays are Equivalent


'''Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.'''

word1 = ["a", "cb"]
word2 = ["ab", "c"]
# word1 = ["ab", "c"]
# word2 = ["a", "bc"]
a1="".join(word1)
a2="".join(word2)
print(a1==a2)