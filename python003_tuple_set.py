# tuple - immutable
stadtteileBerlin = ("Kreuzberg", "Mitte")
print(stadtteileBerlin)
print(stadtteileBerlin[0])
# stadtteileBerlin[0] = "Schöneberg"
# print(stadtteileBerlin)

# set - random order, no doubles
stadtteileBerlin = {"Kreuzberg", "Kreuzberg", "Mitte", "Neukölln"}
print(stadtteileBerlin)

stadtteileBerlinListe = ["Kreuzberg", "Kreuzberg", "Mitte", "Neukölln"]
# remove doubles with conversion to set and back to list
stadtteileBerlinKeineDoppels = list(set(stadtteileBerlin))
print(stadtteileBerlinKeineDoppels)

