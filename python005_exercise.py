einkaufszettel = {
    1: {"artikel": "Milch", "anzahl": 2, "einzelpreis": 1.00},
    2: {"artikel": "Butter", "anzahl": 2, "einzelpreis": 2.50},
    3: {"artikel": "Eier", "anzahl": 1, "einzelpreis": 3.00},
    4: {"artikel": "Kaffee 500g", "anzahl": 2, "einzelpreis": 8.00},
}

anzahlArtikel = 0
gesamtpreis = 0

for artikel in einkaufszettel:
    anzahlArtikel += einkaufszettel[artikel]["anzahl"]
    gesamtpreis += einkaufszettel[artikel]["einzelpreis"] * einkaufszettel[artikel]["anzahl"]

print("Anzahl Artikel:", anzahlArtikel)
print("Summe: ", gesamtpreis)
print("Durchschnittspreis pro Artikel", round(gesamtpreis / anzahlArtikel, 2))
