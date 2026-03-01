wzrost=int(input("podaj wzrost"))
wiek=int(input("podaj wiek"))
if wzrost>160 or wiek>16:
    print("wchodzisz bez opiekuna")
else:
    opiekun=(input("czy jest opiekun?"))
    if opiekun=="tak":
        print("możesz wejść")
    else:
        print("niestety...")

