nombre=input("Ingrese su nombre: \n")
lim_inferior=int(input("Ingrese el valor del límite inferior: \n"))
lim_superior=int(input("Ingrese el valor del límite superior: \n"))
from random import randint
numero=randint(lim_inferior, lim_superior)
if numero%3==0:
    numero=numero+1
    if numero>lim_superior:
        numero=numero-2
num=int(input("Ingrese su primer intento: \n"))
if num==numero:
    print("¡Acertaste!")
puntos=100
resto=numero-num


