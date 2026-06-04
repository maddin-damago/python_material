def levelCheck(level: int) -> str | AssertionError:
    if level < 1:
        raise AssertionError("Ungültiges Level")
    return ""

# print(levelCheck(-2))

import random

daten = [1, 2, 3] * 5
try:
    wert = random.randint(0, 20)
    print(daten[wert])
except NameError:
    print("Variable unbekannt")
except IndexError:
    print("Zugriff außerhalb der Liste (Index)")
except:
    print("Es ist ein unbekannter Fehler aufgetreten")
else:
    print("Hello from the else block")
finally:
    print("Fiiiinallyy here")


filehandle = open("ausgabedatei", "w")
try:
    filehandle.write("Beispieltext")
except:
    print("Fehler beim Schreiben in die Datei")
finally:
    filehandle.close()

try:
    with open("ausgabedatei", "r") as filehandle:
        inhalt = filehandle.readlines()
        print(inhalt)
except:
    print("Fehler beim Lesen der Datei")

import tempfile

with tempfile.NamedTemporaryFile(delete=False) as tf:
    print("Ausgabe in Datei:", tf.name)
    tf.write(b"irgendwas")
    tf.flush()