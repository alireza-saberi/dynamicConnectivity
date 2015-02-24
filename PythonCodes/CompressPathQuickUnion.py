def UF(N):
    for i in range(int(N)):
        point = {
            "number":i,
            "identity":i
            }
        points.append(point)
    return points
def root(i):
    pointI = points[i]
    iid = pointI["identity"]
    while i != iid :
       pointI  = points[iid]
       i = pointI["identity"]
       pointI = points[i]
       iid = pointI["identity"]
       pointI  = points[iid]
       i = pointI["identity"]
       pointI = points[i]
       iid = pointI["identity"]
    return i

def connected(p,q):
    rootP = root(p)
    rootQ = root(q)
    return rootP == rootQ

def union(p,q):
    i = root(p)
    j = root(q)
    pointI = points[i]
    pointI["identity"] = j

points = []    
P = raw_input("Please enter number of points: ")
UF(P)
union(4,3)
print connected(4,3)
union(3,8)
union(6,5)
union(9,4)
union(2,1)
print connected(8,9)
print connected(5,4)
union(5,0)
union(7,2)
union(6,1)
union(7,3)
print connected(5,4)
