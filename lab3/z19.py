import math

def rysuj_figure(figura, parametr):
    if figura == "koło":
        promien = parametr
        pole = math.pi * promien ** 2
        for i in range(2 * promien + 1):
            for j in range(2 * promien + 1):
                if (i - promien)**2 + (j - promien)**2 <= promien**2:
                    print("*", end="")
                else:
                    print(" ", end="")
            print()
        return pole
    elif figura == "kwadrat":
        bok = parametr
        pole = bok ** 2
        for i in range(bok):
            print("*" * bok)
        return pole

# Test
print("Pole koła:", rysuj_figure("koło", 5))
print("Pole kwadratu:", rysuj_figure("kwadrat", 4))
