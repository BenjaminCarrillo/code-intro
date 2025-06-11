def edad():
    edad=int(input("ingrese edad= "))
    if edad>17:
        print("usted es mayor de edad")
    elif (edad>0) and (edad<18):
        print("usted es menor de edad")
edad()