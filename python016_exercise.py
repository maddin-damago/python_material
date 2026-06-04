from functools import reduce

# Aufgabe a
stadtteile = ["Kreuzberg", "Lichtenberg", "Wilmersdorf", "Tegel", "Mariendorf", "Schmargendorf"]

def findeStadtteile(listeDerStadtteile: list[str], gesuchterStadtteil: str) -> list[str]:

    ergebnis: list[str] = []
    for stadtteil in listeDerStadtteile:
        if gesuchterStadtteil in stadtteil:
            ergebnis.append(stadtteil)
    return ergebnis  

ergebnis = findeStadtteile(stadtteile, "dorf")
print(ergebnis)

# Aufgabe b
def gesamtsumme(zahlenliste: list[int]) -> int:
    return reduce(lambda x, y: x + y, zahlenliste)

ergebnis = gesamtsumme([12, 57, 3, 8, 10])
print(ergebnis)

# Aufgabe c
plz = [10967, 10365, 10719, 13503, 12107, 14193]

def zuordnen(stadteilListe: list[str], plzListe: list[int]) -> list[tuple[int, str]]:
    map: list[tuple[int, str]] = []

    for i in range(len(stadteilListe)):
        map.append((plzListe[i], stadteilListe[i]))

    return sorted(map)

zugeordnet = zuordnen(stadtteile, plz)

for pair in zugeordnet:
    print(pair)