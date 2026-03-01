variable = " Python jest super! "
lenght = len(variable)
print(variable[1:len(variable)-1])

variable1 = variable.strip()
variable2 = variable1.lower()
variable3 = variable2.replace("super", "świetny")

print(f"{variable2}\n{variable3}")