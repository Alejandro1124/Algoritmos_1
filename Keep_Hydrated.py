import math


def calcular_litros():
    # Pedir al usuario que ingrese el tiempo
    time = float(input("Introduce el tiempo en horas: "))

    # Calcular los litros de agua consumidos y redondear hacia abajo
    litros = math.floor(time * 0.5) #math.floor() redondea el resultado al entero de menor valor  mas cercano

    # Imprimir el resultado
    print(f"Nathan beberá {litros} litros de agua porque entreno {time} horas.")


# Llamar a la función
calcular_litros()
