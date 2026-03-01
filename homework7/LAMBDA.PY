dodaj = lambda a,b: a+b
print(dodaj(1,2))


slowa = ["jabłko", "banan", "kiwi", "gruszka",
"truskawka"]

owoce_krotkie = [i for i in slowa if len(str(i))>5]
print(owoce_krotkie)

oceny = {"Jan": 4, "Anna": 5, "Piotr": 3,
"Kasia": 4}

oceny_sorted = sorted(oceny, key=lambda oceny: oceny[1])

imiona = ["anna", "piotr", "kasia"]
imiona_v2 = list(map(str.capitalize, imiona))

print(imiona_v2)

from functools import reduce

liczby = [1, 2, 3, 4, 5]

iloczyn = reduce(lambda x, y: x * y, liczby)

print(iloczyn)


uzytkownicy = [
{"imie": "Jan", "wiek": 30, "aktywny": True},
{"imie": "Anna", "wiek": 17, "aktywny": False},
{"imie": "Piotr", "wiek": 25, "aktywny": True}
]

aktywni = [i["imie"].upper() for i in uzytkownicy if i["aktywny"] == True and i["wiek"]>18]
print(aktywni)

def powtorz(n):
    def dekorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return dekorator



@powtorz(5)
def siema():
    print("siema!")

siema()
przywitaj = powtorz(3)(siema)