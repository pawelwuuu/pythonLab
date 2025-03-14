def sortuj_liste(lista, rosnaco=True):
    return sorted(lista, reverse=not rosnaco)

# Test
print(sortuj_liste([5, 2, 9, 1], rosnaco=True))
print(sortuj_liste([5, 2, 9, 1], rosnaco=False))
