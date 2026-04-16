n=float(input("Ingrese su calificación:\n"))
print("")
if n>=1.0 and n<=3.9:
    print("Usted ha reprobado")
elif n>=4.0 and n<=5.1:
    print("Usted ha aprobado")
elif n>=5.2 and n<=6.5:
    print("Usted ha aprobado con una exelente calificación")
elif n>=6.6 and n<=7.0:
    print("Usted ha aprobado con honores")
else:
    print("Calificación ingresada no válda")
print("")