# -*- coding: utf-8 -*-
def Ejercicio12():
    def identification(a):
        try:
            a=int(a)
            print(f"Este tipo de dato en Python es:\n{type(a)}") 
        except:
               try:
                    a=float(a)
                    print(f"Este tipo de dato en Python es:\n{type(a)}") 
               except:  
                    try:
                        a=complex(a)
                        print(f"Este tipo de dato en Python es:\n{type(a)}") 
                    except:                    
                            if a=="True" or a=="False":
                                print("Este tipo de dato en Python es:\n booleano") 
                            else:
                                print("Este tipo de dato en Python es:\n str") 
                           
    for a in range(5):
        var1=input("Ingrese un valor cualquiera:")
        identification(var1)