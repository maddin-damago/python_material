"""
Aufgabe 3: Funktionen schreiben und verstehen

Folgende Liste ist gegeben:

stadtteile = ["Kreuzberg", "Lichtenberg", "Wilmersdorf", "Tegel", "Mariendorf", "Schmargendorf"]

a) Die folgende Funktion namens findeStadtteile() besteht bereits als Programmcode:

   def findeStadtteile(listeDerStadtteile, gesuchterStadtteil):

       ergebnis = ()
       for stadtteil in listeDerStadtteile:
           if gesuchterStadtteil in stadtteil:
               ergebnis.append(gesuchterStadtteil)

   Korrigiere die Funktion so, dass ein Aufruf der Funktion diesen Rückgabewert liefert:

   Aufruf:

   ergebnis = findeStadtteile(Stadtteile, "dorf")
   print(ergebnis)

   Ausgabe:

   ["Wilmersdorf", "Mariendorf", "Schmargendorf"]

b) Schreibe eine Funktion gesamtsumme(), die als Parameter eine Liste von ganzen
   Zahlen entgegennimmt und als Rückgabewert die Summe der Zahlen übermittelt.

   Aufruf:

   ergebnis = gesamtsumme([12, 57, 3, 8, 10])
   print(ergebnis)

   Ausgabe:

   90

c) Folgende Postleitzahlen sind zusätzlich zur Liste stadtteile vorhanden:

   plz = [10967, 10365, 10719, 13503, 12107, 14193]

   Erstelle eine Funktion namens zuordnen(), die auf der Grundlage der Listen
   stadttteile und plz diese Ausgabe liefert:

   (10967, "Kreuzberg")
   (10365, "Lichtenberg")
   …
   (14193, "Schmargendorf")

   Gib die Ausgabe anhand der Postleitzahl aufsteigend sortiert aus.
"""
# a)

from functools import reduce


stadtteile = ["Kreuzberg", "Lichtenberg", "Wilmersdorf",
              "Tegel", "Mariendorf", "Schmargendorf"]


def findeStadtteile(listeDerStadtteile: list[str], gesuchterStadtteil: str):

    ergebnis: list[str] = []
    for stadtteil in listeDerStadtteile:
        if gesuchterStadtteil in stadtteil:
            ergebnis.append(stadtteil)

    return ergebnis


ergebnis = findeStadtteile(stadtteile, "dorf")
print(ergebnis)

# b)


def gesamtsumme(zahlenliste: list[int]):
    return reduce(lambda x, y: x + y, zahlenliste)


ergebnis = gesamtsumme([12, 57, 3, 8, 10])
print(ergebnis)

# c)

plz = [10967, 10365, 10719, 13503, 12107, 14193]


def zuordnen(stadtteilListe: list[str], plzListe: list[int]):
    ergebnisListe: list[tuple[int, str]] = []

    for i in range(len(stadtteilListe)):
        ergebnisListe.append((plzListe[i], stadtteilListe[i]))

    return sorted(ergebnisListe)


ergebnis = zuordnen(stadtteile, plz)

for item in ergebnis:
    print(item)
