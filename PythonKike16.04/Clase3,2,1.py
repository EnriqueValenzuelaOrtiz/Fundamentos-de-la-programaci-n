edad=int(input("Ingrese su edad:\n"))
if edad>=18:    
    l=input("¿Tiene licencia? (si/no)")
    if l.lower()=="si":
        print("Puede manejar")
    else:
         print("Debe sacar la licencia")
else:
    print("No puedes manejar")