"""
Aufgabe 2: Verwenden einer Liste aus Dictionaries

Folgendes Dictionary ist gegeben:

artikel1 = {
    "id" : 1367,
    "beschreibung": "Einkaufstüte, blau, gebraucht",
    "preis" : 0.25
}

artikel2 = {
    "id" : 169,
    "beschreibung": "100g Kaffeesatz in Bio-Qualität",
    "preis" : 3.00
}

a) Ändere den Preis von artikel1 auf 0.45 und gib das Dictionary aus.

   Ausgabe:

   {"id": 1367, "Beschreibung": "Einkaufstüte, blau, gebraucht", "preis": 0.45}

b) Erstelle einen dritten Artikel artikel3 mit der Id 45, der Beschreibung "Tomate"
   und dem Preis 1.00 . Gib den Inhalt des neuen Artikels aus.

   Ausgabe:

   {"id": 45, "Beschreibung": "Tomate", "preis": 1.00}


c) Der Kunde A. Zitterbacke hat diese Einkaufsliste:

   einkaufsliste = [
       {"id": 45, "anzahl": 3},
       {"id", 1367, "anzahl": 1}
   ]

   Wieviel muss A. Zitterbacke an der Kasse für seinen Einkauf bezahlen?

   Ausgabe: 
   Einkaufspreis: 3.45 Goldstücke
"""
from typing import TypedDict


class Artikel(TypedDict):
    id: int
    beschreibung: str
    preis: float


artikel1: Artikel = {
    "id": 1367,
    "beschreibung": "Einkaufstüte, blau, gebraucht",
    "preis": 0.25
}

artikel2: Artikel = {
    "id": 169,
    "beschreibung": "100g Kaffeesatz in Bio-Qualität",
    "preis": 3.00
}

# a)
artikel1["preis"] = 0.45
print(artikel1)

# b)
artikel3: Artikel = {
    "id": 45,
    "beschreibung": "Tomate",
    "preis": 1.00
}
print(artikel3)

# c)


class Einkaufsliste(TypedDict):
    id: int
    anzahl: int

# searchable datastructure for products


class Produkt(TypedDict):
    beschreibung: str
    preis: float


produkte: dict[int, Produkt] = {
    1367: {
        "beschreibung": "Einkaufstüte, blau, gebraucht",
        "preis": 0.45
    },
    169: {

        "beschreibung": "100g Kaffeesatz in Bio-Qualität",
        "preis": 3.00
    },
    45: {

        "beschreibung": "Tomate",
        "preis": 1.00
    }
}


einkaufsliste: list[Einkaufsliste] = [
    {"id": 45, "anzahl": 3},
    {"id": 1367, "anzahl": 1}
]

gesamtSumme: float = 0

for item in einkaufsliste:
    gesamtSumme += produkte[item["id"]]["preis"] * item["anzahl"]

print("Einkaufspreis:", gesamtSumme, "Goldstücke")
