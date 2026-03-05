import json
# Dane w Pythonie (słownik)
uzytkownik = {
"imie": "Zofia",
"wiek": 28,
"miasta": ["Gdańsk", "Warszawa"],
"aktywny": True
}
# --- Serializacja (Python -> JSON) --
# Zapis do pliku
with open("uzytkownik.json", "w", encoding="utf-8") as f:
# indent - tworzy ładne wcięcia
# ensure_ascii=False - kluczowe dla polskich znaków!
    json.dump(uzytkownik, f, indent=4, ensure_ascii=False)
# --- Deserializacja (JSON -> Python) --
# Odczyt z pliku
with open("uzytkownik.json", "r", encoding="utf-8") as f:
    dane_z_pliku = json.load(f)
print(dane_z_pliku["imie"]) # Zofia