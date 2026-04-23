g=float(input("Ingrese la temperetura actual (C°)\n"))
if g<10:
    print("Frío")
elif g>=10 and g<=25:
    print("Templado")
else:
    print("Caluroso")