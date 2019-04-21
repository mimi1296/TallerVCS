#El problema es realizar un programa que indique si el nÃºmero es positivo o negativo
#Usar primero ciclos y despues usar recursividad
#Entradas: eval(Numero a probar) int(Las veces que se va a probar los numeros)
#Salidas: str (Es positibo) str(Es negativo) str(El cero no tiene signo)
#Restricciones: Ninguna
#Pseudocodigo: Si un numero es mayor a cero, entonces el numero es positivo,
#si el numero es menor a cero, entonces el numero es negativo.
#Si el numero es igual a cero, entonces el numero no tiene signo, porque
#el cero no tiene signo.
def signo ():
    numeros = int(input("Indique la cantidad de numeros a probar "))
    contador = 1
    while contador != numeros:
        prueba = eval(input("Escriba un numero de prueba "))
        if prueba > 0:
            print("El numero es positivo\n")
        elif prueba < 0:
            print("El numero es negativo\n")
        elif prueba == 0:
            print ("El cero no tiene signo")
        else:
            print("numero invalido")
        contador = contador + 1
signo()
def signo2 (numeros):
    prueba = int(input("Escriba un numero de prueba "))
    if numeros == 0:
        return 0
    elif prueba == 0:
        print ("El cero no tiene signo")
        return 0
    elif prueba > 0:
        print ("El numero es positivo\n")
        return signo2 (numeros-1)
    elif prueba < 0:
        print ("El numero es negativo\n")
        return signo2 (numeros-1)
    else:
        print ("numero invalido")
        return signo2 (numeros-1)
numeros = int(input("Indique la cantidad de numeros a probar"))
signo2(numeros)

#Punto B
#El problema, es indicar el MCD entre dos numeros.
#Entradas: int(Primero numero) int(Segundo numero)
#Salidas: int(El maximo comun divisor)
#Restricciones: si es cero se retorna la funcion
#Pseudocodigo: El usuario intreduce el primer numero, despues introduce el segundo,
#siguiendo a esto, se imprime el MCD

def MCD(num1,num2):
    if num2 == 0:
        return num1
    return MCD(num2, num1 % num2)
num1 = int(input("Introduce el primer numero: "))
num2 = int(input("Introduce el segundo numero: "))

print("El maximo comun divisor de ", num1," y ", num2," es ", MCD(num1, num2))