playlist = [
{"title": "Bohemian Rhapsody", "duration": "5:55"},
{"title": "Hotel California", "duration": "6:30"},
{"title": "Stairway to Heaven", "duration": "8:02"},
{"title": "Imagine", "duration": "3:07"},
{"title": "Smells Like Teen Spirit", "duration": "5:01"},
{"title": "Billie Jean", "duration": "4:54"},
{"title": "Hey Jude", "duration": "7:11"},
{"title": "Like a Rolling Stone", "duration": "6:13"},
]

duracionMax=""
duracionMin=""
cancionMasCorta=""
cancionMasLarga=""
segsMin=9999
segsMax=-1
minsTotal=0
segsTotal=0
for cancion in playlist:
    title=cancion["title"]
    duration=cancion["duration"]

    min,segs=duration.split(":")

    mins=min*60
    totalSegs=mins+segs


    ##caclulo cancion larga y corta
    if totalSegs>segsMax :
        segsMax=totalSegs
        cancionMasLarga=title
        duracionMax= str(min) + ":" + str(segs)
    if totalSegs<segsMin :
        segsMin=totalSegs
        cancionMasCorta=title
        duracionMin= str(min) + ":" + str(segs)


    ##calculo duracion total

    minsTotal+=min
    segsTotal+=segs


