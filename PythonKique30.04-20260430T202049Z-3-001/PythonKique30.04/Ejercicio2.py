lado1=int(input("Ingrese el valor del primer lado: \n"))
lado2=int(input("Ingrese el valor del segundo lado: \n"))
lado3=int(input("Ingrese el valor del terceer lado: \n"))
if lado1+lado2>lado3 or lado2+lado3>lado1 or lado1+lado3>lado2:
    if lado1+lado2<lado3 or lado2+lado3<lado1 or lado1+lado3<lado2:
        print("Su figura es imposible")
        triangulo="no"
    elif lado1==lado2 and lado1==lado3:
        print("Su figura es un Triángulo Equilátero")
    elif lado1==lado2 or lado1==lado3 or lado2==lado3:
        print("Su figura es un Triángulo Isóceles")
    elif lado1!=lado2 and lado2!=lado3 and lado1!=lado3:
        print("Su figura es un Triángulo Escaleno")
if triangulo=="si" and lado1**2+lado2**2==lado3**2 or lado2**+lado3**2==lado1**2 or lado1**2+lado3**2==lado2**2:
    print("Su triangulo es Rectángulo") 
if lado1+lado2==lado3 or lado1+lado3==lado2 or lado2+lado3==lado1:
    print("Su figura es un segmento")
