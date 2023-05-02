# -*- coding: utf-8 -*-
def ejercicio11():
    print("\nEmpezando a trabajar con Python\nRealizado por: Karina Dahik\n\nConsultando los tipos de valores:\n")

    var1=875
    print(f"El tipo de dato de {var1} es:\n {type(var1)}\n")

    var1=4.89
    print(f"El tipo de dato de {var1} es:\n {type(var1)}\n")

    var1="Now is better than never."
    print(f"El tipo de dato del texto: {var1} es:\n {type(var1)}\n")

    var1=1.32
    print(f"El tipo de dato de {var1} es:\n {type(var1)}\n")

    var1=(5 + 8j)
    print(f"¿El valor {var1} corresponde a un valor entero?\n {isinstance(var1,int)}\n")

    var1=8.2
    print(f"¿El valor {var1} corresponde a un valor entero?\n {isinstance(var1,int)}\n")

    var1="Readability counts."
    print(f"¿Eltexto: {var1} corresponde a un string?\n {isinstance(var1,str)}")
