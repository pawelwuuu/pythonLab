import math

def oblicz_odleglosc(P1, P2):
    x1, y1 = P1
    x2, y2 = P2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def obwod_trojkata(P1, P2, P3):
    a = oblicz_odleglosc(P1, P2)
    b = oblicz_odleglosc(P2, P3)
    c = oblicz_odleglosc(P3, P1)
    return a + b + c
