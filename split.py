from quadtree import build_quadtree
import json, os.path


#   Funkce načte soubor input.geojson (ošetřeny chybné vstupy)
def load_file(json_file):
    if os.path.isfile(json_file):
        try:  # Zkus otevřít soubor
            with open(json_file, "r", encoding="utf-8") as f:
                data = json.load(f)

        except Exception as error:
            print(error)
            print("Soubor " + json_file + " je poškozený, nebo se nejedná o korektní geojson.")
            exit(1)
    else:
        print("Soubor " + json_file + " neexistuje!")
        exit(1)

    return data

#   Funkce pro načtení jednotlivých souřadnic bodů
def extract_coordinates(data):
    coordinates = []
    for feature in data['features']:
        xy = feature['geometry']['coordinates']
        coordinates.append(xy)

    return coordinates

#   Funkce pro přiřazení příslušné clusterID
def add_ID(data, xyID):
    for f in data['features']:
        xy = f['geometry']['coordinates']
        f['properties']['clusterID'] = xyID[tuple(xy)]

    return data

#   Spouštení jednotlivých funkcí
data = load_file("input.geojson")
coordinates = extract_coordinates(data)
xyID = build_quadtree(coordinates)
print(xyID) # kontrolní tisk, zda se clusterID přiřadila správně
final_ID = add_ID(data,xyID)

#   Uložení souboru
with open("output.geojson", "w", encoding="utf-8") as f:
    json.dump(final_ID, f, indent=2)

