pares = 0
impares = 0
suma_pares = 0

for i in range (1, 101):
    if i % 2 == 0:
        pares += 1
        suma_pares += 1
    else:
        impares += 1

print ("Cantidad de los pares", pares)
print ("Cantidad de los impares", impares)
print ("Suma de los pares", suma_pares)