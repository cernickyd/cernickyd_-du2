from quadtree import bbox
import json, os.path

#   Funkce pro otoevření souboru .geojson
def load_file(json_file):
    if os.path.isfile(json_file):
        try:    # Zkus otevřít soubor
            with open(json_file, "r", encoding="utf-8") as f:
                data = json.load(f)
        except FileExistsError:
            print("Soubor " + json_file + " je poškozený, nebo se nejedná o korektní geojson.")
            exit()
    else:
        print("Soubor " + json_file + " neexistuje!")
        exit()
    return data

#   Funkce pro načtení souřadnic z geojson
def load_xy(data):
    coordinates = []    # seznam pro zapisování souřadnic
    for f in data['features']:
        xy = f['geometry']['coordinates']
        coordinates.append(xy)
    #print(xy)
    return coordinates

data = load_file("export.geojson")
#print(data)

coordinates = load_xy(data)
print(coordinates)

hm = bbox(data)