# Count the Number of Consistent Strings


allowed = "abc"
words = ["a","b","c","ab","ac","bc","abc"]
count=len(words)
for word in range(len(words)):
    for ch in words[word]:
        if ch not in allowed:
            count-=1
            break
print(count)