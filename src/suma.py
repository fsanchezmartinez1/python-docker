

# Método que calcula la media de un listado donde cada posición del array tiene dos posiciones,
# la primera con el nombre, y la segunda con la nota
def calcularMedia(lista):
    suma = 0
    for numero in lista:
        suma = suma + numero[1]
    return suma/len(lista)

def mejorAlumnos(lista):
    notaMaxima = 0
    mejorAlumno = []
    for alumno in lista:
        if(alumno[1]>notaMaxima):
            mejorAlumno = alumno
            notaMaxima = alumno[1]
    return mejorAlumno



# Creamos la lista de alumnos con sus correspondientes notas
listaNumeros = [
        ["alumno 1",5],
        ["alumno 2",6],
        ["alumno 3",10],
        ["alumno 4",2],
    ]

alumno = mejorAlumnos(listaNumeros)
print(alumno[0]+":"+str(alumno[1]))




