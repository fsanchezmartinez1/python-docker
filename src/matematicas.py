import sys

def calcularFactorial(numero):   
    factorial = 1
    for i in range(2,int(numero)+1):
        factorial = factorial * i
    return factorial

def calcularCuadrado(numero):
    resultado = numero * numero
    return resultado

def calcularBinario(numero):
    resultado = bin(numero)
    return resultado


funcion = sys.argv[1]
numero = int(sys.argv[2])

if(funcion == 'factorial'):
    resultado = calcularFactorial(numero)
    print(resultado)
elif(funcion == 'cuadrado'):
    resultado = calcularCuadrado(numero)
    print(resultado)
elif(funcion == 'binario'):
    resultado = calcularBinario(numero)
    numeroBinario = resultado.replace('0b','')
    print(str(int(numeroBinario,base=2))+"="+numeroBinario)
else:
    print("no has elegido una opcion válida")

