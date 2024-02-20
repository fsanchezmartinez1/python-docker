

def cuentaLetra(frase, letraBuscada):
    contadorLetra = 0
    for letra in frase:
        if(letra == letraBuscada):
            contadorLetra = contadorLetra + 1
    print("Hay un total de "+str(contadorLetra)+" '"+letraBuscada+"'")


# input("introduce tu frase")
username = "Elvhg        texto deberia     de ser       claro"
# letraBuscada = input("Introduce que letra quieres contar")

while username.find("  ") != -1:
    username = username.replace("  "," ")
#
    
cuentaLetra(username,"o")


print(username)
