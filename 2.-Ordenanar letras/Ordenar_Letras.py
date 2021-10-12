Letras = ["C", "D", "A", "E", "B"]

for posicion in range(0,len(Letras)):
    for recorrido in range(posicion+1, len(Letras)):
        if(Letras[recorrido]<Letras[posicion]):
            x=Letras[posicion]
            Letras[posicion]=Letras[recorrido]
            Letras[recorrido]=x  
    print(Letras)