"""
Aufgabe 2

Eine Zeichenkette soll in Spiegelschrift wieder ausgegeben werden,
sprich: von rechts nach links wie folgt:

     Berlin -> nilreB

Vervollständige den nachfolgenden Funktionsrumpf, so dass eine 
rekursive Funktion zur Erzeugung einer Spiegelung entsteht:
"""


ergebnis = ""


def spiegelschrift(zeichenkette: str, erg: str):  # type: ignore
    if len(zeichenkette) == 0:
        return erg
    erg += zeichenkette[len(zeichenkette) - 1]
    neueZeichenkette = zeichenkette[0:-1]

    return spiegelschrift(neueZeichenkette, erg)  # type: ignore


zeichenkette = "Berlin"
gespiegelt = spiegelschrift(zeichenkette, ergebnis)  # type: ignore
print(gespiegelt)  # type: ignore
