# Number of Changing Keys
'''You are given a 0-indexed string s typed by a user. 
Changing a key is defined as using a key different from the last used key. For example, 
s = "ab" has a change of a key while s = "bBBb" does not have any.

Return the number of times the user had to change the key.

Note: Modifiers like shift or caps lock won't be counted in changing the key that is 
if a user typed the letter 'a' and then the letter 'A' then it will not be considered as a changing of key.'''

s = "aAbBcC"
s1=s.lower()
count=0
for i in range(len(s1)-1):
    if s1[i]!=s1[i+1]:
        count+=1
print(count)