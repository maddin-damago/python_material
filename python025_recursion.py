"""
Übungsblatt 5 - Rekursion

Aufgabe 1

Eine Fibonacci-Zahl berechnet sich aus der Summe der vorherigen
mit der vor-vorherigen Fibonacci-Zahl wie folgt:

     Fib(n) = Fib(n - 2) + Fib(n - 1)

Definiert sind ebenso die beiden Werte Fib(1) = 0 und Fib(2) = 1.
Somit ergeben die Fibonacci-Zahlen die Werte 0, 1, 1, 2, 3, 5 etc.

a) Schreibe eine rekursive Funktion Fib() mit n als Parameter, die 
   die n-te Fibonacci-Zahl errechnet.

b) Schreibe eine Funktion FibSum() mit n als Parameter, die die Summe
   aller Fibonacci-Zahlen von 1 bis n errechnet.
"""


def Fib(n: int) -> int:
    if n < 1:
        return 0
    if n == 2:
        return 1
    return Fib(n - 2) + Fib(n - 1)


print(Fib(10))


def FibSum(n: int) -> int:
    if n < 1:
        return 0
    if n == 2:
        return 1
    return Fib(n) + Fib((n + 1)) - 1


print("Summe:", FibSum(9))


"""
Aufgabe 2

Eine Zeichenkette soll in Spiegelschrift wieder ausgegeben werden,
sprich: von rechts nach links wie folgt:

     Berlin -> nilreB

Vervollständige den nachfolgenden Funktionsrumpf, so dass eine 
rekursive Funktion zur Erzeugung einer Spiegelung entsteht:
"""


# def spiegelschrift(zeichenkette: str) -> str:
#     ergebnis = ""
#     if len(zeichenkette) == 0:
#         return ergebnis
#     ergebnis = ergebnis + zeichenkette[0]
#     neueZeichenkette = zeichenkette[1:]
#     return ergebnis + spiegelschrift(neueZeichenkette)
# # ALMOST: it needs to be: return spiegelschrift(neueZeichenkette) + ergebnis

def spiegelschrift(zeichenkette: str) -> str:
    # Base case
    if len(zeichenkette) == 0:
        return ""

    # Recursive case: notice we put the first character at the END
    return spiegelschrift(zeichenkette[1:]) + zeichenkette[0]


zeichenkette = "Berlin"
gespiegelt = spiegelschrift(zeichenkette)
print(gespiegelt)
