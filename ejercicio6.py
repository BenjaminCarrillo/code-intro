def operaciones():
    num1= int(input("ingresa el primer numero= "))
    num2= int(input("ingresa el segundo numero= "))
    if(num1!=0)and(num2!=0):
        suma=num1+num2
        resta=num1-num2
        multi=num1*num2
        divid=num1/num2
        print(f"{num1}+{num2}= {suma}")
        print(f"{num1}-{num2}= {resta}")
        print(f"{num1}x{num2}= {multi}")
        print(f"{num1}/{num2}= {divid}")
operaciones()