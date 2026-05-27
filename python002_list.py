# import keyword
# import math

# print(keyword.kwlist)
# for e in dir(math):
#     print(e, end=" ")

orte = ["Berlin", "Potsdam", "München"] 

for i in range(len(orte)):
    print(i)
    print(orte[i])

leereListe = []

stadtteileNorden = ["Pankow", "Reinickendorf", "Wedding"]
stadtteileSueden = ["Schöneberg", "Tempelhof"]
stadtteileBerlin = stadtteileNorden + stadtteileSueden
print(stadtteileBerlin)
istDabei = "Kreuzberg" in stadtteileBerlin
print(istDabei)
istDabei = "Pankow" in stadtteileBerlin
print(istDabei)
stadtteileBerlin += ["Kreuzberg"]
stadtteileBerlin.append("Zehlendorf")
print(stadtteileBerlin)
stadtteileBerlin.extend(["Dahlem", "Lichtenrade", "Lichterfelde"])
print(stadtteileBerlin)
stadtteileBerlin.insert(0, "Charlottenburg")
print(stadtteileBerlin)
stadtteileBerlin.remove("Wedding")
print(stadtteileBerlin)
stadtteileBerlin.pop()
stadtteileBerlin.pop(0)
print(stadtteileBerlin)
position = stadtteileBerlin.index("Zehlendorf")
print(position)
anzahlStadteil = stadtteileBerlin.count("Lichtenrade")
print(anzahlStadteil)
stadtteileBerlin.sort()
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