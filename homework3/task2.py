weight = float(input("wpisz wagę w kilogramach:"))
height = float(input("wpisz wzrost w centymetrach:"))
bmi = weight / height**2
print(f"BMI wynosi {round(bmi,2)}")
