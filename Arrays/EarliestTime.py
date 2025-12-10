# Earliest Time to Finish One Task
'''You are given a 2D integer array tasks where tasks[i] = [si, ti].

Each [si, ti] in tasks represents a task with start time si that takes ti units of time to finish.

Return the earliest time at which at least one task is finished.'''

tasks = [[1,6],[2,3]]
min_time=float('inf')
for i in range(len(tasks)):
    min_time =min(sum(tasks[i]),min_time)
print(min_time)