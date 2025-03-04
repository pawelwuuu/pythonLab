#  Napisz funkcję prime_selector(numbers: list[int]), która przyjmuje listę liczb 
# całkowitych i zwraca nową listę zawierającą tylko liczby pierwsze

def is_prime(n: int):
    dzielniki = 0
    for i in range(1,n+1):
        if n % i ==0:
            dzielniki +=1
            
    return dzielniki == 2

def prime_selector(numbers: list[int]):
    return list(filter(lambda n: is_prime(n), numbers))

print(prime_selector([1,3,4,5,6,13,15,16]))