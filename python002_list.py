# import keyword
# import math

# print(keyword.kwlist)
# for e in dir(math):
#     print(e, end=" ")

orte = ["Berlin", "Potsdam", "München"] 

# index basierter loop
for i in range(len(orte)):
    print(i)
    print(orte[i])

leereListe = []

stadtteileNorden = ["Pankow", "Reinickendorf", "Wedding"]
stadtteileSueden = ["Schöneberg", "Tempelhof"]
stadtteileBerlin = stadtteileNorden + stadtteileSueden
print(stadtteileBerlin)

# überprüfe, o element in Liste vorhanden
istDabei = "Kreuzberg" in stadtteileBerlin
print(istDabei)
istDabei = "Pankow" in stadtteileBerlin
print(istDabei)

# einzelnes Element anhängen, 2 Varianten
stadtteileBerlin += ["Kreuzberg"]
stadtteileBerlin.append("Zehlendorf")
print(stadtteileBerlin)

# Liste von Elementen anhängen
stadtteileBerlin.extend(["Dahlem", "Lichtenrade", "Lichterfelde"])
print(stadtteileBerlin)

# einfügen an bestimmtem Index
stadtteileBerlin.insert(0, "Charlottenburg")
print(stadtteileBerlin)

# entfernen per wert/value
stadtteileBerlin.remove("Wedding")
print(stadtteileBerlin)

# letztes Element entfernen mit .pop() oder beliebiges mit .pop(index)
stadtteileBerlin.pop()
stadtteileBerlin.pop(0)
print(stadtteileBerlin)

# index eines bestimmten elements herausfinden
position = stadtteileBerlin.index("Zehlendorf")
print(position)

# anzahl eines bestimmten Elements in der Liste
anzahlStadteil = stadtteileBerlin.count("Lichtenrade")
print(anzahlStadteil)

# Liste sortieren aufsteigend
stadtteileBerlin.sort()
print(stadtteileBerlin)

# Liste umdrehen
stadtteileBerlin.reverse()
print(stadtteileBerlin)

postleitzahlen = [10179, 12555, 12051, 13089, 12309, 12305]
postleitzahlen.sort()
print(postleitzahlen)

addressbuch = [
    [10179, "Charlottenburg"],
    [12555, "Köpenick"],
    [12051, "Neukölln"],
]

for i in range(len(addressbuch)):
    plz, stadtteil = addressbuch[i]
    print(plz, stadtteil)