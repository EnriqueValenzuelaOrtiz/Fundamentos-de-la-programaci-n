nombre=input("Ingrese su nombre: \n")
años=int(input("Ingrese la cantidad de años de experiencia: \n"))
nivelingles=(input("Ingrese su nivel de inglés: (básico/intermedio/avanzado) \n "))
disponibilidad=input("Disponibilidad para viajar: (sí/no)")
print("")
if años>=5 and nivelingles.lower()=="avanzado":
    print("Postulante DESTACADO-Pasa a entrevista final")
elif años>=3 and nivelingles.lower()=="avanzado" or nivelingles.lower()=="intermedio":
    print("Postulante APTO-pasa a 2da fase")
elif disponibilidad.lower()=="si" and años>=1:
    print("Postulante EN REVISIÓN")
else:
    print("ppostulante NO CUMPLE con los requisitos")
print("Nombre: ",nombre.upper())
print("Largo nombre: ",len(nombre))
