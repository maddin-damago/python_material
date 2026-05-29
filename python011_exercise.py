orte = ["Amsterdam", "Paris", "Rom", "Paris", "Brüssel", "Paris"]

# Amsterdamm vorhanden
print("Amsterdam" in orte)

# Amsterdamm vorhanden 2.
for ort in orte:
    if ort == "Amsterdam":
        print(True)

# Häufigkeit Paris
print(orte.count("Paris"))

# ort, der am häufgsten in der Liste ist: statisch
countParis = orte.count("Paris")
countAmsterdam = orte.count("Amsterdam")
countRom = orte.count("Rom")
countBruessel = orte.count("Brüssel")

orteDictionary = {
    "Paris": countParis,
    "Amsterdam": countAmsterdam,
    "Rom": countRom,
    "Brüssel": countBruessel,
}

count = 0
for ort in orteDictionary:
    if orteDictionary[ort] > count:
        count = orteDictionary[ort]

# clasht aber, wenn 2 orte gleich oft vorkommen
for ort in orteDictionary:
    if orteDictionary[ort] == count:
        print("Ort, der am häufigsten vorkommt: ", ort)

# ort, der am häufgsten in der Liste ist: dynamisch

orte = ["Amsterdam", "Paris", "Rom", "Paris", "Brüssel", "Paris"]

orteDict = {}

for ort in orte:
    if ort in orteDict:
        orteDict[ort] +=1
    else:
        orteDict[ort] = 1

print(orteDict)

highestCount = max(orteDict, key=orteDict.get)

print("Ort, der am häufigsten vorkommt: ", highestCount)
