# Importamos la libreria math la que nos  va a permitir realizar la conversion de la resolucion
import math


# Funcion que recibe parametro x, y los cuales los  pasamos  a una tupla
def convert(x: int, y: int) -> tuple:
    new_width = math.ceil(y * (16 / 9)) #math.ceil nos permite redondear el valor decimal al entero mas cercano

    return new_width, y # retornamos los valores


# probamos que sea correcto
x = int(input("Ingresa el valor de x "))
y = int(input("Ingresa el  valor de y "))
# le pasamos los parametros a la funcion en este caso los valores de x y y
new_resolution = convert(x, y)

#Imprimimos  la resolucion original y la convertida
print(f"Original resolution: {x}x{y}")
print(f"New Resolution with 16.9 aspect ratio: {new_resolution[0]}x{new_resolution[1]}")
