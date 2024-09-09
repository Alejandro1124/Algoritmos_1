def calcular_presion_total(M1, M2, m1, m2, V, T):
    # Convertir temperatura de °C a K
    T_K = T + 273.15

    # Calcular el número de moles de cada gas
    moles_gas1 = m1 / M1
    moles_gas2 = m2 / M2

    # Calcular el número total de moles
    total_moles = moles_gas1 + moles_gas2

    # Constante de gas
    R = 0.082

    # Calcular la presión total
    P_total = (total_moles * R * T_K) / V

    return P_total

# Leer los valores del usuario y convertirlos a los tipos adecuados
M1 = float(input("Ingresa la masa molar del gas 1 en g/mol: "))
M2 = float(input("Ingresa la masa molar del gas 2 en g/mol: "))
m1 = float(input("Ingresa la masa del gas 1 en gramos: "))
m2 = float(input("Ingresa la masa del gas 2 en gramos: "))
V = float(input("Ingresa el volumen del recipiente en dm^3: "))
T = float(input("Ingresa la temperatura en °C: "))

# Calcular y mostrar la presión total
presion_total = calcular_presion_total(M1, M2, m1, m2, V, T)
print(f"La presión total es: {presion_total:.2f} atm")



#
# # Ejemplo de uso:
# M1 = 32  # Molar masa del gas 1 en g/mol (por ejemplo, Oxígeno)
# M2 = 44  # Molar masa del gas 2 en g/mol (por ejemplo, Dióxido de Carbono)
# m1 = 64  # Masa del gas 1 en gramos
# m2 = 88  # Masa del gas 2 en gramos
# V = 10  # Volumen del recipiente en dm^3
# T = 25  # Temperatura en °C
