nombre=input("Ingrese su nombre: \n")
tipotarifa=input("Ingrese su tipo de tarifa: (residencial/comercial)\n")
consumo=int(input("Ingrese su consumo: (kWh)\n"))
if tipotarifa.lower()=="residencial" and consumo<=150:
    print("Su total a pagar es de: $",consumo*82, "pesos")
elif tipotarifa.lower()=="residencial" and consumo>150:
    print("Su total a ágar es de $",150*82 + 110(consumo-150), "pesos")
else:
    print("Su total a pagar es de: $",consumo*130, "pesos")
print("Nombre: ", nombre.upper())
print("Cantidad de letras: ",len(nombre))