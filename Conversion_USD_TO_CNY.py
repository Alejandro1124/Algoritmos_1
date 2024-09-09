
#x: int indica que el parámetro x debe ser de tipo entero.
# -> str indica que la función va a devolver un valor de tipo cadena de texto (string).

def conversionFunction(x: int) -> str:

    # Definimos la tasa de conversión
    conversion_rate = 6.75

    # Realizamos la conversión
    conversion = x * conversion_rate

    # Retornamos la conversión formateada a 2 decimales seguida de 'Chinese Yuan'
    return f"{conversion:.2f} Chinese Yuan"


# Solicitamos la cantidad de USD al usuario
x = int(input("Ingresa los dólares a convertir: "))

# Obtenemos el resultado de la conversión
result = conversionFunction(x)

# Imprimimos el resultado
print(result)
