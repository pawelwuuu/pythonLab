# Napisz klasę Person z atrybutami imie i wiek, oraz metodą przedstaw_sie(), która wypisuje 
# "Mam na imię X i mam Y lat."
class Person():
    def __init__(self, imie, wiek):
        self.imie = imie
        self.wiek = wiek
        
    def przedstaw_sie(self):
        print(f"Mam na imię {self.imie} i mam {self.wiek} lat.")
        
Person("adam", 1).przedstaw_sie()