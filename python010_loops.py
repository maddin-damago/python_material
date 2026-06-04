# import time

stadtbezirke = ["Schwabing", "Solln", "Sendling", "Moosach"]

# mit zähler i und dann liste[index]
for i in range(len(stadtbezirke)):
    print(stadtbezirke[i])

# mit wert direkt in der iterationsvariable
for bezirk in stadtbezirke:
    print(bezirk)

for bezirk in stadtbezirke:
    if bezirk.startswith("S"):
        print(bezirk)

# startwert, endwert und schrittweite, in diesem fall von 5 bis (aber nicht inklusive) 0 mit der schrittweite -1
# for i in range(5, 0, -1):
#     print(i)
#     time.sleep(1)
# print("BOOOOOOOM")

for i in range(1,21):
    if i % 4 == 0:
        print(i)

# while loop

ort = "Berlin"
counter = 0

while ort == "Berlin":
    print(counter)
    counter += 1

    if counter > 10:
        ort = "Leipzig"

elIdx = 0
while elIdx < len(stadtbezirke):
    print(stadtbezirke[elIdx], "ist ein Bezirk in München")
    elIdx += 1
print("Schleife beendet")

# rückwärts ausgeben
elIdx = len(stadtbezirke) - 1
while elIdx >= 0:
    print(stadtbezirke[elIdx], "ist ein Bezirk in München")
    elIdx -= 1
print("Schleife beendet")

# rückwärts ausgeben, danach ist die Liste aber leer
while len(stadtbezirke):
    name = stadtbezirke.pop()
    print(name, "ist ein Bezirk in München")

# stadtbezirke.reverse() dreht die Liste auch um