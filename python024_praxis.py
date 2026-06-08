from functools import reduce
from typing import Final, TypedDict
"""
Übungsblatt 4: Aufgaben zur Festigung

Aufgabe 1
---------

Das Hotel Blauer Elefant erhält eine Buchungsanfrage für eine Reisegruppe wie 
folgt:

15x Doppelzimmer, 3 Nächte, Einzelpreis EUR 70 pro Nacht
2x  Einzelzimmer, 2 Nächte, Einzelpreis EUR 55 pro Nacht

Alle Preise sind Nettopreise zzgl. 7% Umsatzsteuer plus Beherbungsabgabe 
von EUR 3.00 pro Person pro Aufenthalt.

Das Hotel hat eine Gesamtkapazität von 25 Zimmern -- 20 Doppelzimmer und 5 
Einzelzimmer. Davon sind gerade 6 Zimmer belegt -- 2 Doppelzimer und 4
Einzelzimmer.

a) Kann das Hotel die Anfrage positiv beantworten und alle Gäste beherbergen?

b) Welchen Umsatz würde das Hotel mit der Buchungsanfrage machen? 
"""


class ZimmerInformation(TypedDict):
    anzahl: int
    belegt: int
    frei: int
    ppn: int


class Buchung(TypedDict):
    anzahl: int
    naechte: int


UST: Final[float] = 0.07
BEHERBERGUNGSABGABE: Final[int] = 3


zimmerInfo: dict[str, ZimmerInformation] = {
    "einzelzimmer": {
        "anzahl": 5,
        "belegt": 4,
        "frei": 1,
        "ppn": 70
    },
    "doppelzimmer": {
        "anzahl": 20,
        "belegt": 2,
        "frei": 18,
        "ppn": 55
    }
}

buchung: dict[str, Buchung] = {
    "einzelzimmer": {
        "anzahl": 2,
        "naechte": 2
    },
    "doppelzimmer": {
        "anzahl": 15,
        "naechte": 3
    }
}


def buchungMoeglich(kundenBuchung: dict[str, Buchung], kapa: dict[str, ZimmerInformation]):
    eZ = kundenBuchung["einzelzimmer"]["anzahl"]
    dZ = kundenBuchung["doppelzimmer"]["anzahl"]

    return eZ <= kapa["einzelzimmer"]["frei"] and dZ <= kapa["doppelzimmer"]["frei"]


print(buchungMoeglich(buchung, zimmerInfo))


def berechneGesamtsummeBuchung(kundenBuchung: dict[str, Buchung], kapa: dict[str, ZimmerInformation]):
    gesamtEinzelzimmerNetto = kundenBuchung["einzelzimmer"]["anzahl"] * \
        kundenBuchung["einzelzimmer"]["naechte"] * \
        kapa["einzelzimmer"]["ppn"]
    gesamtEinzelzimmerBrutto = gesamtEinzelzimmerNetto + \
        (gesamtEinzelzimmerNetto * UST) + \
        (kundenBuchung["einzelzimmer"]["anzahl"] * BEHERBERGUNGSABGABE)
    gesamtDoppelzimmerNetto = kundenBuchung["doppelzimmer"]["anzahl"] * \
        kundenBuchung["doppelzimmer"]["naechte"] * \
        kapa["doppelzimmer"]["ppn"]
    gesamtDoppelelzimmerBrutto = gesamtDoppelzimmerNetto + \
        (gesamtEinzelzimmerNetto * UST) + \
        (kundenBuchung["doppelzimmer"]["anzahl"] * BEHERBERGUNGSABGABE)

    return gesamtEinzelzimmerBrutto + gesamtDoppelelzimmerBrutto


print(berechneGesamtsummeBuchung(buchung, zimmerInfo))

"""
Aufgabe 2
---------

Fritzchen darf einkaufen gehen und bekommt einen Einkaufszettel:

2x Gurken, 400g pro Gurke
2x Gläser Joghurt, 500g pro Glas
1x Tafel Schokolade, 85g
1x Gemischtes Eis, 1kg

Er hat einen Karton, mit dem er 2kg nach Hause tragen kann.

a) Kann er den gesamten Einkauf auf einmal alleine nach Hause tragen?

b) Welche Artikel wählt er von dem Einkaufszettel aus, damit der Karton 
   maximal gefüllt wird, sprich: möglichst viele Artikel auf einmal
   transportiert werden? Entwickle eine Strategie dazu, um das in einem
   Programm umzusetzen.

c) Sein Onkel Helmut begleitet ihn beim Einkauf. Entwickle ein Programm, 
   welches ermittelt, wie der Einkauf so verteilt wird, dass beide vom 
   Gewicht her möglichst gleich viel nach Hause tragen.
"""
MAX_TRAGE_KAPA: Final[float] = 2.0


class EinkaufItem(TypedDict):
    produktName: str
    gewichtInKg: float
    anzahl: int


