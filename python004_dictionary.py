addressDictionary = {
    1: {"plz": 10969, "name": "Kreuzberg"},
    2: {"plz": 12051, "name": "Neukölln"},
    3: {"plz": 12555, "name": "Köpenick"},
    4: {"plz": 10179, "name": "Charlottenburg"}
}

plzDictionary = {
    10969: "Kreuzberg",
    12051: "Neukölln",
    12555: "Köpenick",
    10179: "Charlottenburg",
}


# Dictionary durchloopen, "eintrag" ist in diesem Fall der "Key" (1, 2, 3, 4) des Dictionary Eintrags, in diesem befindet sich je Key
# ein weiteres Dictionary -> key mit ["keyname"] ansteuern
for eintrag in addressDictionary:
    addressDictionary[eintrag]["einwohnerzahl"] = 123456
    print(addressDictionary[eintrag]["plz"], addressDictionary[eintrag]["name"], addressDictionary[eintrag]["einwohnerzahl"])

for plz in plzDictionary:
    print(plz)
    print(plzDictionary[plz])


print(addressDictionary[1]["plz"], addressDictionary[1]["name"])

# keys und values des dictionary auslesen
print(addressDictionary.keys())
print(addressDictionary.values())

# Länge des dictionary auslesen
print(len(addressDictionary))

# dictionary inhalt löschen
plzDictionary.clear();
print(plzDictionary)