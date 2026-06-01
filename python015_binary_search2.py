daten = [45, 12, 67, 3, 89, 105, 46, 40, 33, 20]
zahl = 105

daten.sort()
print("Suche nach", zahl, "in sortierter Liste", daten)

def findeZahl(z, arr):
    links = 0
    rechts = len(arr) - 1

    while links <= rechts:
        positionMitte = (links + rechts) // 2
        if z == arr[positionMitte]: # Treffer
            return positionMitte 
        if z < arr[positionMitte]: # Zahl kleiner als Zahl an der Mitte; in der rechte Hälfte weitersuchen
            rechts = positionMitte - 1
        else: # Zahl größer als Zahl an der Mitte; in der linken Hälfte weitersuchen
            links = positionMitte + 1
    
    return -1

res = findeZahl(zahl, daten)

if res != -1:
    print("Zahl gefunden an Index", res)
else:
    print("Zahl nicht in der Liste gefunden")


def findeZahlRekursiv(z, arr):
    links = 0
    rechts = len(arr)
    print(arr)
    # wenn array leer, dann abbrechen
    if not arr:
        return -1 # alternativ return False

    positionMitte = (links + rechts) // 2
    if z == arr[positionMitte] : # Treffer
        return positionMitte # der index hat nichts mehr mit dem index des urpsrünglichen arrays zu tun, daher vlt einfach True and dieser Stelle zurückgeben für "gefunden" aber nicht wo
    elif z < arr[positionMitte]: # Zahl kleiner als Zahl an der Mitte; in der rechte Hälfte weitersuchen
        return findeZahlRekursiv(z, arr[links : positionMitte])
    elif z > arr[positionMitte]: # Zahl größer als Zahl an der Mitte; in der linken Hälfte weitersuchen
        return findeZahlRekursiv(z, arr[positionMitte + 1 : rechts])

res = findeZahlRekursiv(zahl, daten)
print(res)