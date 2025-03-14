def szukajWLiscie(lista, a):
    wystapien = 0
    for e in lista:
        if e == a:
            wystapien += 1
            
    return wystapien

print(szukajWLiscie([1,2,3,4,1,1,3], 1))
