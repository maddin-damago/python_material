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

for eintrag in addressDictionary:
    addressDictionary[eintrag]["einwohnerzahl"] = 123456
    print(addressDictionary[eintrag]["plz"], addressDictionary[eintrag]["name"], addressDictionary[eintrag]["einwohnerzahl"])

for plz in plzDictionary:
    print(plz)
    print(plzDictionary[plz])


print(addressDictionary[1]["plz"], addressDictionary[1]["name"])

print(addressDictionary.keys())
print(addressDictionary.values())

print(len(addressDictionary))

plzDictionary.clear();
print(plzDictionary)