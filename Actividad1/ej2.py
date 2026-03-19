segs= int(input("Ingrese una cantidad de segundos: "))

def Hours(segs):
    hora=int(segs/3600)
    
    return hora

def Minutes(segs):
    
    segs-= Hours(segs)*3600
    mins=int(segs/60)
  
    return mins

print(f" Esa cantidad equivale a {Hours(segs)} HORAS , Esa cantidad equivale a {Minutes(segs)} MINUTOS , Esa cantidad equivale a {int(segs-Hours(segs)*3600-Minutes(segs)*60)} SEGUNDOS")