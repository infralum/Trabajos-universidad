s = input().strip()
#ingreso informacion de usuario, pero eliminando los espacios

palabra = "pythonia"
#palabra a buscar
suma= 0

for char in s:
#char es una abreviatura de "character"
    if suma < len(palabra) and char == palabra[suma]:
        suma += 1
        #sumamos 1 a suma si el caracter corresponde a la palabra buscada
    if suma == len(palabra):
        break

print("SI" if suma == len(palabra) else "NO")
