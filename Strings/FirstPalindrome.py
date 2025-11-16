# Find First Palindromic String in the Array


words = ["abc","car","ada","racecar","cool"]
for i in words:
    if i == i[::-1]:
        print(i)
        break
else:
    print('')