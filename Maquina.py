entrada = input()
clave = "FLDSMDFR21"
ciclo = 0

#en caso de ingresar la clave incorrecta:
while entrada != clave and ciclo <= 4:
    entrada = str(input())
    ciclo += 1
    if ciclo == 4:
        print("FLDSMDFR bloqueada!")
        exit()
        
#en caso de ingresar la clave correcta
if entrada == clave:
    agua = int(input())
    maquina = agua // 3
    filas = "*"
    contador = 0

    
#contador es para contar la veces el ciclo, mientras el calculo de maquina sea
#diferente al contador se seguira sumando los *
    while maquina != contador:
        print(filas)
        filas += " *"
        contador +=1
