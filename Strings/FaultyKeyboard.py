# Faulty Keyboard
'''Your laptop keyboard is faulty, and whenever you type a character 'i' on it,
it reverses the string that you have written. Typing other characters works as expected.

You are given a 0-indexed string s, and you type each character of s using your faulty keyboard.

Return the final string that will be present on your laptop screen.'''

# s = "string"
s = "poiinter"
res=[]
for i in s:
    if i == 'i':
        res.reverse()
    else:
        res.append(i)
print("".join(res))