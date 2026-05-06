edad=int(input("Ingrese su edad: \n"))
tramo=input("Ingrese su tramo (A/B/C/D): \n ").lower()
carga=input("¿Tiene cargas familiares? (Sí/No): \n").lower()
pb=45,000
descuento=0
if edad<=30 and (tramo=="a" or tramo=="b"):
    precio_plan=pb*0,8
    descuento=20
    if carga=="si":
        coste_carga=8,000
        precio_plan_carga=precio_plan+coste_carga
elif edad<=30 and (tramo=="c" or tramo=="d"):
    precio_plan=pb*0,9
    descuento=10
    if carga=="si":
        coste_carga=5,000
        precio_plan_carga=precio_plan+coste_carga
elif edad>=31 and edad<=60 and (tramo=="a" or tramo=="b"):
    precio_plan=pb*0,9
    descuento=10
    if carga=="si":
        coste_carga=8,000
        precio_plan_carga=precio_plan+coste_carga
elif edad>=31 and edad<=60 and (tramo=="c" or tramo=="d"):
    precio_plan=pb*0,95
    descuento=5
    if carga=="si":
        coste_carga=5,000
        precio_plan_carga=precio_plan+coste_carga
elif edad>60:
    precio_plan=pb
    descuento=0
print(f"El precio base de su plan de salud es de: $"{pb} "pesos.")
print(f"Su porcentaje de decuento es de: "{descuento} "porciento.")
print(f"Su Precio con descuento es: $"{precio_plan} "pesos.")
print(f"El costo de las cargas familiares es de: $"{coste_carga} "pesos.")
print(f"El coste total de su plan es de: $"{precio_plan_carga} "pesos.")