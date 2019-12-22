#   Hlavní proměnné
clusterID = 0
xyID = {}

#   Rekurzivní funkce vytvoření obdélníků (více viz. dokumentace.md)
def lines (xy, NW, SE, xyID):
    global clusterID
    if len(xy) < 50:
        for pt in xy:
            xyID[tuple(pt)] = clusterID
        clusterID += 1
    else:
        #   Hraniční body bounding-box, pokud neni splněna předchozí podmínka
        a1 = NW
        a2 = ((SE[0] + NW[0]) / 2, NW[1])
        a3 = (NW[0], (SE[1] + NW[1]) / 2)
        a4 = ((SE[0] + NW[0]) / 2, (SE[1] + NW[1]) / 2)
        b1 = ((SE[0] + NW[0]) / 2, (SE[1] + NW[1]) / 2)
        b2 = (SE[0], (SE[1] + NW[1]) / 2)
        b3 = ((SE[0] + NW[0]) / 2, SE[1])
        b4 = SE
        #   Seznam pro každý kvadrant rozděleného bounding-boxu
        q1 = []
        q2 = []
        q3 = []
        q4 = []

        #   Cyklus, který kontroluje, zda je bod v či vně bounding-boxu
        for pt in xy:
            if pt[0] >= a1[0] and pt[0] <= b1[0] and pt[1] >= b1[1] and pt[1] <= a1[1]:
                q1.append(pt)
            elif pt[0] >= a2[0] and pt[0] <= b2[0] and pt[1] >= b2[1] and pt[1] <= a2[1]:
                q2.append(pt)
            elif pt[0] >= a3[0] and pt[0] <= b3[0] and pt[1] >= b3[1] and pt[1] <= a3[1]:
                q3.append(pt)
            elif pt[0] >= a4[0] and pt[0] <= b4[0] and pt[1] >= b4[1] and pt[1] <= a4[1]:
                q4.append(pt)
        lines(q1, a1, b1, xyID)
        lines(q2, a2, b2, xyID)
        lines(q3, a3, b3, xyID)
        lines(q4, b1, b4, xyID)

        return clusterID

#   Funkce pro spočítání hranic bounding-boxů
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

#   Spouštění předchozích funkcí
def build_quadtree(xy):
    NW, SE = bbox(xy)
    lines(xy, NW, SE, xyID)
    return xyID

