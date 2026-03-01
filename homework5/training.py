age=int(input("Type in your age:"))

if age>=65:
    print("Senior")
elif age>=18:
    print("Adult")
elif age>=13:
    print("Teenage")
elif age>=2:
    print("Child")
else:
    print("Newborn")

price_in_pln = 100
is_student = False

is_not_adult = False
if is_student or is_not_adult:
    price_in_pln=price_in_pln*0.5
    print(f"Cena po zniżkach: {price_in_pln}") 
if not (is_student and is_not_adult):
    print(f"Cena bez zmian, wynosi {price_in_pln}")

i=10
while i>0:
    print(f"{i}....")
    i-=1

text=str(input("Wpisz słowo do przeliterowania:"))
for i in text:
    print(i)

for i in range(1, 6):
    for j in range(1,6):
        print(f"{i} times {j} equals: {i * j}")

#guess number
sekret = 42

while True:
    liczba = int(input("Zgadnij liczbę: "))

    if liczba == sekret:
        print("Gratulacje! Odgadłeś liczbę!")
        break
    else:
        print("Zła liczba, spróbuj ponownie.")

#samogłoski
sentence = str(input("Wprowadź dowolne zdanie:"))
string=""
for i in sentence:
    if i not in "AaĄąEeĘęIiOoUuÓóYy":
        continue
    string+=i

print(string)

#wyszukiwarka w liście:
names = ["Anna", "Jan", "Piotr",
"Kasia"]
name = str(input("wprowadź imię, sprawdzę czy jesteś na liście zaproszonych"))
for i in names:
    if i==name:
        print("Wchodzisz")
        break
else: print("niestety, nie ma Ciebie na liście")

#potęgi dwójki
i=1
while i < 500:
    i*=2
    print(i)

#mini projekt
kursy = {"USD": 4.0, "EUR": 4.3}

while True:
    # Pobranie danych od użytkownika
    kwota_pln = float(input("Podaj kwotę w PLN: "))
    waluta = input("Podaj walutę (USD/EUR): ").upper()

    # Sprawdzenie wybranej waluty
    if waluta == "USD":
        wynik = kwota_pln / kursy["USD"]
        print(f"Otrzymasz {wynik:.2f} USD")
    elif waluta == "EUR":
        wynik = kwota_pln / kursy["EUR"]
        print(f"Otrzymasz {wynik:.2f} EUR")
    else:
        print("Nieprawidłowa waluta! Wybierz USD lub EUR.")

    # Pytanie o kontynuację
    kontynuuj = input("Czy chcesz kontynuować? (tak/nie): ").lower()
    if kontynuuj == "nie":
        print("Koniec programu.")
        break
