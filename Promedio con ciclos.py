notas = int(input("cuantas notas desea calcular?"))
contador = 0
suma = 0
while contador < notas:
    n1 = float(input("ingrese la  nota: "))
    suma = suma + n1
    contador += 1

promedio = suma/notas
print(promedio)
