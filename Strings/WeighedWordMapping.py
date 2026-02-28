# Weighted Word Mapping
'''You are given an array of strings words, where each string represents a word containing lowercase English letters.

You are also given an integer array weights of length 26, where weights[i] represents the weight of the ith lowercase English letter.

The weight of a word is defined as the sum of the weights of its characters.

For each word, take its weight modulo 26 and map the result to a lowercase English letter 
using reverse alphabetical order (0 -> 'z', 1 -> 'y', ..., 25 -> 'a').

Return a string formed by concatenating the mapped characters for all words in order.'''

weights = [5,3,12,14,1,2,3,2,10,6,6,9,7,8,7,10,8,9,6,9,9,8,3,7,7,2]
words = ["abcd","def","xyz"]
res = {chr(97+i): value for i,value in enumerate(weights)}
ans=''
for word in words:
    temp=0
    for letter in word:
        if letter in res:
            temp+=res[letter]
    temp = temp%26
    ans += chr(122-temp)
print(ans)    