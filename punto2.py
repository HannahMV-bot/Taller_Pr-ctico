def ejecutar():
    Num = int(input("Ingrese su número: "))

    if Num > 0:
        print("Número positivo")
    elif Num < 0:
        print("Número negativo")
    else:
        print("El número ingresado es cero")


if __name__ == "__main__":
    ejecutar()
    