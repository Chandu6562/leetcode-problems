# Widest Vertical Area Between Two Points Containing No Points
'''Given n points on a 2D plane where points[i] = [xi, yi], Return the widest vertical area between two points such that no points are inside the area.

A vertical area is an area of fixed-width extending infinitely along the y-axis (i.e., infinite height). The widest vertical area is the one with the maximum width.

Note that points on the edge of a vertical area are not considered included in the area.'''

# points = [[8,7],[9,9],[7,4],[9,7]]
points = [[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]
x_coords=[]
for i in range(len(points)):
    x_coords.append(points[i][0])
x_coords.sort()
res=0
for j in range(1,len(x_coords)):
    res=max(x_coords[j]-x_coords[j-1],res)
print(res)