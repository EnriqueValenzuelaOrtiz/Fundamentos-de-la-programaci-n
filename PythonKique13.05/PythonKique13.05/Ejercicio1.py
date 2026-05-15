##El usuario ingresa un numero  entero n. El programa debe contar cuantos numero pares existen entre 1 y n (inclusive) y los muentra junto con el total.
n=int(input("Ingrese un número: \n"))
c=0
for i in range(1,n+1):
    if i%2==0:
        c+=1
        print(f"Los pares son:{i}")
print(f"La cantidad de pares es:{c}")
