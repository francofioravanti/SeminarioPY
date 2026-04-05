weight= float(input("Ingrese el peso en kg del envio del pedido: "))

zone= input("Ingrese la zona del destino del pedido: ").lower().strip()
while zone != "local" and zone != "regional" and zone != "nacional":
    zone= input("Ingrese la zona del destino del pedido: ")


match zone:
    case "local":
        if weight<1:
            print("$500")
        elif 1<weight<5:
            print("$1000")
        else:
            print("$2000")
    case "regional":
        if weight<1:
            print(1000)
        elif 1<weight<5:
            print(2500)
        else:
            print(5000)

    case "nacional":
        if  weight<1:
            print(2000)
        elif 1<weight<5:
            print(4500)
        else :
            print(8000)