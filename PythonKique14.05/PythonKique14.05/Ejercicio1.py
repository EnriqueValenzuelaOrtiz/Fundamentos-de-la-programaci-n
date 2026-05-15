##Una emprese realiza una encuesta de satisfacción. El menú tiene opciones: (1)Registrar una respuesta, 1=Muy insatisfecho
##a 5=Muy satisfecho. (2)Ver estadísticas, promedio, mejor/peor puntuación, %de respuestas 4 o 5.
##(3)Nueva encuesta. (4)Salir. La opción 3 reinicia los contadores.
tf=False
opcion=0
prom=0
mejor_nota=0
peor_nota=0
cant_respuestas=0
total_respuestas=0
cant_porcentaje=0
while opcion!=4:    
    print("--------------------------------------")
    print("------------MENÚ ENCUESTA-------------")
    print("--------------------------------------")
    print("-Elija una opción:")
    print("1-Registrar respuesta")
    print("2-Ver estadística")
    print("3-Nueva encuesta")
    print("4-Salir")
try:
    opcion=int(input("¿Qué desea hacer? \n"))
    tf=True
except ValueError:
    print("Caracter dijitado no válido, ingrese un número")
    if opcion==1:
        try:                   
            nota=int(input("Ingrese una nota (1 al 5):"))
            if nota<1 or nota>5:
                raise ValueError("Ingrese un número del 1 al 5")
            else:    
                if nota==4 or nota==5:
                    cant_porcentaje+=1
                cant_respuestas+=1
                total_respuestas+=nota
                if nota>mejor_nota:
                    mejor_nota=nota
                if nota<peor_nota:
                    peor_nota=nota
                prom=total_respuestas/cant_respuestas
                porcentaje=(cant_porcentaje/total_respuestas)*100
            n=input("¿Desea ingresar otra nota? (Sí/No)").lower()
        except ValueError:
            print("Caracter dijitado no válido, ingrese un número")

    elif opcion==2:
        if cant_respuestas==0:
            print("No hay respuestas a la encuesta")
        else:    
            print("*********Estadísticas*********")
            print(f"el promedio de las notas es:{prom}")
            print(f"la mejor puntuacion es:{mejor_nota}")
            print(f"La peor puntuacion es:{peor_nota}")
            print(f"")
    elif opcion==3:
        prom=0
        mejor_nota=0
        peor_nota=0
        cant_respuestas=0
        total_respuestas=0
        cant_porcentaje=0
        nota=0
    elif opcion==4:
        print("Gracias por utilizar el sistema")
    else:
        print("Ingrese un número del 1 al 4")
        
            


