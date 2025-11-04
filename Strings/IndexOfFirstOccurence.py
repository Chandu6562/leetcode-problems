# Find the Index of the First Occurrence in a String

haystack = "butsad"
needle = "sad"
l=len(needle)
if needle in haystack:
    for i in range(len(haystack)):
        if haystack[i:i+l] == needle[:]:
            print(i)
            break
else:
    print(-1)