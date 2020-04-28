abecedario=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'Ã±', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


print("BIENVENIDO A MI CIFRADOR CE‰SAR")

texto_claro=input("Escribe el texto a cifrar: ")
clave=int(input("Escribe la clave de cifrado (un numero del 1 al 27): "))


texto_cifrado=""

for letra in texto_claro:
    nueva_posicion = abecedario.index(letra)
    letra_cifrada = (nueva_posicion + texto_claro) % len(abecedario)
    texto_cifrado+= letra_cifrada

print("\nEl mensaje cifrado es:",texto_cifrado)