# from dataclasses import dataclass

# @dataclass
# class MyThingT:
#    name: str
#    desc: str

class MyThing:
    # immer statische Klassenvariable, gilt global für alle Instanzen
    instanceCounter: int = 0
    # Konvention mit __ bedeutet "private"
    __privateVar: str = "I am soooo encapsulated, lol"

    def __init__(self, name: str, desc: str):
        self.__name: str = name
        self.__desc: str = desc
        MyThing.instanceCounter += 1

    def getName(self) -> str:
        return self.__name

    def setName(self, name: str):
        self.__name = name

    def getDesc(self):
        return self.__desc

    def setDesc(self, desc: str):
        self.__desc = desc

    def __str__(self) -> str:
        return "Name: " + self.__name + " Desc: " + self.__desc


mt1 = MyThing("Maddin", "Itsumi")

print(mt1.getName())
print(mt1.getDesc())
print(mt1)

mt1.setName("Martin")
print(mt1.getName())

mt1.setDesc("Isch bin der")
print(mt1.getDesc(), mt1.getName(), "ne.")
print(mt1)

print(MyThing.instanceCounter)
# Pylance strict mode meckert, damit man darauf achtet, aber es lässt sich trotzdem erfolgreich ausführen
# Zugriff auf "private" Klassenvariable
print(mt1._MyThing__privateVar)  # type: ignore

mt1._MyThing__privateVar = "Got hacked yüay"  # type: ignore
print(mt1._MyThing__privateVar)  # type: ignore

# print(mt1.__dict__)
# print(dir(classmethod.__dict__))

"""
def sucheNachKennzeichen(kennzeichenAusschnitt, fahrzeugflotte):
    treffer = []
    for fz in fahrzeugflotte:
        if kennzeichenAusschnitt in fz.getKennzeichen():
            treffer.append(fz)
    return treffer

"""
