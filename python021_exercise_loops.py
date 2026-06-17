"""
Aufgabe 1: Ausgeben einer Liste mit Hilfe einer Schleife

Folgende Liste ist gegeben:

stadtteile = ["Kreuzberg", "Lichtenberg", "Wilmersdorf", "Tegel"]

a) Benutze eine while-Schleife, um alle Elemente der Liste nacheinander auszugeben.

   Ausgabe:

   Kreuzberg
   Lichtenberg
   Wilmersdorf
   Tegel

b) Benutze eine while-Schleife, um alle Elemente der Liste nacheinander in umgekehrter 
   Reihenfolge auszugeben.

   Ausgabe:

   Tegel
   Wilmersdorf
   Lichtenberg
   Kreuzberg

c) Benutze eine while-Schleife, um alle Elemente der Liste nacheinander auszugeben.
   Hierbei soll keine Ausgabe erfolgen, wenn das Listenelement den Wert "Wilmersdorf" 
   hat. Unterbreite zwei Vorschläge zur Lösung.

   Ausgabe:

   Kreuzberg
   Lichtenberg
   Tegel

d) Benutze eine for-Schleife, um alle Elemente der Liste nacheinander auszugeben.
   Hierbei sollen alle Aktionen des Schleifendurchlaufs abgebrochen werden, wenn das
   Listenelement mit dem Buchstaben "K" beginnt.

   Ausgabe:

   Lichtenberg
   Wilmersdorf
   Tegel

e) Benutze eine for-Schleife, um alle Elemente der Liste nacheinander auszugeben.
   Hierbei soll die gesamte Ausführung der Schleife nach dem zweiten Element 
   abgebrochen werden.

   Ausgabe:

   Kreuzberg
   Lichtenberg
"""

stadtteile = ["Kreuzberg", "Lichtenberg", "Wilmersdorf", "Tegel"]

# a)

counter = len(stadtteile)
index = 0

while counter > 0:
    print(stadtteile[index])
    counter -= 1
    index += 1
    print(counter, index)

# destruktiv
while stadtteile:
    print(stadtteile.pop(0))

# b)
stadtteile = ["Kreuzberg", "Lichtenberg", "Wilmersdorf", "Tegel"]

counter = len(stadtteile)

while counter > 0:
    print(stadtteile[counter-1])
    counter -= 1

# destruktiv
while stadtteile:
    print(stadtteile.pop())

# c)
stadtteile = ["Kreuzberg", "Lichtenberg", "Wilmersdorf", "Tegel"]

counter = len(stadtteile)
index = 0

while counter > 0:
    if stadtteile[index] != "Wilmersdorf":
        print(stadtteile[index])
    counter -= 1
    index += 1
    print(counter, index)

# destruktiv
while stadtteile:
    if stadtteile[index] == "Wilmersdorf":
        stadtteile.pop(0)
    print(stadtteile.pop(0))

# d)
stadtteile = ["Kreuzberg", "Lichtenberg", "Wilmersdorf", "Tegel"]

for i in range(len(stadtteile)):
    if "K" in stadtteile[i]:
        continue
    print(stadtteile[i])

for i in range(len(stadtteile)):
    if i == 2:
        break
    print(stadtteile[i])
