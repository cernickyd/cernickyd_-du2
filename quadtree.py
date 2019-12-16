#   Funkce oddělí X a Y souřadnice od sebe a nejde jejich extrémy a vypočítá průměry které následně uloží
def bbox(data):
    coordinateX = []
    for f in data['features']:
        coordinateX.append(f['geometry']['coordinates'][0])

    coordinateY = []
    for f in data['features']:
        coordinateY.append(f['geometry']['coordinates'][1])
#   Maxima a minima
    max_x = max(coordinateX)
    min_x = min(coordinateX)
    max_y = max(coordinateY)
    min_y = min(coordinateY)
#   Střed bounding boxu
    mid_x = (max_x + min_x) / 2
    mid_y = (max_y + min_y) / 2
    print(mid_x,min_y)
    return (mid_x, mid_y)

def build_quadtree(file):
    cluster_ID = 0
    file_ID = {}
    mid_x, mid_y = bbox(file)
