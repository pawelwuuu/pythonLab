def most_frequent_element(data: list):
    frequencies = dict()    
    data_set = set(data)
    
    for d in data_set:
        frequencies[d] = 0
    
    for data_check in data_set:
        for data_unit in data:
            if data_unit == data_check:
                frequencies[data_check] = frequencies[data_check] + 1
    
    maxx = 0
    maxx_key = None
    for key, value in frequencies.items():
        if value > maxx:
            maxx = value
            maxx_key = key
    
    return maxx_key
    
print(most_frequent_element(["a", "b", "c", "a", 1, 2, 3, 1, "a"]))  