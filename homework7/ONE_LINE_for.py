kwadraty_liczb_parzystych = []
for i in range(1,11):
    if i % 2 == 0:
        kwadraty_liczb_parzystych.append(i ** 2)
    i=+1
print(kwadraty_liczb_parzystych)

kwadraty_liczb_parzystych1 = [i ** 2 for i in range(1,11) if i% 2 ==0]

print(kwadraty_liczb_parzystych1)

def czy_liczba_pierwsza(element):
    if element < 2:
        return False
    for i in range (2,element):
        if element % i == 0:
            return False
    return True
        
liczby_pierwsze = [i for i in range(1,111) if czy_liczba_pierwsza(i)]

print(liczby_pierwsze)

# Set comprehension (tworzy zbiór unikalnych wartości)
kwadraty_zbior = {x ** 2 for x in [1, 2, 2, 3]}
# Wynik: {1, 4, 9}

# Dict comprehension (tworzy słownik)
liczby_slownik = {x: x ** 2 for x in range(1, 5)}
# Wynik: {1: 1, 2: 4, 3: 9, 4: 16}
## ZAPISZ_NOWY_CIĄG = [ZRÓB COŚ Z LICZBĄ for LICZBA in ZBIÓR_LICZB if SPEŁNIA WARUNEK]