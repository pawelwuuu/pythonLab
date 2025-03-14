def szukajWLiscie(lista, a):
    if type(a) == int or type(a) == float:
        wystapien = 0
        for e in lista:
            if e == a:
                wystapien += 1

        return wystapien
    elif type(a) == str:
        try:
            a = int(a)
            wystapien = 0
            for e in lista:
                if e == a:
                    wystapien += 1

            return wystapien
        except:
            new = 0
            for c in a:
                new += ord(c)
            a = new
            wystapien = 0
            for e in lista:
                if e == a:
                    wystapien += 1

            return wystapien
    
    elif type(a) == bool:
        if a == True:
            a = 1
        else:
            a = 0
        
        wystapien = 0
        for e in lista:
            if e == a:
                wystapien += 1

        return wystapien
    else:
        raise TypeError()
    
        

print(szukajWLiscie([1,1,2,3,4,1.3,1.3,3.2], False))
