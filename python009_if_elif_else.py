ort = "Hamburg"

if ort == "Berlin":
    plz = 12345

# print(plz)

# if ort == "Berlin":
#     print("Dickes B")
# else:
#     print("Was könn' wir dafür wenn Euer Döner sch***e schmeckt?")

if ort == "Berlin":
    print("Dickes B")
elif ort == "Hamburg":
    print("Fischbrötchen")
else:
    print("Was könn' wir dafür wenn Euer Döner sch***e schmeckt?")


a = 5
b = 20
if a < b:
    print(a, "ist die kleinere Zahl")
else:
    print(b, "ist die kleinere Zahl")


# Ternary
print("a ist die kleinere Zahl" if a < b else "b ist WIRKLICH die kleinere Zahl")

# Match statt switch, kein "break"
match a:
    case 5:
        print("Wert ist 5")
    case 10:
        print("Wert ist 10")
    case _:
        print("Kein Treffer gefunden")

