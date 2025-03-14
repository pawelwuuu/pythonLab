import math

def oblicz_odleglosc(P1, P2):
    x1, y1 = P1
    x2, y2 = P2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def czy_wspolliniowe(P1, P2, P3):
    x1, y1 = P1
    x2, y2 = P2
    x3, y3 = P3
    return (x2 - x1) * (y3 - y1) == (x3 - x1) * (y2 - y1)


def obwod_trojkata(P1, P2, P3):
    if czy_wspolliniowe(P1, P2, P3):
        print("Punkty są współliniowe, nie tworzą trójkąta.")
        return 0
    a = oblicz_odleglosc(P1, P2)
    b = oblicz_odleglosc(P2, P3)
    c = oblicz_odleglosc(P3, P1)
    return a + b + c
