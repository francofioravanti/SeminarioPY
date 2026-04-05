students = [
    {"name": " Ana García ", "grade": "8", "status": "aprobado"},
    {"name": "pedro lópez", "grade": "4", "status": "DESAPROBADO"},
    {"name": "MARÍA FERNÁNDEZ", "grade": "10", "status": "Aprobado"},
    {"name": "ana garcía", "grade": "9", "status": "aprobado"},
    {"name": None, "grade": "7", "status": "aprobado"},
    {"name": "Luis Martínez ", "grade": None, "status": "aprobado"},
    {"name": " carlos RUIZ", "grade": "6", "status": "aprobado"},
    {"name": "PEDRO LÓPEZ ", "grade": "3", "status": "desaprobado"},
    {"name": " ", "grade": "5", "status": "aprobado"},
    {"name": "María Fernández", "grade": "7", "status": "APROBADO"},
    {"name": "Sofía Torres", "grade": "9", "status": "Aprobado"},
    {"name": " sofía torres ", "grade": "8", "status": "aprobado"},
    {"name": "Carlos Ruiz", "grade": "6", "status": "APROBADO"},
    {"name": "Roberto Díaz", "grade": "absent", "status": "ausente"},
    {"name": "roberto díaz", "grade": "", "status": "Ausente"},
    {"name": None, "grade": None, "status": None},
    {"name": "Laura Méndez", "grade": "7", "status": "aprobado"},
    {"name": " laura méndez", "grade": "8", "status": "Aprobado"},
    {"name": "GABRIELA RÍOS", "grade": "5", "status": "aprobado"},
    {"name": "gabriela ríos ", "grade": "4", "status": "Desaprobado"},
]

lista=[]

for student in students :


    #Eliminar registros con nombre nulo, vacío o solo espacios.
    if student['name'] == None or student['name'] == "" or student['name'] == " ":
        continue

    else:
        #Eliminar registros con nota nula, vacía o no numérica (como "absent").
        if student['grade'] == None  or  not student['grade'].isdigit() or student['grade'] == "" or student['grade'] == " ":
            continue

    #Normalizar nombres a formato título y estados a formato título.

    if student['name'].istitle() != True  :
        student['name']=student['name'].strip().title()
    
    if student['status'] == None or student['status'] == "" or student['status'] == " ":
        continue
    elif student['status'].istitle() != True:
        student['status']=student['status'].strip().title()
    
    #Eliminar duplicados por nombre, quedándose con la nota más alta de cada alumno.

    

    existe=False
    
    for i,estudiante in enumerate(lista):
        if student['name'].strip() == estudiante['name'].strip() :
            existe=True
            if int(student['grade']) > int(estudiante['grade']):
                lista[i]=student
    if not existe:
        lista.append(student)


lista_ordenada=sorted(lista, key=lambda s: s['name'])

for student in lista_ordenada:
    print(f"{student} \n")


    

    
        
        

    









