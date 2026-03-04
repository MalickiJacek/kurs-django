import csv
dane_csv = [
["Imię", "Wiek", "Miasto"],
["Anna", 25, "Gdańsk"],
["Piotr", 32, "Kraków"]
]
# --- Zapis do pliku CSV --
with open("dane.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f, delimiter=';') # Możemy zmienić separator
    writer.writerows(dane_csv)
# --- Odczyt z pliku CSV --
with open("dane.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f, delimiter=';')
    for wiersz in reader:
        print(wiersz)