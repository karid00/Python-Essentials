def ejercicio2_2():
    tiene_letra_minuscula = False
    tiene_letra_mayuscula = False
    tiene_numero = False
    tiene_simbolo_especial = False
    
    contrasena = input("Ingrese su contraseña: ")
    
    for caracter in contrasena:
        if caracter.islower():
                tiene_letra_minuscula = True
        elif caracter.isupper():
                tiene_letra_mayuscula = True
        elif caracter.isdigit():
                tiene_numero = True
        elif caracter in "$%*@":
                tiene_simbolo_especial = True
    
    
    if (tiene_letra_minuscula and tiene_letra_mayuscula and tiene_numero and tiene_simbolo_especial and
            5 <= len(contrasena) <= 15
        ):
            print("Contraseña registrada.")
    else:
        requisitos_faltantes = []
        if not tiene_letra_minuscula:
                requisitos_faltantes.append("Debe contener al menos una letra minúscula entre las letras: a,b,c,d,e,f,g,h,i,j.")
        if not tiene_letra_mayuscula:
                requisitos_faltantes.append("Debe contener al menos una letra mayúscula entre las letras: K,L,M,N,O,P,Q,R,S,T.")
        if not tiene_numero:
                requisitos_faltantes.append("Debe contener al menos un número entre 0 y 9.")
        if not tiene_simbolo_especial:
                requisitos_faltantes.append("Debe contener un símbolo especial entre: $,%,*,@")
        if not (5 <= len(contrasena) <= 15):
                requisitos_faltantes.append("Tamaño mínimo de 5 caracteres y máximo de 15.")
        print("La contraseña no cumple con los requisitos. Faltantes:")
        for requisito in requisitos_faltantes:
            print("- " + requisito)
