#Funcion que calcula los descuentos de los mangos
def mango(quantity, price):
    return price * (quantity - (quantity // 3)) #(quantity // 3)) Inidica caintos grupos de mangos hay

# Ejemplos
print(mango(5, 3))   # Debería imprimir 12
print(mango(10, 5))   # Debería imprimir 30
"""
Ejemplos de funcionamiento
mango(5, 3):
Grupos de 3: 5 // 3 = 1
Mangos que pagas: 5 - 1 = 4
Precio total: 4 * 3 = 12
mango(9, 5):
Grupos de 3: 9 // 3 = 3
Mangos que pagas: 9 - 3 = 6
Precio total: 6 * 5 = 30

"""

#El operador // en Python se llama división entera (o floor division en inglés). Este operador divide dos números y
# devuelve el resultado entero redondeado hacia abajo (o hacia el menor valor entero), eliminando cualquier parte decimal.