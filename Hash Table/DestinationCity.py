# estination City

'''You are given the array paths, where paths[i] = [cityAi, cityBi] means there exists a direct path going from cityAi to cityBi.
Return the destination city, that is, the city without any path outgoing to another city.

It is guaranteed that the graph of paths forms a line without any loop, therefore, there will be exactly one destination city.'''

# paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
# paths = [["B","C"],["D","B"],["C","A"]]

# starting_city = set()
# for cityA,cityB in paths:
#     starting_city.add(cityA)

# for cityA, cityB in paths:
#     if cityB not in starting_city:
#         print(cityB)

paths = [["B","C"],["D","B"],["C","A"]]
l1=[]
l2=[]

for i in range(len(paths)):
    l1.append(paths[i][0])
    l2.append(paths[i][1])
    
for i in range(len(l1)):
    if l2[i] not in l1:
        print(l2[i])