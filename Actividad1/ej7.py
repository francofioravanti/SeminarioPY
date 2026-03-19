word= input("Ingrese palabras  (corte . ): ")
lista=[]


while word!= ".":
    lista.append(word)
    word= input("Ingrese palabras (corte . ): ")


for palabra in lista:
     if (len(palabra) <=3):
          lista.remove(palabra)
     
print(lista)
     