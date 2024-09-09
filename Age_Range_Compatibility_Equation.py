import math  # Importa el módulo math para usar la función floor()


def age_range(age):
    """
    Calcula el rango de edad mínimo y máximo basado en la edad dada.

    Parámetros:
    age (int): Edad de la persona, 1 <= age <= 100

    Retorna:
    str: Rango de edad en el formato "min-max"
    """

    # Si la edad es menor o igual a 14, usa la fórmula dada
    if age <= 14:
        # Calcula el rango mínimo, redondeado hacia abajo
        min_age = math.floor(age - 0.10 * age)
        # Calcula el rango máximo, redondeado hacia abajo
        max_age = math.floor(age + 0.10 * age)
    else:
        # Para edades mayores a 14, usa la misma fórmula
        min_age = math.floor(age - 0.10 * age)
        max_age = math.floor(age + 0.10 * age)

    # Retorna el rango de edad en el formato "min-max"
    return f"{min_age}-{max_age}"


# Solicitar al usuario que ingrese la edad
age = int(input("Ingresa la edad (1 <= edad <= 100): "))

# Verificar que la edad está dentro del rango permitido
if 1 <= age <= 100:
    # Calcular y mostrar el rango de edad
    rango_edad = age_range(age)
    print(f"El rango de edad es: {rango_edad}")
else:
    print("La edad ingresada no está en el rango permitido (1 a 100).")

    #Cambio numero 2

