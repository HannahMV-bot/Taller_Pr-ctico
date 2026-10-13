# Archivo punto3.py — Número mayor y menor
def ejecutar():
    a = float(input("Número 1: "))
    b = float(input("Número 2: "))
    c = float(input("Número 3: "))

    print("Mayor:", max(a, b, c))
    print("Menor:", min(a, b, c))


if __name__ == "__main__":
    ejecutar()
