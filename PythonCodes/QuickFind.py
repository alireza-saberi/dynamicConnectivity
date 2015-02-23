def UF(N):
    for i in range(int(N)):
        point = {
            "number":i,
            "identity":i
            }
        points.append(point)
    return points
points = []
P = raw_input("Please enter number of points: ")
UF(P)

def connected(p,q):
    pointP = points[p]
    pointQ = points[q]
    return pointP["identity"] == pointQ["identity"]

def union(p,q):
    pointP = points[p]
    pointQ = points[q]
    pid = pointP["identity"]
    qid = pointQ["identity"]
    for point in points:
        if point["identity"] == pid:
           point["identity"] = qid 
    
print connected(0,1)
