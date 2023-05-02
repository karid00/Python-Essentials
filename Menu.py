import pandas as pd
import matplotlib.pyplot as plt


try:
    from Ejercicio1Parte1 import ejercicio11 as programa_1
    from Ejercicio1Parte2 import Ejercicio12 as programa_2
    from Ejercicio2Parte1 import ejercicio2_1 as programa_3
    from Ejercicio2Parte2 import ejercicio2_2 as programa_4
    from Ejercicio3 import ejercicio3 as programa_5
except ImportError as e:
    print("Error al importar los módulos:", e)
    exit(1)

opcion=None
while opcion!="A" or opcion!="B" or opcion!="C" or opcion!="D" or opcion!="E":
    print("A. Consultando los tipos de valores\nB. Identificación dato en Python")
    print("C. Imprimir pares, impares y atípicos\nD Creación contraseña")
    print("E. Valores más altos y bajos\n0 Salir\n")
    opcion = input("Ingresa una opción: ")
    print("\n\n")
    if opcion == "A":
        programa_1()
        print("\n\n")
    elif opcion == "B":
        programa_2()
        print("\n\n")
    elif opcion == "C":
        programa_3()
        print("\n\n")
    elif opcion == "D":
        programa_4()
        print("\n\n")
    elif opcion == "E":
        programa_5()
        print("\n\n")
    elif opcion == "0":
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida. Por favor, ingresa una opción válida.\n")