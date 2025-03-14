def czy_wspolliniowe(P1, P2, P3):
    x1, y1 = P1
    x2, y2 = P2
    x3, y3 = P3
    return (x2 - x1) * (y3 - y1) == (x3 - x1) * (y2 - y1)
