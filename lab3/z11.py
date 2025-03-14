import statistics

def statystyki_lista(lista):
    mediana = statistics.median(lista)
    srednia = statistics.mean(lista)
    min_wartosc = min(lista)
    max_wartosc = max(lista)
    odchylenie_standardowe = statistics.stdev(lista)
    
    return {
        "mediana": mediana,
        "srednia": srednia,
        "min": min_wartosc,
        "max": max_wartosc,
        "odchylenie_standardowe": odchylenie_standardowe
    }
