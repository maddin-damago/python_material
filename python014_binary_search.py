# Binary search teilt eine sortierte!! Liste in der Mitte und schaut
# ob der gesuchte Wert größer oder kleiner ist als die Mitte, schmeißt dann die
# nicht mehr benötigte Hälfte weg und teilt die noch vorhandene Hälfte wieder in der Mitte
# Auf diese Weise wird die gesamte Liste durchsucht
# da der zu durchsuchende Rest immer kleiner wird ist die Zeitkomplexität recht gut
# -> 0(log n); 
# im Vergleich zum Standard 0(n), der linear ist: die Liste wird von vorne nach hinten durchsucht (for loop),
# also je länger die Liste, desto (linear) länger dauert die Suche

# Beispiel von w3schools:

def binarySearch(arr: list[int], targetVal: int):
  left = 0 # erster index
  right = len(arr) - 1 # letzter index

  while left <= right:
    mid = (left + right) // 2 # mitte, obviously

    if arr[mid] == targetVal: # das wäre der Zeitpunkt des Treffers
      return mid

    if arr[mid] < targetVal: # wenn der gesuchte wert größer ist als die aktuelle mitte kann die linke seite der liste weg und der neue anfangsindex ist die alte mitte
      left = mid + 1
    else:
      right = mid - 1 # das gegenteil von oben

  return -1 # wert nicht gefunden; -1 ist so eine konvention für "nicht im array gefunden"

mylist = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
x = 11

result = binarySearch(mylist, x)

if result != -1:
  print("Found at index", result)
else:
  print("Not found") 