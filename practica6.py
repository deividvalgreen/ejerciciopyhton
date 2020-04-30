abecedario='abcdefghijklmnopqrstuvwxyz'

print("BIENVENIDO A MI CIFRADOR CÉSAR")

texto_claro=input("Escribe el texto a cifrar: ")
clave=int(input("Escribe la clave de cifrado (un número del 1 al 27): "))
def cifracesar(texto_claro,clave):
    texto_cifrado=""

    for letra in texto_claro:
        nueva_posicion = abecedario.find(letra) + clave
        letra_cifrada = int(nueva_posicion) % len(abecedario)
        texto_cifrado = texto_cifrado + str(abecedario[letra_cifrada])
    return texto_cifrado

cifrado=cifracesar(texto_claro,clave)
print("\nEl mensaje descifrado es: ",cifrado) 
def descifracesar(texto_cifrado,clave):
    texto_descifrado=""

    for letra in texto_cifrado:
        nueva_posicion = abecedario.find(letra) - clave
        letra_cifrada = int(nueva_posicion) % len(abecedario)
        texto_descifrado = texto_descifrado + str(abecedario[letra_cifrada])
 
    return texto_descifrado

descifrado=descifracesar(cifrado,clave)
print("\nEl mensaje descifrado es: ",descifrado) 