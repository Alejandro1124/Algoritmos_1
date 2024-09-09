#Calcula la edad del perro y el gato en años humanos


def calculate_pet_ages(humanYears):


    # Inicializamos las edades de gato y perro en 0
    catYears = 0
    dogYears = 0

    # Condición para el primer año
    if humanYears >= 1:
        catYears += 15
        dogYears += 15

    # Condición para el segundo año
    if humanYears >= 2:
        catYears += 9
        dogYears += 9

    # Condición para los años restantes (3 en adelante)
    if humanYears > 2:
        catYears += (humanYears - 2) * 4
        dogYears += (humanYears - 2) * 5
#Devuelve una lista con los años humanos lo años perro y los años gato
    return [humanYears, catYears, dogYears]


# Ejemplo de uso
#Establecemos los años en el ejemplo
humanYears = int(input("ingresa los años  "))
#llama a la funcion y lo asiga a la variable ages
ages = calculate_pet_ages(humanYears)
#Imprime Ages
print(ages)
print(f"los años del Humano son {humanYears}")
print(f"los años del gato son {ages[1]}")
print(f"los años del perro son {ages[2]}")


