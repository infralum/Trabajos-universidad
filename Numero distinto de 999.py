n1 = int(input("ingrese el primer numero: "))


while n1 != 999:
    if n1 < 0:
        print(f"el {n1} es negativo")
    elif n1 == 0 :
        print(f"el {n1} es cero")
    else:
        print(f"el {n1} es positivo")
    n1 = int(input("reingrese el  numero: "))


print("ingreso el numero 999, fin del ciclo")
