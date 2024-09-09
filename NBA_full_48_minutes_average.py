
#funcion que calcula la extrapolacion de un jugador en la NBA dependiendo cuanto juegue y cuanot spuntos haga
def nba_extrap(ppg, mpg):
    if mpg == 0:
        return 0
    else:
        ppg_48 = (ppg * 48) / mpg
        return round(ppg_48, 1)

# Leer los valores desde la consola
ppg = float(input("Ingresa los puntos por juego (ppg): "))
mpg = float(input("Ingresa los minutos por juego (mpg): "))

# Calcular y mostrar la extrapolación
ppg_48 = nba_extrap(ppg, mpg)
print(f"Extrapolación de puntos por juego a 48 minutos: {ppg_48}")
