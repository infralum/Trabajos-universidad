paciencia = int(input())
contador = 0
sueño = 0
muerte = 0
while paciencia != contador:

    golpe = str(input())
    if golpe == "si":
        contador += 1
        sueño = 0
        muerte += 1
        
    elif golpe == "no":
        sueño +=1
        muerte = 0
    if muerte == 3:
        print("Aplicando correctivo avalado por las autoridades de esta gran nación. ¡¡ PSSSST PSSSST !!")
    elif sueño == 5:
        print("(8) Duérmete pythoncito, duérmete ya, que viene el robotrón y te rociara. (8)")
        
print("Aplicando correctivo avalado por las autoridades de esta gran nación. ¡¡ PSSSST PSSSST !!")
    
si
si
si
si
