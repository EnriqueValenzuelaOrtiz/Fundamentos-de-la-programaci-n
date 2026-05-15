edad=int(input("Ingrese su edad: \n"))
tramo=input("Ingrese su tramo (A/B/C/D): \n").lower()
medicamentos=60000
despacho=8000
descuento=0
total=0
if edad<=30:
    if tramo=="a" or tramo=="b":
        descuento=18
        total=medicamentos*0.82
        despacho=despacho*0.9
    elif tramo=="c" or tramo=="d":
        descuento=12
        total=medicamentos*0.88
if edad>30 and edad<=54:
    if tramo=="a" or tramo=="b":
        descuento=12
        total=medicamentos*0.88
        despacho=despacho*0.9
    elif tramo=="c" or tramo=="d":
        descuento=8
        total=medicamentos*0.92
if edad>=55 and edad<=60:
    if tramo=="a" or tramo=="b":
        descuento=12
        total=medicamentos*0.88
        despacho=despacho*0.85
    elif tramo=="c" or tramo=="d":
        descuento=8
        total=medicamentos*0.92
        despacho=despacho*0.95
if edad>=61:
    if tramo=="a" or tramo=="b":
        despacho=despacho*0.85
        total=medicamentos
    elif tramo=="c" or tramo=="d":
        despacho=despacho*0.95
        total=medicamentos
print("")
print("El valor de medicamentos es de: $",total, )
print("El valor del despacho es de: $",despacho, )


