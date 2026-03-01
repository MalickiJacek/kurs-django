print("Imię: {}, Wiek: {}".format("Anna", 30))
print("Imię: {imie}, Wiek: {wiek}".format(imie="Anna", wiek=30))
print("Imię: {imie}, Wiek: {wiek: .2f}".format(imie="Anna", wiek=30))
age = 18
adult = True
adult = False if age < 18 else adult
print(adult)

if "Wars" in "Warszawa":
    print("Yup")

x=10
y=11-1
if x is y:
    print("x is y")

licznik = 0
while licznik < 3:
    print(f"wydrukowałem ile razy? {licznik+1}")
    licznik+=1

owoce = ["jabłko", "banan", "wiśnia"]
for j in owoce:
    print(f"Nazwa owocu: {j}")

for j, i in enumerate(owoce, start=1):
    print(f"Nazwa owocu nr {j}: {i}")

# Iteracja po stringu
for i in "Python":
    print(i, end="-") # P-y-t-h-o-n-

for i in range(1, 6, 2): # Liczby od 1 do 5, z krokiem 2
    print(i) # 1, 3, 5


# Przykład z break i continue
print("\nPrzykład z break i continue:")
for i in range(10):
    if i == 7:
        print("Znaleziono 7, przerywam pętlę!")
        break # Zakończ pętlę
    if i % 2 == 0:
        continue # Pomiń parzyste liczby
    print(f"Przetwarzam liczbę nieparzystą: {i}")

# Przykład z else
print("\nPrzykład z else:")
szukana_liczba = 2
for i in range(1, 4):
    print(f"Sprawdzam {i}...")
    if i == szukana_liczba:
        print("Znaleziono!")
        print("Zakończono skutecznie!")
        break
    else:
        # Ten blok wykona się tylko, jeśli pętla przejdzie przez wszystkie liczby i nie znajdzie szukanej
        print("Nie znaleziono szukanej liczby w pętli.")
else: print("Zakonczono nieskutecznie")