try:
    file = open("data.txt")
    print(file.name)
except FileNotFoundError as error:
    print(f"plik nie istnieje:{error}")
else:
    print("Prawidłowe wczytanie pliku")