def dach(znak):
    print(f"  {znak*6}  ")
    print(f"{znak*10}")

def pietro(znak):
    print(f"{znak}  {znak*4}  {znak}")
    print(f"{znak}  {znak*4}  {znak}")
    print("----------")

def rysuj_dom(liczba_pieter, znak_dachu, znak_pietra):
    dach(znak_dachu)
    
    for _ in range(liczba_pieter):
        pietro(znak_pietra)

rysuj_dom(3, "#", "*")
