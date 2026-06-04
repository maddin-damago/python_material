import math
from typing import TypedDict
from datetime import datetime, timedelta

# 1. Define the "Interface"
class Route(TypedDict):
    von: str
    nach: str
    distanz: int
    zugtyp: str
    abfahrt: str 
    ankunft: str

# gib jeden Streckenabschnitt in der Form "von -> nach (Distanz km mit Zugtyp)" aus
# bestimme die kürzeste Strecke
# bestimme die längste Strecke
# bestimme die durchschnittliche Streckenlänge
# wird ein Streckenabschnitt mit dem TGV zurückgelegt
# wird ein Streckenabschnitt mit dem Thalys zurückgelegt
# wieviele Streckenabschnitte werden mit dem ICE zurückgelegt
# bestimme die Fahrzeit von Lyon nach Frankfurt (Main)

routen: list[Route] = [
    {"von":"Montpellier", "nach":"Lyon", "distanz":303, "zugtyp":"TGV", "abfahrt":"6:25", "ankunft":"8:24"},
    {"von":"Lyon", "nach":"Strasbourg", "distanz":495, "zugtyp":"TGV", "abfahrt":"8:32", "ankunft":"12:24"},
    {"von":"Strasbourg", "nach":"Frankfurt (Main)", "distanz":218, "zugtyp":"TGV","abfahrt":"13:09", "ankunft":"14:56"},
    {"von":"Frankfurt (Main)", "nach":"Leipzig", "distanz":400, "zugtyp":"ICE", "abfahrt":"15:19", "ankunft":"18:31"},
    {"von":"Leipzig", "nach":"Berlin Südkreuz", "distanz":180, "zugtyp":"RE", "abfahrt":"18:51", "ankunft":"20:31"}
]

# gib jeden Streckenabschnitt in der Form "von -> nach (Distanz km mit Zugtyp)" aus
for route in routen:
    print(f"{route["von"]} -> {route["nach"]} ({route["distanz"]} km mit {route["zugtyp"]})")

# bestimme die kürzeste Strecke
kuerzesteStrecke = routen[0]
for route in routen:
    if route["distanz"] < kuerzesteStrecke["distanz"]:
         kuerzesteStrecke = route
print(kuerzesteStrecke)

# bestimme die längste Strecke
laengsteStrecke = routen[0]
for route in routen:
    if route["distanz"] > laengsteStrecke["distanz"]:
         laengsteStrecke= route
print(laengsteStrecke)

# bestimme die durchschnittliche Streckenlänge
def getTotalDistance(routen: list[Route]) -> int:
    gesamtlaenge: int = 0
    for route in routen:
        gesamtlaenge += route["distanz"]

    return gesamtlaenge

print(f"Durchschnitt: {getTotalDistance(routen) / len(routen)} km")

def getDistance(strecke: Route):
    return strecke["distanz"]

print(getDistance(routen[3]))

# wird ein Streckenabschnitt mit dem TGV zurückgelegt
def isTGV(routen: list[Route]):
    for route in routen:
        if route["zugtyp"].lower() == "tgv":
            return True
    return False
print(isTGV(routen))

# wird ein Streckenabschnitt mit dem Thalys zurückgelegt
def isThalys(routen: list[Route]):
    for route in routen:
        if route["zugtyp"].lower() == "thalys":
            return True
    return False
print(isThalys(routen))

# def isTGV(routen: list[Route]):
#     gefunden = any(route["zugtyp"].lower() == "tgv" for route in routen)
#     return gefunden

# print(isTGV(routen))

# wieviele Streckenabschnitte werden mit dem ICE zurückgelegt
def streckenMitICE(routen: list[Route]):
    anzahl = 0
    for route in routen:
        if route["zugtyp"].lower() == "ice":
            anzahl += 1
    return anzahl

print(streckenMitICE(routen))

# bestimme die Fahrzeit von Lyon nach Frankfurt (Main)
def ermittleReisezeit(routen: list[Route]):
    abfZeit: str = ""
    ankZeit: str = ""
    for route in routen:
        if route["von"] == "Lyon":
            abfZeit = route["abfahrt"]
        if route["nach"] == "Frankfurt (Main)":
            ankZeit = route["ankunft"] 

    zeit1 = datetime.strptime(abfZeit, "%H:%M")
    zeit2 = datetime.strptime(ankZeit, "%H:%M")

    return zeit2 - zeit1

print("Die gesamte Reisezeit beträgt:", ermittleReisezeit(routen))

# durchschnittliche geschwindigkeit
zeit1 = datetime.strptime(routen[0]["abfahrt"], "%H:%M")
zeit2 = datetime.strptime(routen[4]["ankunft"], "%H:%M")

gesamtZeit: timedelta = zeit2 - zeit1

gesamtDistanz: int = 0
for route in routen:
    gesamtDistanz += route["distanz"]

durchschnittsGeschwindigkeit = gesamtDistanz // (gesamtZeit.total_seconds() / 3600)

print("Die Durchschnittsgeschwindigkeit ist:", durchschnittsGeschwindigkeit, "km/h")

# Zusatzaufgabe 2:
# Die Rückfahrt erfolgt mit dem Fahrrad, max. 100 km pro Tag. 

# * In wieviele Etappen ist die Strecke zu unterteilen?
# * Eine Übernachtung kostet EUR 85. Welches Budget ist für die Rückfahrt einzuplanen?

etappen: int = math.ceil(gesamtDistanz / 100)
print("Bei einem Tageslimit von 100 km benötigen wir", etappen, "Etappen für eine Strecke von", gesamtDistanz, "km")
budget: int = etappen * 85
print("Für", etappen,"Etappen mit einem Tagesbudget von 85 EUR für Übernachtungen benötigen wir", budget,"EUR insgesamt")