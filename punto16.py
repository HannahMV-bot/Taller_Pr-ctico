def ejecutar():
    num = int(input("Ingrese un número entero positivo: "))

    if num <= 0:
        print("Debe ingresar un número entero positivo.")
    else:
        contador = 0
        temp = num

        while temp > 0:
            temp = temp // 10
            contador += 1

        print(f"El número {num} tiene {contador} dígitos.")


if _name_ == "_main_":
    ejecutar()