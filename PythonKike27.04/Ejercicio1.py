nombre=input("Ingrese el nombre del paciente: \n") 
especie=input("Indique la especie del paciente (perro/gato): \n").lower()
peso=float(input("Indique el peso del paciente (Kg): \n"))
print("")
if especie=="perro" and peso<10:
    print("Consulta pequeña-$15.000")
elif especie=="perro" and peso>=10:
    print("Consulta grande-$22.000")
elif especie=="gato":
    print("Consulta felina-$12.000")
else:
    print("*Especie no atendida en esta clínica*")
print("Nombre paciente: ", nombre.upper())
print("Cantidad de letras: ", len(nombre))