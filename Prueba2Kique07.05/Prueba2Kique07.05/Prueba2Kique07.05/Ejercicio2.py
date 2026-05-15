num1=int(input("Ingrese el límite superior: \n"))
num2=int(input("Ingrese el límite inferior (mayor que el anterior): \n"))
from random import randint
numero=randint(num1,num2)
if numero%2>0 and numero+1>num1:
    numero=numero-1
elif numero%2>0 and numero+1<num1:
    numero=numero+1
else:
    numero=numero
print("")
numero_usuario1=int(input("Intente adivinar: \n"))
if numero_usuario1==numero:
    print("Felicitaciones, pudiste adivinar")
else:   
    if numero_usuario1>numero:
        print("El número es menor.")
    elif numero_usuario1<numero:
        print("El número es mayor.")
    numero_usuario2=int(input("Intente adivinar: \n"))
    if numero_usuario2==numero:
        print("Felicitaciones, pudiste adivinar")
    else:
        if numero_usuario2>numero:
            print("El número es menor.")
            print("Te daré una pista: \n")
            if numero_usuario1+numero>numero_usuario2+numero:
                print("El número que buscas está más cerca de",numero_usuario2," que de",numero_usuario1,)
            elif numero_usuario1+numero<numero_usuario2+numero:
                print("El número que buscas está más cerca de",numero_usuario1," que de",numero_usuario2,)
        elif numero_usuario2<numero:
            print("El número es mayor.")
            print("Te daré una pista: \n")
            if numero_usuario1+numero>numero_usuario2+numero:
                print("El número que buscas está más cerca de",numero_usuario2," que de",numero_usuario1,)
            else:
                print("El número que buscas está más cerca de",numero_usuario1," que de",numero_usuario2,)

        numero_usuario3=int(input("Intente adivinar: \n"))
        if numero_usuario3==numero:
            print("Felicitaciones, pudiste adivinar")
        else:
            print("Perdiste")
            print("El número era:",numero,)