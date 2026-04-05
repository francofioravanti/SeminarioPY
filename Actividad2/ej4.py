email= input("Ingrese un email: ")

condicion4= email[0] != "@" and email[-1] !="@"

condicion1= email.count("@")==1 

email.split("@")
condicion2=len(email[0])>=1


condicion3=email[1].count(".")>=1

" ".join(email)

email.split(".")
condicion5= len(email[-1]) >= 2

if condicion1 and condicion2 and condicion3 and condicion4 and condicion5:
    print("es validoooo")
else:
    print("no es validoooo")