# Sort the People
'''You are given an array of strings names, and an array heights that consists of distinct positive integers. Both arrays are of length n.

For each index i, names[i] and heights[i] denote the name and height of the ith person.

Return names sorted in descending order by the people's heights.'''

names = ["Mary","John","Emma"]
heights = [180,165,170]
pairs = list(zip(heights, names))  # (height, name)
pairs.sort(reverse=True)           # sort by height descending
print([name for height, name in pairs])