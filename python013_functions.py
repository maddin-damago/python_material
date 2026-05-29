from functools import reduce


def addiere(zahl1, zahl2):
    return zahl1 + zahl2

print(addiere(3, 4)) # direkt ausführen und printen
summe = addiere(3, 4) # Ergebnis/return der Funktion in Varable zwischenspeichern
print(summe)


zahlenwerte = [12, 16, 34, 3, 8]

def addiere(zahlenListe): # Funktionsüberladung, gleicher Name, andere Signatur
    summe = 0
    for zahl in zahlenListe:
        summe += zahl
    return summe

print(addiere(zahlenwerte))

def addiere(zahl1, zahl2): # wie man hier sieht, ist es Python aber auch egal, wenn es die gleiche Signatur ist. Es wird einfach die vorherige
                            # Funktion überschrieben, obwohl diese hier subtrahiert. Absolut horrend, aber dafür "dynamisch" :)
    return zahl1 - zahl2

summeListe = reduce(lambda x, y: x + y, zahlenwerte) # interne python Funktion zum zusammenrechnen der Werte einer Liste
print(summeListe)