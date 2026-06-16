import re

daten = "Merlin der Zauberer lebt geheimnisvoll in Berlin"

muster = ".er.?lin.?"

if re.search(muster, daten):
    print(f"'{muster}' in '{daten}' gefunden")

ergebnisse = re.findall(muster, daten)

for eintrag in ergebnisse:
    print(eintrag)
