def pokaz_wszystko(*args, **kwargs):
    print("Argumenty pozycyjne (args):", args)
    print("Argumenty nazwane (kwargs):", kwargs)
pokaz_wszystko(1, "test", 3.14, imie="Jan", wiek=50)


#global vs nonlocal
#global : Używane wewnątrz funkcji, aby zasygnalizować, że chcemy zmodyfikować
#zmienną z zakresu globalnego.
#nonlocal : Używane w funkcji zagnieżdżonej, aby zasygnalizować, że chcemy
#zmodyfikować zmienną z zakresu otaczającego (ale nie globalnego).
x = "globalny"
def funkcja_zewnetrzna():
    y = "otaczający"
    def funkcja_wewnetrzna():
        global x
        nonlocal y
        x = "zmieniony globalny"
        y = "zmieniony otaczający"
    funkcja_wewnetrzna()
    print("Wartość y po zmianie:", y)
funkcja_zewnetrzna()
print("Wartość x po zmianie:", x)


# Adnotacje w funkcji
def powitanie(imie: str, ilosc: int = 1) -> str:
    return f"Cześć, {imie}! " * ilosc
# Adnotacje dla zmiennych
wiek: int = 30
lista_imion: list[str] = ["Anna", "Piotr"]
for i in lista_imion:
    print(powitanie(i, 2))

def calculator(a: float|int, what: str, b: float|int) -> float:
    '''robi rzeczy wprost niesamowite!'''
    if what == "+":
        print(a+b)
    elif what == "-":
        print(a-b)
    elif what == "*":
        print(a*b)
    elif what=="/" or what ==":":
        print(a/b)
    else:
        print("nie nauczyli mnie innych działań")    

# num_1 = float(input("1. liczba"))
# what = str(input("co robisz?"))
# num_2 = float(input("2. liczba"))

# calculator(num_1, what, num_2)

def opis_ksiazki(tytul, autor, rok_wydania=2024):
    print(f"Książka '{tytul}', napisana przez {autor}, wydana w roku {rok_wydania}")

opis_ksiazki("Wichrowe Wzgórza", rok_wydania=2026, autor = "Agatha Christie")

def oblicz_srednia(*args: float) -> float:
    if not args:  # jeśli nie podano żadnych argumentów
        return 0
    return sum(args) / len(args)

# zmienna globalna
POZIOM_DOSTEPU = "user"

def zmien_poziom():
    # zmienna lokalna o tej samej nazwie (NIE używamy global)
    POZIOM_DOSTEPU = "admin"
    print("Wewnątrz funkcji:", POZIOM_DOSTEPU)

# sprawdzenie
print("Przed wywołaniem funkcji:", POZIOM_DOSTEPU)

zmien_poziom()

print("Po wywołaniu funkcji:", POZIOM_DOSTEPU)


print(calculator.__doc__)

def wielokrotne_powitanie(imie: str, ilosc: int) -> None:
    print((f"Cześć, {imie}!\n") * ilosc)

def wielokrotne_powitanie2(imie: str, ilosc: int) -> None:
    for _ in range(ilosc):
        print(f"Cześć, {imie}!")

wielokrotne_powitanie("JACEK", 4)

