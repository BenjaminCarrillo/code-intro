def sumatoria():
    contador=0
    suma=0
    while contador<15:
        contador +=1
        num=int(input(f"ingrese numero {contador}"))
        suma +=num
    print (suma)
sumatoria()