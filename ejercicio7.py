def valid(name):
    length=len(name)
    if length>6:
        print ("el nombre es valido")
    else:
        print ("el nombre no es valido")
def namepet():
    name=input("ingresa un nombre= ")
    valid(name)
namepet()
