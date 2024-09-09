def find_third_angle(angle1: int, angle2: int) -> int:
    # La suma de los ángulos internos de un triángulo es 180 grados
    return 180 - (angle1 + angle2)

# Ejemplo de uso
angle1 = int(input("Ingresa el primer ángulo: "))
angle2 = int(input("Ingresa el segundo ángulo: "))

# pasamos a una variable el resultado de el calculo que hace la funcion pasandole los parametros
third_angle = find_third_angle(angle1, angle2)
print(f"El tercer ángulo es: {third_angle}")
