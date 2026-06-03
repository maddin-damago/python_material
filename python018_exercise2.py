# gib jeden Streckenabschnitt in der Form "von -> nach (Distanz km mit Zugtyp)" aus
# bestimme die kürzeste Strecke
# bestimme die längste Strecke
# bestimme die durchschnittliche Streckenlänge
# wird ein Streckenabschnitt mit dem TGV zurückgelegt
# wird ein Streckenabschnitt mit dem Thalys zurückgelegt
# wieviele Streckenabschnitte werden mit dem ICE zurückgelegt
# bestimme die Fahrzeit von Lyon nach Frankfurt (Main)

routen = [
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

def getTotalDistance(route):
    gesamtlaenge = 0
    for route in routen:
        gesamtlaenge += route["distanz"]

    return gesamtlaenge

print(f"Durchschnitt: {getTotalDistance(routen) / len(routen)} km")

def getDistance(strecke):
    return strecke["distanz"]

print(getDistance(routen[3]))

# wird ein Streckenabschnitt mit dem TGV zurückgelegt
def isTGV(routen):
    for route in routen:
        if route["zugtyp"].lower() == "tgv":
            return True
    return False
print(isTGV(routen))
# wird ein Streckenabschnitt mit dem Thalys zurückgelegt
def isThalys(routen):
    for route in routen:
        if route["zugtyp"].lower() == "thalys":
            return True
    return False
print(isThalys(routen))

def isTGV(routen):
    gefunden = any(route["zugtyp"].lower() == "tgv" for route in routen)
    return gefunden

print(isTGV(routen))

# wieviele Streckenabschnitte werden mit dem ICE zurückgelegt
def streckenMitICE(routen):
    anzahl = 0
    for route in routen:
        if route["zugtyp"].lower() == "ice":
            anzahl += 1
    return anzahl

print(streckenMitICE(routen))

# bestimme die Fahrzeit von Lyon nach Frankfurt (Main)

