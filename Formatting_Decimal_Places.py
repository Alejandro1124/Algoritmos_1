def round_to_two_decimal_places(number):
    """
    Redondea un número a dos decimales.

    Parámetros:
    number (float): El número a redondear

    Retorna:
    str: El número redondeado a dos decimales en formato de cadena
    """
    # Redondear el número a dos decimales
    rounded_number = round(number, 2)
    # Formatear el número a dos decimales como cadena
    return f"{rounded_number:.2f}"

# Solicitar al usuario que ingrese un número
input_number = float(input("Ingresa un número: "))

# Redondear y mostrar el número
formatted_number = round_to_two_decimal_places(input_number)
print(f"El número redondeado es: {formatted_number}")
