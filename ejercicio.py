adventurers={
} 
esta=False
def reg_adventurer(adventurers,codigo,datos):
    if codigo not in adventurers:
        adventurers[codigo]= {
            'nombre':datos[0],
            'edad':datos[1],
            'puntaje':[]
        }
        return True
    else:
        print("ese codigo ya existe")
        return False
def ing_puntaje(adventurers,codigo,puntaje):
    if codigo in adventurers: 
        adventurers[codigo]['puntaje'].append(puntaje) 
        return True
    else:
        return False
def mod_puntaje(adventurers,codigo,sesion):
    try:
        puntaje=int(input("ingresa el nuevo puntaje"))
    except:
        try:
            puntaje=int(input("ingresa el nuevo puntaje"))
        except:
            print("ingrese un numero valido")
    adventurers[codigo]['puntaje'][sesion-1]=puntaje
while True:
    print("1. Registrar Aventurero.")
    print("2. Registrar puntaje.")
    print("3. Modificar un puntaje.")
    print("4. total acumulado y promedio.")
    print("5. Ver aventureros con bajo promedio.")
    print("6. Lista de aventureros con datos y puntajes.")
    print("7. aventureros por edad.")
    print("8. SALIR.")
    opcion=input("Ingresa una opcion= ")
    if opcion=="1":
        codigo=input("ingrese su codigo unico= ")
        nombre=input("ingresa tu nombre= ")
        try:
            edad= int(input("ingrese su edad= "))
        except:
            while True:
                try:
                    edad=int(input("ingresa un numero valido= "))
                    break
                except:
                    print("siga intentando")
        if reg_adventurer(adventurers,codigo,[nombre,edad]):
            print("se registro con exito")
        else:
            print("no se pudo registrar por que el usuario ya existe")
        
    if opcion=="2":
        codigo=input("ingresa tu codigo unico= ")
        try:
            puntaje=int(("ingrese su puntaje= "))
        except:
            while True:
                try:
                    puntaje=int(input("ingrese el puntaje= "))
                    break
                except:
                    print("ingrese un numero= ")
        ing_puntaje(adventurers,codigo,puntaje)
        elif esta==False:
            print("el usuario no existe")
        lenght=len(adventurers[codigo]['puntaje']) 
        print(f"{lenght} de longitud")
    if opcion=="3":
        codigo=input("ingrese codigo ")
        if codigo in adventurers:
            esta==True
            try:
                sesion=int(input("ingrese el numero de la sesion"))
            except:
                while True:
                    try: 
                        sesion=int(input("ingrese el numero de la sesion"))
                    except:
                        print("ingrese un numero")
            lenght=len(adventurers[codigo]['puntaje']) 
            if sesion<=lenght: 
                mod_puntaje(adventurers,codigo,sesion)
            else:
                print("la sesion no existe")
        elif esta==False:
            print("el usuario no existe")
    if opcion=="4":
        for i in adventurers[codigo]:
            for n in adventurers[codigo]['puntaje']:
                print(i,n)
    if opcion==5:
        pass
    if opcion==6:
        pass
    if opcion==7:
        pass
    if opcion==8:
        pass
    print (adventurers)
    


