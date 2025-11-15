# Reverse Prefix of Word
'''Given a 0-indexed string word and a character ch, reverse the segment of word that starts at
index 0 and ends at the index of the first occurrence of ch (inclusive). If the character ch does not exist in word, do nothing.'''


word = "abcdefd"
ch = "d"
if ch in word:
    index=word.index(ch)+1
    result=word[:index][::-1]+word[index:]
    print(result) 
else:
    print(word) 