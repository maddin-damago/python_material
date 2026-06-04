from functools import reduce


def addiere(zahl1: int, zahl2: int) -> int:
    return zahl1 + zahl2

print(addiere(3, 4)) # direkt ausführen und printen
summe = addiere(3, 4) # Ergebnis/return der Funktion in Varable zwischenspeichern
print(summe)


zahlenwerte = [12, 16, 34, 3, 8]

def addiereZahlenListe(zahlenListe: list[int]): # Funktionsüberladung, gleicher Name, andere Signatur
    summe = 0
    for zahl in zahlenListe:
        summe += zahl
    return summe

print(addiereZahlenListe(zahlenwerte))


summeListe = reduce(lambda x, y: x + y, zahlenwerte) # interne python Funktion zum zusammenrechnen der Werte einer Liste
print(summeListe)