def szyfruj_tekst(tekst, klucz):
    zaszyfrowany_tekst = ""
    for char in tekst:
        if char.isalpha():
            shift = klucz % 26
            new_char = chr(((ord(char.lower()) - 97 + shift) % 26) + 97)
            if char.isupper():
                new_char = new_char.upper()
            zaszyfrowany_tekst += new_char
        else:
            zaszyfrowany_tekst += char
    return zaszyfrowany_tekst

# Test
print(szyfruj_tekst("Hello World", 3))
