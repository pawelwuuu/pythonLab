def round_number(n, treshold):
    if n < treshold:
        return n - n % 10
    else:
        return n + (10 - n%10)


def round_numbers(numbers: list[int], threshold: int):
    return list(map(lambda n: round_number(n, threshold), numbers))

print(round_numbers([10,13,432,654,23,45], 50))
