rounds = [
    {
        'theme': 'Entrada',
        'scores': {
            'Valentina': {'judge_1': 8, 'judge_2': 7, 'judge_3': 9},
            'Mateo': {'judge_1': 7, 'judge_2': 8, 'judge_3': 7},
            'Camila': {'judge_1': 9, 'judge_2': 9, 'judge_3': 8},
            'Santiago': {'judge_1': 6, 'judge_2': 7, 'judge_3': 6},
            'Lucía': {'judge_1': 8, 'judge_2': 8, 'judge_3': 8},
        }
    },
    {
        'theme': 'Plato principal',
        'scores': {
            'Valentina': {'judge_1': 9, 'judge_2': 9, 'judge_3': 8},
            'Mateo': {'judge_1': 8, 'judge_2': 7, 'judge_3': 9},
            'Camila': {'judge_1': 7, 'judge_2': 6, 'judge_3': 7},
            'Santiago': {'judge_1': 9, 'judge_2': 8, 'judge_3': 8},
            'Lucía': {'judge_1': 7, 'judge_2': 8, 'judge_3': 7},
        }
    },
    {
        'theme': 'Postre',
        'scores': {
            'Valentina': {'judge_1': 7, 'judge_2': 8, 'judge_3': 7},
            'Mateo': {'judge_1': 9, 'judge_2': 9, 'judge_3': 8},
            'Camila': {'judge_1': 8, 'judge_2': 7, 'judge_3': 9},
            'Santiago': {'judge_1': 7, 'judge_2': 7, 'judge_3': 6},
            'Lucía': {'judge_1': 9, 'judge_2': 9, 'judge_3': 9},
        }
    },
    {
        'theme': 'Cocina internacional',
        'scores': {
            'Valentina': {'judge_1': 8, 'judge_2': 9, 'judge_3': 9},
            'Mateo': {'judge_1': 7, 'judge_2': 6, 'judge_3': 7},
            'Camila': {'judge_1': 9, 'judge_2': 8, 'judge_3': 8},
            'Santiago': {'judge_1': 8, 'judge_2': 9, 'judge_3': 7},
            'Lucía': {'judge_1': 7, 'judge_2': 7, 'judge_3': 8},
        }
    },
    {
        'theme': 'Final libre',
        'scores': {
            'Valentina': {'judge_1': 9, 'judge_2': 8, 'judge_3': 9},
            'Mateo': {'judge_1': 8, 'judge_2': 9, 'judge_3': 8},
            'Camila': {'judge_1': 7, 'judge_2': 7, 'judge_3': 7},
            'Santiago': {'judge_1': 9, 'judge_2': 9, 'judge_3': 9},
            'Lucía': {'judge_1': 8, 'judge_2': 8, 'judge_3': 7},
        }
    }
]


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



print("////////////////////////////////////////////")
print("////////////////////////////////////////////")

ranking_final = sorted(tabla_final.items(), key=lambda x: x[1]['puntos'], reverse=True)

for nombre, datos in ranking_final:
    print(f"{nombre}: {datos['puntos']} puntos - {datos['rondas_ganadas']} rondas ganadas - {datos['mejor_ronda']} mejor puntuacion - {datos['promedio']:.1f} promedio")


print("////////////////////////////////////////////")
print("////////////////////////////////////////////")











