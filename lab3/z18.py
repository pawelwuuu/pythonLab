def konwertuj_temperature(temperatura, skala_zrodlowa, skala_docelowa):
    if skala_zrodlowa == "C" and skala_docelowa == "F":
        return (temperatura * 9/5) + 32
    elif skala_zrodlowa == "F" and skala_docelowa == "C":
        return (temperatura - 32) * 5/9
    elif skala_zrodlowa == "C" and skala_docelowa == "K":
        return temperatura + 273.15
    elif skala_zrodlowa == "K" and skala_docelowa == "C":
        return temperatura - 273.15
    elif skala_zrodlowa == "F" and skala_docelowa == "K":
        return (temperatura - 32) * 5/9 + 273.15
    elif skala_zrodlowa == "K" and skala_docelowa == "F":
        return (temperatura - 273.15) * 9/5 + 32
    else:
        return "Nieznane skale"

# Test
print(konwertuj_temperature(25, "C", "F"))
print(konwertuj_temperature(77, "F", "C"))
