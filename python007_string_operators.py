var1 = "Hallo aus"
var2 = "Berlin"
var3 = 3

concatenation = var1 + var2
print(concatenation)

stringProdukt = var1 * var3
print(stringProdukt)

ort = "Strasbourg"
print("a" in ort)

staedte = ["Berlin", "Karslruhe", "Freiburg"]
print("Berlin" in staedte)
print("Hamburg" not in staedte)

staedte = ["Berlin", "Erfurt", "Freiburg", "Oer-Erkenschwiek"]
print("er" in staedte)

for ort in staedte:
    print("er" in ort)

ort = "Bordeaux"
print(ort[0]) # am index
print(ort[3])
print(ort[2:6]) # von bis
print(ort[:4]) # von anfang bis index
print(ort[-4]) # -4ter index von hinten
print(ort[-6:-3]) # von bis von hinten