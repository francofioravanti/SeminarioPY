

equipos={



}

while True:
    print()
    print("Opciones disponibles: ")
    print("1) Agregar un equipo.")
    print("2) Registrar un resultado.")
    print("3) Mostrar tabla de posiciones.")
    print("4) Eliminar un equipo.")
    print("5) Salir del programa.")

    opcion=input("Elija una opcion: ")
    match opcion:
        case "1":
            # agregar equipo
            name=input("Ingrese el nombre del equipo: ")
            if name in equipos:
                print("El equipo ya existe.")
            else:
                equipos[name]=0
                print("Se registró exitosamente.")
            
        case "2":
            # registrar resultado
            local=input("Ingrese el nombre del equipo local: ")



            

            visit=input("Ingrese el nombre del equipo visitante: ")

            if local not in equipos or visit not in equipos:
                print("Alguno de los equipos ingresados no esta registrado.")
                continue

            print(f"{local}  -  {visit}")

            resultado=input("Ingrese el resultado (ej.:4-2): ")
            
            partes=resultado.split("-")
            
            if len(partes)!= 2:
                print("Formato de marcador invalido.")
                continue
            
            golLocal=partes[0]
            golVisit=partes[1]
            if not golVisit.strip().isdigit() or not golLocal.strip().isdigit():
                print("No respetaste el formato de marcador.")
                continue

            if golLocal > golVisit:
                equipos[local]+=3
            elif golLocal < golVisit:
                equipos[visit]+=3
            else:
                equipos[visit]+=1
                equipos[local]+=1


            print(f"{local} {golLocal} - {golVisit} {visit}")

            
        case "3":
            # mostrar tabla
            print("========= TABLA DE POSICIONES =========")
            for equipo , puntos in sorted(equipos.items() , key=lambda x:x[1] , reverse=True):
                print(f"{equipo}: {puntos}pts")


        case "4":
            
            # eliminar equipo

            equipo=input("Ingrese el equipo a eliminar: ")
            if equipo not in equipos:
                print("Ese equipo no existe.")
            else:
                del equipos[equipo]
                print("Equipo eliminado.")

        case "5":
            break
        case _:
            print("Opcion invalida")
