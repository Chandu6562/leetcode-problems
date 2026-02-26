# Reverse Letters Then Special Characters in a String
'''You are given a string s consisting of lowercase English letters and special characters.

Your task is to perform these in order:

Reverse the lowercase letters and place them back into the positions originally occupied by letters.
Reverse the special characters and place them back into the positions originally occupied by special characters.
Return the resulting string after performing the reversals.'''

s = ")ebc#da@f("
ch=''
sym=''
for i in s:
    if i.islower():
        ch=i+ch
    else:
        sym=i+sym
ch_index = 0
sym_index = 0
res=''
for j in s:
    if j.islower():
        res+=ch[ch_index]
        ch_index+=1
    else:
        res+=sym[sym_index]
        sym_index+=1
print(res)