einkauf: list[EinkaufItem] = [
    {
        "produktName": "Gurken",
        "gewichtInKg": 0.4,
        "anzahl": 2
    },
    {
        "produktName": "Glas Joghurt",
        "gewichtInKg": 0.5,
        "anzahl": 2
    },
    {
        "produktName": "Tafel Schokolade",
        "gewichtInKg": 0.085,
        "anzahl": 1
    },
    {
        "produktName": "Gemischtes Eis",
        "gewichtInKg": 1.0,
        "anzahl": 1
    }
]

# a)


def kannErDenGesamtenEinkaufAufEinmalAlleineNachHauseTragen(einkaufsZettel: list[EinkaufItem]):
    return reduce(lambda acc, item: acc +
                  item["gewichtInKg"] * item["anzahl"], einkaufsZettel, 0) <= MAX_TRAGE_KAPA


print(kannErDenGesamtenEinkaufAufEinmalAlleineNachHauseTragen(einkauf))

# b)


def maxKapaEinkaufszettel(einkaufsZettel: list[EinkaufItem]):
    maxKapaEinkauf: list[EinkaufItem] = []
    sortiertAbsteigend = sorted(
        einkaufsZettel, key=lambda item: item["gewichtInKg"], reverse=True)

    summe = 0
    for item in sortiertAbsteigend:
        if summe > MAX_TRAGE_KAPA:
            break
        if summe + item["gewichtInKg"] * item["anzahl"] <= MAX_TRAGE_KAPA:
            maxKapaEinkauf.append(item)
            summe += item["gewichtInKg"] * item["anzahl"]

    return maxKapaEinkauf


print("Max Kapa Einkauf:", maxKapaEinkaufszettel(einkauf))

# c)


def fairteilterEinkauf(einkaufsZettel: list[EinkaufItem]):
    maxKapaEinkaufFritchen: list[EinkaufItem] = []
    maxKapaEinkaufOnkelHelmut: list[EinkaufItem] = []

    sortiertAbsteigend = sorted(
        einkaufsZettel, key=lambda item: item["gewichtInKg"], reverse=True)

    summeFritchen = 0
    summeOnkelHelmut = 0
    itemZaehler = 1

    for item in sortiertAbsteigend:
        if itemZaehler % 2 != 0:
            if summeFritchen + item["gewichtInKg"] * item["anzahl"] <= MAX_TRAGE_KAPA:
                maxKapaEinkaufFritchen.append(item)
                summeFritchen += item["gewichtInKg"] * item["anzahl"]
                itemZaehler += 1
        else:
            if summeOnkelHelmut + item["gewichtInKg"] * item["anzahl"] <= MAX_TRAGE_KAPA:
                maxKapaEinkaufOnkelHelmut.append(item)
                summeOnkelHelmut += item["gewichtInKg"] * item["anzahl"]
                itemZaehler += 1

    print("Gewicht Fritchen:", summeFritchen)
    print("Gewicht Onkel Helmut:", summeOnkelHelmut)

    return {"fritchen": maxKapaEinkaufFritchen, "onkelHelmut": maxKapaEinkaufOnkelHelmut}


print(fairteilterEinkauf(einkauf))

# flattened


def fairteilterEinkaufFlattened(einkaufsZettel: list[EinkaufItem]):
    maxKapaEinkaufFritchen: list[EinkaufItem] = []
    maxKapaEinkaufOnkelHelmut: list[EinkaufItem] = []

    flattenedEinkaufsZettel: list[EinkaufItem] = []

    for item in einkaufsZettel:
        if item["anzahl"] == 1:
            flattenedEinkaufsZettel.append(item)
        else:
            originalAnzahl = item["anzahl"]
            item["anzahl"] = 1
            flattenedEinkaufsZettel.extend([item] * originalAnzahl)

    sortiertAbsteigend = sorted(
        flattenedEinkaufsZettel, key=lambda item: item["gewichtInKg"], reverse=True)

    print("flattened: ", sortiertAbsteigend)

    summeFritchen = 0
    summeOnkelHelmut = 0

    for item in sortiertAbsteigend:
        if summeFritchen + item["gewichtInKg"] <= MAX_TRAGE_KAPA:
            if summeFritchen <= summeOnkelHelmut:
                maxKapaEinkaufFritchen.append(item)
                summeFritchen += item["gewichtInKg"]
            else:
                maxKapaEinkaufOnkelHelmut.append(item)
                summeOnkelHelmut += item["gewichtInKg"]

        else:
            if summeOnkelHelmut + item["gewichtInKg"] <= MAX_TRAGE_KAPA:
                if summeOnkelHelmut <= summeFritchen:
                    maxKapaEinkaufOnkelHelmut.append(item)
                    summeOnkelHelmut += item["gewichtInKg"]
                else:
                    maxKapaEinkaufFritchen.append(item)
                    summeFritchen += item["gewichtInKg"]

    print("Gewicht Fritchen:", summeFritchen)
    print("Gewicht Onkel Helmut:", summeOnkelHelmut)

    return {"fritchen": maxKapaEinkaufFritchen, "onkelHelmut": maxKapaEinkaufOnkelHelmut}


amFairsten = fairteilterEinkaufFlattened(einkauf)

print("Fritzchen:", amFairsten["fritchen"])
print("Onkel Helmut:", amFairsten["onkelHelmut"])
