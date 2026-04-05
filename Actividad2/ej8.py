text=input("Ingrese lo que quiera cifrar: ")
shift=int(input("Ingrese el numero de desplazamiento: "))
palabra=""
for word in text :
    if (word.isalpha()):

        start = ord("A") if word.isupper() else ord("a")
        letter_pos = ord(word) - start

        letter_pos+=shift
        nueva_pos= letter_pos % 26

        palabra += chr(nueva_pos + start)

    else:
        
        palabra+=word

print(palabra)
desencriptado=""
for word in palabra :
    if (word.isalpha()):

        start = ord("A") if word.isupper() else ord("a")
        letter_pos = ord(word) - start

        letter_pos-=shift
        nueva_pos= letter_pos % 26

        desencriptado += chr(nueva_pos + start)
        
    else:
        desencriptado+=word
print(desencriptado)

        
