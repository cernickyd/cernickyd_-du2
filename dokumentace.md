# Úkol č. 2
Tento skript slouží k přiřazení unikátního kódu skupiny bodům, na základě jejich polohy určené pomocí metody Quadtree.
Soubor output.geojson lze posléze otevřít v QGIS, kde jsou jednotlivé body rozrařeny podle atributu `clusterID`.

## Vstupní data
- hlavním vstupem je soubor `input.geojson`, který obsahuje informmaci o poloze bodu
- pokud program zjistí, že soubor neexistuje nebo je poškozený, vyřeší výjimku a skončí

## Výstupní data
- výstupem je rovněž soubor `output.geojson`, který obsahuje v atributech nové pole `clusterID`

## Popis jednotlivých funkcí
- program má dva moduly - `split.py` a `quadtree.py`
- modul `split.py` řeší pouze načtení/uložení souboru a přiřazení `clusterID` do atributů
- modul `quadtree.py` řeší matematickou stránku věci, implementuje quadtree

#### load_file
- načte soubor `.geojson`
- ošetřeny chybné vstupy

#### load_xy
- funkce pro načtení jednotlivých souřadnic bodů

#### add_ID
- přiřadí bodů přislušné `clusterID`

#### lines
- rekurzivní funkce
1. Načte hranice z funkce `bbox`
2. Ohraniční obdélník (čtverec)
3. Pokud obdélník obsahuje více než 50 bodů, rozdělí ho na 4 stejné obdélníky
4. Pokud ne, obdélník dál nedělí a přiřadí mu ID
5. Funkce se opakuje dokud se nepřiřadí hodnota všem obdélníkům

#### bbox
- spočítá hranice bounding-boxů

#### build_quadtree
- funkce pro spuštení funkcí
- spouští funkci `bbox` a `lines`