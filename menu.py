
import punto12
import punto13
import punto16
import punto2
import punto3


while True:
    print("\n========== MENÚ DE EJERCICIOS ==========")
    print("12. Suma de números naturales")
    print("13. Conteo de pares e impares")
    print("14. Cantidad de dígitos")
    print("15. Número positivo, negativo o cero")
    print("16. Número mayor y menor")
    print("0. Salir")
    print("========================================")

    opcion = input("Seleccione una opción: ")

    if opcion == "12":
        punto12.ejecutar()

    elif opcion == "13":
        punto13.ejecutar()

    elif opcion == "14":
        punto16.ejecutar()

    elif opcion == "15":
        punto2.ejecutar()

    elif opcion == "16":
        punto3.ejecutar()

    elif opcion == "0":
        print("Gracias por utilizar el programa.")
        break

    else:
        print("Opción no válida. Intente nuevamente.")
