# print("Hello world")

# ort ="Kreuzberg"

# print(ort)

# postleitzahl = "10963"

# print(postleitzahl)

# print(postleitzahl, ort)

# print(postleitzahl, "-", ort)

# print(postleitzahl + ort)

# hausnummer = "30"
# versatz = "2"

# print(int(hausnummer) + int(versatz))

# ergebnis = True

# farben = ["rot", "blau", "gelb"]

# farben += ["grün"]

# for farbe in farben:
#     print(farbe)

# print(farben[2])

# for i in range(len(farben)):
#     print(farben[i])

# whichType1 = {ergebnis, postleitzahl, ort}
# whichType2 = (ergebnis, postleitzahl, farben)

# print(type(farben))
# print(type(whichType1))
# print(type(whichType2))

testZahl = 5
testZahl2 = testZahl
testZahl2 = 7

print(testZahl)
print(testZahl2)

print(isinstance(testZahl, int))

print(testZahl == 5)
print(testZahl == "5")

produktwert = 150
steuersatz = 20

print("Bruttopreis:", produktwert + (produktwert / 100 * 20))