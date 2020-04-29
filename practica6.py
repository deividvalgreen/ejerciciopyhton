def cifracesar(texto,key):
    texto = input("Mensaje > ").upper()

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
