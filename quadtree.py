clusterID = 0
xyID = {}

def lines (xy, SZ, JV):
    if len(xy) < 50:
        global clusterID, xyID
        for pt in xy:
            xyID[(pt[0],pt[1])] = clusterID
        clusterID += 1
    else:
        a1 = SZ
        a2 = ((JV[0] + SZ[0]) / 2, SZ[1])
        a3 = (SZ[0], (JV[1] + SZ[1]) / 2)
        a4 = ((JV[0] + SZ[0]) / 2, (JV[1] + SZ[1]) / 2)
        b1 = ((JV[0] + SZ[0]) / 2, (JV[1] + SZ[1]) / 2)
        b2 = (JV[0], (JV[1] + SZ[1]) / 2)
        b3 = ((JV[0] + SZ[0]) / 2, JV[1])
        b4 = JV
        q1 = []
        q2 = []
        q3 = []
        q4 = []

        for pt in xy:
            if pt[0] >= a1[0] and pt[0] <= b1[0] and pt[1] >= b1[1] and pt[1] <= a1[1]:
                q1.append(pt)
            elif pt[0] >= a2[0] and pt[0] <= b2[0] and pt[1] >= b2[1] and pt[1] <= a2[1]:
                q2.append(pt)
            elif pt[0] >= a3[0] and pt[0] <= b3[0] and pt[1] >= b3[1] and pt[1] <= a3[1]:
                q3.append(pt)
            elif pt[0] >= a4[0] and pt[0] <= b4[0] and pt[1] >= b4[1] and pt[1] <= a4[1]:
                q4.append(pt)
        lines(q1, a1, b1)
        lines(q2, a2, b2)
        lines(q3, a3, b3)
        lines(q4, b1, b4)

def bbox(xy):
    coordinateX = []
    for f in xy:
        coordinateX.append(f[0])

    coordinateY = []
    for f in xy:
        coordinateY.append(f[1])

    maxX = max(coordinateX)
    minX = min(coordinateX)
    maxY = max(coordinateY)
    minY = min(coordinateY)
    return (minX, maxY), (maxX, minY)

def build_quadtree(xy):
    SZ, JV = bbox(xy)
    lines(xy, SZ, JV)
    return xyID


