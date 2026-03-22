import random

categories = {
    "Programacion":["python","programa","variable","funcion","bucle","cadena","entero","lista"],
    "Objetos": ["tijera", "mesa","destornillador","silla","telefono"],
    "Animales":["perro","gato","elefante","loro","capibara"]
}

while True:
    print("¡Bienvenido al Ahorcado!")
    print()
    print("Categorias disponibles: ")
    
    options= list(categories.keys())
    for i in range (len(options)):
        print(f"{i+1}) {options[i]} ")

    choice=int(input("Elija una categoria: "))
    while choice < 1 or choice > len(options):
        choice=int(input("Opcion invalida. Elija una categoria: "))
    categoria=options[choice-1]

    palabras = random.sample(categories[categoria],3)


    puntaje=0
    for palabra in palabras:
        guessed = []
        attempts = 6
        
        








        while attempts > 0:
            # Mostrar progreso: letras adivinadas y guiones para las que faltan
            progress = ""
            for letter in palabra:
                if letter in guessed:
                    progress += letter + " "
                else:
                    progress += "_ "
            print(progress)
            # Verificar si el jugador ya adivinó la palabra completa
            if "_" not in progress:
                print("¡Ganaste!")
                puntaje+=6
                break
            print(f"Intentos restantes: {attempts}")
            print(f"Letras usadas: {', '.join(guessed)}")
            letter = input("Ingresá una letra: ").lower()

            while len(letter) > 1 or not ("a" <= letter <= "z"):
                letter = input("Entrada no válida. Ingrese una letra: ").lower()
            
            if letter in guessed:
                print("Ya usaste esa letra.")
            elif letter in palabra:
                guessed.append(letter)
                print("¡Bien! Esa letra está en la palabra.")
            else:
                guessed.append(letter)
                attempts -= 1
                puntaje-=1
                print("Esa letra no está en la palabra.")
            print()
        else:
            puntaje=0
            print(f"¡Perdiste! La palabra era: {palabra}")
        print(f"Puntaje: {puntaje}")
    
    respuesta=input("Queres jugar de nuevo? (s/n): ").lower()
    while respuesta != "s" and respuesta != "n":
        respuesta=input("Entrada invalida. Queres jugar de nuevo? (s/n): ").lower()
    if respuesta == "s":
        continue
    elif respuesta == "n":
        break
   
        
