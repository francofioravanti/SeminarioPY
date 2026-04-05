import string
review = """La película sigue a un grupo de astronautas que
viajan a Marte
en una misión de rescate. El capitán Torres lidera al equipo
a través
de tormentas solares y fallos en el sistema de navegación. Al
llegar
a Marte descubren que la base está abandonada y los
suministros
destruidos. Torres decide sacrificar la nave nodriza para
salvar
al equipo y logran volver a la Tierra en una cápsula de
emergencia.
El final revela que Torres sobrevivió gracias a un pasaje
secreto."""
wordsText= review.split()

spoilers= input("Ingrese las palabras que spoilean: ")

listaSpoiler=[w.strip().lower() for w in spoilers.split(",")]

for i in range(len(wordsText)): 

    cleanWord= wordsText[i].lower().strip(string.punctuation)

    if cleanWord in listaSpoiler :
        wordsText[i] = "*" * len(wordsText[i])

print(" ".join(wordsText))