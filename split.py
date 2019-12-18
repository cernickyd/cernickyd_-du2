from quadtree import build_quadtree
import json, os.path

def load_file(json_file):
    if os.path.isfile(json_file):
        while True:
            try:  # Zkus otevřít soubor
                with open(json_file, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    break
            except FileExistsError as error:
                print(error)
                print("Soubor " + json_file + " je poškozený, nebo se nejedná o korektní geojson.")
                exit()
    else:
        print("Soubor " + json_file + " neexistuje!")
        exit()

    return data

def load_xy(data):
    coordinates = []
    for feature in data['features']:
        xy = feature['geometry']['coordinates']
        coordinates.append(xy)

    return coordinates

def add_ID(data, xyID):
    for f in data['features']:
        xy = f['geometry']['coordinates']
        f['clusterID'] = xyID[(xy[0],xy[1])]

    return data

data = load_file("input.geojson")
coordinates = load_xy(data)
xyID = build_quadtree(coordinates)
print(xyID)
final_ID = add_ID(data,xyID)
with open("output.geojson", "w", encoding="utf-8") as f:
    json.dump(final_ID, f, indent=2)