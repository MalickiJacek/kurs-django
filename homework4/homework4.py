'''9. Identyfikator po zmianie: Utwórz zmienną x = 10 . Wyświetl jej id() . Następnie
przypisz do x nową wartość x = x + 1 . Ponownie wyświetl id() . Czy identyfikator się
zmienił? Dlaczego? Odpowiedz w komentarzu.'''
x = 10
print(id(x))
x = x + 1
print(id(x))
#identyfikator zmienił się bo int jest niemutowalny - po każdej zmianie tak naprawde w Python tworzony jest nowy obiekt.
'''10. Komentowanie kodu: Poniżej znajduje się fragment kodu. Dodaj do niego komentarze
jednoliniowe oraz docstring dla funkcji, wyjaśniając, co robi każda część.'''
def oblicz_pole_prostokata(a, b):
    '''funkcja oblicza pole prostokąta mnożąc dwa jego boki, które podaje użytkownik'''
    # zmienna do której przypisujemy wynik mnożenia zmiennych
    pole = a * b
    # Zwracamy pole użytkownikowi
    return pole
bok_a = 10
bok_b = 20
wynik = oblicz_pole_prostokata(bok_a, bok_b)
print(f"Pole prostokąta o bokach {bok_a} i {bok_b} wynosi {wynik}.")