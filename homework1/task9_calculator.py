liczba1=int(input("podaj lcizbe"))
liczba2=int(input("drugą liczbę"))
znak=input("znak:")
if znak == "+":
    print(liczba1+liczba2)
elif znak=="-":
    print(liczba1-liczba2)
elif znak=="*":
    print(liczba1*liczba2)
else:
    print(liczba1/liczba2)