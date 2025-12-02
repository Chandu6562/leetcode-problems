# Sorting the Sentence
'''A sentence is a list of words that are separated by a single space with no leading or trailing spaces. 
Each word consists of lowercase and uppercase English letters.

A sentence can be shuffled by appending the 1-indexed word position to each word then rearranging the words in the sentence.

For example, the sentence "This is a sentence" can be shuffled as "sentence4 a3 is2 This1" or "is2 sentence4 This1 a3".
Given a shuffled sentence s containing no more than 9 words, reconstruct and return the original sentence.'''

s = "is2 sentence4 This1 a3"
a=s.split()
l=[]
for j in range(1,len(a)+1):
    for i in range(len(a)):
        if str(j) in a[i]:
            l.append(a[i].replace(str(j),''))
print(" ".join(l))