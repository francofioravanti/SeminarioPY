import random
names=input("Ingrese una lista de nombres (separados por coma): ").lower().strip()

lista=names.split(",")
if len(lista)>=3:
    
    for name in lista:
        if lista.count(name) >1:
            print(f"{name} se repite {lista.count(name)} veces")
            break
            exit()
    
    mezclados=random.sample(lista,len(lista))
    
    #basicamente si se asigna un nombre a si mismo se vuelve a mezclar
    
    while any(a == b for a,b in zip(lista,mezclados)):
        mezclados=random.sample(lista,len(lista))

    for a,b in zip(lista,mezclados):
        print(f"{a} ---> {b}")
else:
    print("Debe agregar como minimo tres nombres.")