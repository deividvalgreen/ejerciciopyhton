from datetime import date
print ("BIENVENIDO A EMPAREJANDO.COM\n")
print("Necesitamos conocer algunos datos sobre ti para encontrar tu pareja ideal")
Nombre = input("Tu nombre: ")
edad = input('Dime tu edad: ')
print ('Hola', Nombre, '.Si no me equivoco, tiene', edad,'años')
print('Menu:')
ano_actual=date.today().year
edad = ano_actual
Taburete = input('¿Te gusta Taburete? ')
if Taburete in ('s','S','si','Si','SI'):
    print("OK Boomer, lo tuyo va a ser un caso difícil.")
else:
    print("Bueno, al menos es un comienzo. Veremos qué se puede hacer contigo.")

#contador = 1
#while (contador<edad):
#    print("Que no cumple ", contador)
#    contador+=1
    
#print ("Que si cumple ", contador,"!")

#for contador in range(1,edad):
#    print("Que no cumple",contador)

#print("¡ Que sí cumple",edad,"!")
    
#usuario=[Nombre,edad,Taburete]

#for dato in usuario:
#    print(dato)


#usuario={
#        "nombre": Nombre,
#        "edad": edad,
#        "taburete": Taburete
#        }
#for dato in usuario.values():
#    print(dato)