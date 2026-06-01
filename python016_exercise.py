# Aufgabe a

from functools import reduce


stadtteile = ["Kreuzberg", "Lichtenberg", "Wilmersdorf", "Tegel", "Mariendorf", "Schmargendorf"]

def findeStadtteile(listeDerStadtteile, gesuchterStadtteil):

    ergebnis = []
    for stadtteil in listeDerStadtteile:
        if gesuchterStadtteil in stadtteil:
            ergebnis.append(stadtteil)
    return ergebnis  

        
ergebnis = findeStadtteile(stadtteile, "dorf")
print(ergebnis)

# Ausgabe:

["Wilmersdorf", "Mariendorf", "Schmargendorf"]

# Aufgabe b
def gesamtsumme(zahlenliste):
    return reduce(lambda x, y: x+y, zahlenliste)

ergebnis = gesamtsumme([12, 57, 3, 8, 10])
print(ergebnis)

# Aufgabe c

plz = [10967, 10365, 10719, 13503, 12107, 14193]

def zuordnen(stadteilListe, plzListe):
    map = []

    for i in range(len(stadteilListe)):
        map.append((plzListe[i], stadteilListe[i]))

    return sorted(map)

print(zuordnen(stadtteile, plz))