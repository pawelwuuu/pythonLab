a = 1
b = 2
c = 3

lista = (a,b,c)

maxx = -999
for liczba in lista:
    if liczba > maxx:
        maxx = liczba
        
print(maxx)
