def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

def fibonacci_generator(n: int):
    numbers = []
    for i in range(n):
        numbers.append(fibo(i))
        
    return numbers

print(fibonacci_generator(10))