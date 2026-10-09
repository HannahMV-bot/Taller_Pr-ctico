num = int(input("Ingrese un número entero positivo: "))

# El ciclo elimina el último dígito dividiendo entre 10 en cada paso
contador = 0
temp = num

while temp > 0:
    temp = temp // 10
    contador += 1

print(f"Tiene {contador} dígitos.")