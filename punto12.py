N = int(input("Ingrese un número natural N: "))

suma = 0

for i in range(1, N + 1):
    suma = suma + i

print("La suma de los números naturales desde 1 hasta", N, "es:", suma)