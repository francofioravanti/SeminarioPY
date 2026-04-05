posts = [
"Arrancando el lunes con energía #Motivación #NuevaSemana",
"Terminé mi primer proyecto en Python #Python #Programación #OrgullosoDeMi",
"No puedo creer el final de la serie #SinSpoilers #SerieAdicta",
"Nuevo video en el canal sobre #InteligenciaArtificial y #Python",
"Entrenamiento de hoy completado #Fitness #Motivación #NoPainNoGain",
"Leyendo sobre #InteligenciaArtificial y el futuro del trabajo #Tecnología",
"Arranqué a estudiar #Programación por mi cuenta #Python #Autodidacta",
"Finde de lluvia, maratón de series #SerieAdicta #Relax",
"Workshop de #InteligenciaArtificial en la universidad #Tecnología #Programación"
]

map={}

for i in range(len(posts)):
    if posts[i].count("#") >= 1:
        palabras=posts[i].split()
        ht=[ p for p in palabras if "#" in p]
        for i in range(len(ht)):
            if not ht[i] in map:
                map[ht[i]]= 1
            else:
                map[ht[i]]+=1
resultado=sorted(map.items(),key=lambda item:item[1],reverse=True)
print(resultado)
suma=sum(map.values())

print(suma)
#print (map)






