# Sort the Students by Their Kth Score
'''There is a class with m students and n exams. You are given a 0-indexed m x n integer matrix score,
where each row represents one student and score[i][j] denotes the score the ith student got in the jth exam. 
The matrix score contains distinct integers only.

You are also given an integer k. Sort the students (i.e., the rows of the matrix) by their 
scores in the kth (0-indexed) exam from the highest to the lowest.

Return the matrix after sorting it.'''

score = [[10,6,9,1],[7,5,11,2],[4,8,3,15]]
k=2
n = len(score)
for i in range(n):
    max_idx = i
    for j in range(i + 1, n):
        if score[j][k] > score[max_idx][k]:
            max_idx = j
    score[i], score[max_idx] = score[max_idx], score[i]
print(score)
    