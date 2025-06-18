def impares(num1,num2):
    suma=0
    while num1<num2:
        num1 +=1
        if num1 % 2 != 0:
            suma = suma + num1
    return suma
num1=int(input("ingresa un numero"))
num2=int(input("ingresa un numero mayor al primero"))
print (impares(num1,num2))
