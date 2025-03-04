def transposition_cipher(text: str, key: int) -> str:
    if key > len(text) or key <= 1:
        return text
    
    text_list = list(text)
    n = len(text)
    
    for i in range(key - 1, n - key, key):
        text_list[i], text_list[i + key] = text_list[i + key], text_list[i]
    
    return "".join(text_list)


print(transposition_cipher("HelloWorld", 3))