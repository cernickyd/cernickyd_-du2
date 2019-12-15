import json, os.path

#   Funkce pro otoevření souboru .geojson
def load_file(json_file):
    if os.path.isfile(json_file):
        try:    # Zkus otevřít soubor
            with open(json_file, "r", encoding="utf-8") as f:
                file = json.load(f)
        except FileExistsError:
            print("Soubor " + json_file + " je poškozený, nebo se nejedná o korektní geojson.")
            exit()
    else:
        print("Soubor " + json_file + " neexistuje!")
        exit()
    return file

#   Funkce pro načtení souřadnic z geojson
def load_xy(file):
    coordinates = []    # seznam pro zapisování souřadnic
    for f in file['features']:
        xy = f['geometry']['coordinates']
        coordinates.append(xy)
    #print(xy)
    return coordinates

#   Funkce oddělí X a Y souřadnice od sebe a nejde jejich extrémy, které následně uloží
def bbox(coord):
    coordinateX = []
    for f in file['features']:
        coordinateX.append(f['geometry']['coordinates'][0])

    coordinateY = []
    for f in file['features']:
        coordinateY.append(f['geometry']['coordinates'][1])

    max_x = max(coordinateX)
    min_x = min(coordinateX)
    max_y = max(coordinateY)
    min_y = min(coordinateY)

    return max_x,min_x,max_y,min_y

file = load_file("export.geojson")
#print(file)

coordinates = load_xy(file)
#print(coordinates)

bbox(file)