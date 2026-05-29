stadtbezirke = ["Schwabing", "Solln", "Sendling", "Moosach"]

for bezirk in stadtbezirke:
    print(bezirk)
else: print("Loop vollständig durchlaufen") # <-- wird nur ausgeführt, wenn der loop nicht vorher abgebrochen wurde

for bezirk in stadtbezirke:
    pass # <-- überspringt die aktuelle Iteration ohne Effekt

for bezirk in stadtbezirke:
    continue # <-- geht in die nächste Iteration der Schleife
    print("Ich werde nicht mehr ausgeführt")

for bezirk in stadtbezirke:
    if bezirk == "Sendling":
        continue # <-- print statement wird nicht mehr ausgeführt; mit "pass" wird es noch ausgeführt
    print("Ich werde ausgeführt")