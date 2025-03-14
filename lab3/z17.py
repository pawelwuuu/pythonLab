def silnia(n):
    if n == 0 or n == 1:
        return 1
    wynik = 1
    for i in range(2, n + 1):
        wynik *= i
    return wynik

# Test
print(silnia(5))
print(silnia(0))
