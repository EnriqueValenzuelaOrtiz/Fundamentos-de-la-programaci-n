v=input("Ingrese el tipo de veículo (auto/moto/camioneta): \n")
h=int(input("¿Cuántas horas utilizó el estacionamiento?: \n"))
if h<=2:
    pha=h*1,200
if h<=2:
    phm=h*800
if h<=2:
    phc=h*2,500
else:
    pha=2,400
    phm=1,600
    phc=5,000
    e=h-2
    haa=(800*e)+pha 
    ham=(400*e)+phm
    hac=(1,200*e)+phc

if v.lower() =="auto" and h<=2:
    print("El costo es de:", pha, "pesos" )
elif v.lower() =="auto" and h<=3 and h<8:
    print("El costo es de: ", pha+haa, "pesos")
elif v.lower() =="auto" and h>=8:        
    print("El costo normal es de: ", pha+haa, "pesos")
    print("El costo con descuento es de: ", (pha+haa)*0.8)
else:
    if v.lower() =="moto" and h<=2:
        print("El costo es de: ", phm, "pesos")
    elif v.lower() =="moto" and h>=3:
        print("El costo es de: ", phm+ham, "pesos")
    
    else:
            if v.lower() =="camioneta" and h<=2:
                print("El costo el de: ", phc, "pesos")
            elif v.lower() =="camioneta" and h<=3 and h<8:
                print("El costo es de: ", phc+hac, "pesos")
            elif v.lower() =="camioneta" and h>=8:
                print("El costo normal es de: ", phc+hac, "pesos")
                print("El costo con descuento es de: ", (phc+hac)*0.8, "pesos")


    
