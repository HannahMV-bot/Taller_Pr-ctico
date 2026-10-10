num = int(input("Ingrese un número entero positivo: "))

contador = 0
temp = num

while temp > 0:
    temp = temp // 10
    contador += 1

print(f"Tiene {contador} dígitos.")
