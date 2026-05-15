##Crea un menu con 4 opciones:(1)Sumar, (2)Restar, (3)Multiplicar, (4)Salir. El programa muestra el menu
##El usuario  elige, ingresa dos números y muestra el resultado. El ciclo se repite hasta que elija salir.
opcion=321321
while opcion!=4:
    print("___MENÚ___")
    print("Elija una opción:")
    print("1._Sumar")
    print("2._Restar")
    print("3._Multiplicar")
    print("4._Salir")
    opcion=int(input("Elija una opcón: \n"))
    if opcion==1:
        num1=int(input("Ingrese el primer número: \n"))
        num2=int(input("Ingrese el segúndo número: \n"))
        print(f"El resultado es:{num1+num2}")
    elif opcion==2:
        num1=int(input("Ingrese el primer número: \n"))
        num2=int(input("Ingrese el segúndo número: \n"))
        print(f"El resultado es:{num1-num2}")

    elif opcion==3:
        num1=int(input("Ingrese el primer número: \n"))
        num2=int(input("Ingrese el segúndo número: \n"))
        print(f"El resultado es:{num1*num2}")
    elif opcion==4:
        print("Gracias por utilizar el sistema!")
    else:
        print("La opción dijitada no es válida")
    print("")

    
