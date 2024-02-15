import random

numeroPreguntas = random.randint(1,8)

aciertos = 0 
fallos = 0
for i in range(1,numeroPreguntas+1):
    numero = random.randint(2,9)
    multiplicando = random.randint(1,10)
    respuesta = input("¿Cual es el resultado de multiplicar "+str(numero)+"x"+str(multiplicando)+"=")

    if(int(respuesta) == numero*multiplicando):
        aciertos = aciertos + 1
    else:
        fallos = fallos + 1


nota = (aciertos*10)/numeroPreguntas

print("El resultado obtenido es de "+str(aciertos)+" aciertos")
print("Tu nota es de "+str(nota))