# Maximum Number of Words You Can Type
'''There is a malfunctioning keyboard where some letter keys do not work. All other keys on the keyboard work properly.

Given a string text of words separated by a single space (no leading or trailing spaces) 
and a string brokenLetters of all distinct letter keys that are broken, 
return the number of words in text you can fully type using this keyboard.'''

text = "leet code"
brokenLetters = "lt"
text_list=text.split()
broken_words=0
for word in text_list:
    for i in brokenLetters:
        if i in word:
            broken_words+=1
            break
print(len(text_list)-broken_words)