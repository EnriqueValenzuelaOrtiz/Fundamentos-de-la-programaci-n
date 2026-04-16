edad=int(input("Ingrese su edad:\n"))
print("")
l=input("¿Tienes licencia de conducir? (si/no)\n")
print("")
#convertir lo que el usuario escribió en minúsculas
l=l.lower()
if edad>=18 and l=="si":    
    print("Puede conducir")
elif edad>=18 and l=="no":    
    print("Debe sacar la licencia")
else:    
    print("No puede conducir")
print("")