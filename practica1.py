#print ("BIENVENIDO A EMPAREJANDO.COM\n")
#print("Necesitamos conocer algunos datos sobre ti para encontrar tu pareja ideal")
#Nombre = input("Tu nombre: ")
#edad = input('Dime tu edad: ')
#print ('Hola', Nombre, '.Si no me equivoco, tiene', edad,'años')
#print('Menu:')
#Taburete = input('¿Te gusta Taburete? ')
#if Taburete in ('s','S','si','Si','SI'):
#    print("OK Boomer, lo tuyo va a ser un caso difícil.")
#else:
#    print("Bueno, al menos es un comienzo. Veremos qué se puede hacer contigo.")

#suma=1
#num=0
#sum=suma+num
#while(num<=9):
#    num=num+1
#    print("Que no cumple " +str(num))

#anos = ('Que no cumple 1', 'Que no cumple 2','Que no cumple 3', 'Que no cumple 4', 'Que no cumple 5', 'Que no cumple 6' )
#for anos in anos:
#    print(anos)
    
#manzanas = [39]
#peras = [36]
#lechuga = [17]
#lista = ["manzana", "peras", "lechuga"]
#lista


#productos={"manzanas":39, "peras":32, "lehcuga":17}
#print(productos)

def cifradocesar():
    return cifradocesar
texto = input("Mensaje >").upper()
n = int(input("Desplazamiento > "))
abc = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
cifrado = ""
for l in texto:
    if l in abc:
        pos_letra = abc.index(l)
        nueva_pos = (pos_letra + n) % len(abc)
        cifrado+= abc[nueva_pos]
    else:
        cifrado+= l

print("Mensaje cifrado:", cifrado)