import random

def gra_kamien_papier_nozyce():
    opcje = ["kamień", "papier", "nożyce"]
    komputer = random.choice(opcje)
    gracz = input("Wybierz (kamień, papier, nożyce): ").lower()
    
    if gracz not in opcje:
        return "Nieprawidłowy wybór!"
    
    print("Komputer wybrał:", komputer)
    
    if gracz == komputer:
        return "Remis!"
    elif (gracz == "kamień" and komputer == "nożyce") or \
         (gracz == "papier" and komputer == "kamień") or \
         (gracz == "nożyce" and komputer == "papier"):
        return "Wygrałeś!"
    else:
        return "Przegrałeś!"

# Test
print(gra_kamien_papier_nozyce())
