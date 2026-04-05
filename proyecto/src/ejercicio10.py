

def procesar_rondas(rounds):
    map={}
    tabla_final={  }


    for ronda in rounds:

        print("--------------------------------------------------")
        print(f"Ronda: {ronda['theme']}   ")
        map={}

        for nombre, datos in ronda['scores'].items():
            
            puntos = sum(datos.values())
            map[nombre] = map.get(nombre, 0) + puntos

            if nombre not in tabla_final:
                tabla_final[nombre] = {'puntos': puntos, 'rondas_ganadas': 0 ,'mejor_ronda':puntos , 'promedio':0 }
            else:
                tabla_final[nombre]['puntos'] += puntos
                if tabla_final[nombre]['mejor_ronda'] < puntos :
                    tabla_final[nombre]['mejor_ronda'] = puntos
        
        ganador_ronda= max(map, key=map.get)
        tabla_final[ganador_ronda]['rondas_ganadas']+=1

        

        

        ranking = sorted(map.items(), key=lambda x: x[1], reverse=True)



        i=1
        for jugador in ranking:
            if(i==1):
                print(f"Ganador: {jugador}")
            else:
                print(f"{i}) {jugador}")
            i+=1




    for nombre in tabla_final:
        tabla_final[nombre]['promedio'] = tabla_final[nombre]['puntos'] / len(rounds)


    return tabla_final












