import math

def oblicz_odleglosc(P1, P2):
    x1, y1 = P1
    x2, y2 = P2
    
    odleglosc = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    
    return odleglosc

P1 = [1, 2]
P2 = [4, 6]
print("Odległość między punktami P1 i P2 wynosi:", oblicz_odleglosc(P1, P2))
