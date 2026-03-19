N=int(input("Ingrese un numero N: "))
multiplos=[]
noMultiplos=[]
for i in range(1,N+1):
    if (i%5 == 0):
        multiplos.append(i)
        continue
    noMultiplos.append(i)
    print(i)

print(f" Lista de multiplos de 5: {multiplos}")
print(f"Lista de NO multiplos : {noMultiplos}")
      
      
       