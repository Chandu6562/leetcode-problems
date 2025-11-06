# Find Most Frequent Vowel and Consonant


s='successes'
vowel_count=0
consonant_count=0
for i in s:
    if i in "aeiou":
        a=s.count(i)
        vowel_count=max(vowel_count,a)
    else:
        b=s.count(i)
        consonant_count=max(consonant_count,b)
print(vowel_count+consonant_count)