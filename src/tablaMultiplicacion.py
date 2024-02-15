import random

numero = 7

for i in range(1,11):
    print(str(numero)+"x"+str(i)+"="+str(numero*i))


numeroPreguntas = 10


multiplicando = random.randint(1,10)
respuesta = input("¿Cual es el resultado de multiplicar "+str(numero)+"x"+str(multiplicando)+"=")

if(int(respuesta) == numero*multiplicando):
    print("Muy bien")
else:
    print("Muy mal")
