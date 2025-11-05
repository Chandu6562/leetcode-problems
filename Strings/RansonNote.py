# Ransome Note
'''Given two strings ransomNote and magazine, 
return true if ransomNote can be constructed by using the letters from magazine and false otherwise.'''

ransomNote = "aa"
magazine = "ab"
for ch in ransomNote:
    if ch in magazine:
        magazine = magazine.replace(ch, "", 1)  # remove one occurrence
    else:
        print(False)
        break
else:
    print(True)