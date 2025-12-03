# Count Asterisks
'''You are given a string s, where every two consecutive vertical bars '|' are grouped into a pair.
In other words, the 1st and 2nd '|' make a pair, the 3rd and 4th '|' make a pair, and so forth.

Return the number of '*' in s, excluding the '*' between each pair of '|'.

Note that each '|' will belong to exactly one pair.'''

# s = "a|bc|d***|e|f"
s = "l|*e*|e*|rr|*e|*|"
inside = False
count = 0
for ch in s:
    if ch == '|':
        inside = not inside     # toggle state
    elif ch == '*' and not inside:
        count += 1
print(count)