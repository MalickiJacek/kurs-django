prawo_jazdy = input("Czy masz prawo jazdy? (tak/nie): ")
wiek = int(input("Ile masz lat? "))

ma_prawo_jazdy = prawo_jazdy == "tak"
ma_18_lat = wiek >= 18

wynik = ma_prawo_jazdy and ma_18_lat

print(wynik)
