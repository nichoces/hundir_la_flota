# Importamos las librerias necesarias
import numpy as np
import random

# Creamos la funcion para colocar barcos
def colocar_barcos(tablero, barcos): # Tenemos en cuenta los parametros tablero y barcos, de tal manera
    for longitud, cantidad in barcos.items(): # que se introduce el tablero que se desea colocar en el Main.py
        for _ in range(cantidad):
            barco_colocado = False # Por defecto, no estan colocados los barcos
            while not barco_colocado: # Mientras no esten colocados se ejecutará el bucle infinitamente
                fila = np.random.randint(0, 10)
                columna = np.random.randint(0, 10)
                direccion = np.random.choice(["horizontal", "vertical"]) # Elejimos las horientaciones
                if direccion == "horizontal":
                    # while fila -1 == 0 or fila+1 == 0 or columna-1 == 0 or columna +1 ==0:
                        if columna + longitud <= 10 and np.all(tablero[fila, columna:columna+longitud] == 0):
                            tablero[fila, columna:columna+longitud] = 1
                            barco_colocado = True
                else:
                    # while fila -1 ==0 or fila+1 ==0 or columna-1 ==0 or columna +1 ==0:
                        if fila + longitud <= 10 and np.all(tablero[fila:fila+longitud, columna] == 0):
                            tablero[fila:fila+longitud, columna] = 1
                            barco_colocado = True
                            


# Creamos las funciones para mostrar los tableros
def mostrar_tablero(tablero):
    print(tablero)
def mostrar_tablero_revelar():
    print(tablero_revelar)
def mostrar_tablero_misbarcos():
    print(tablero_misbarcos)


# Creamos la funcion para cuando se hunda un barco
def barco_hundido(tablero, fila, columna):
    if tablero[fila, columna] == 1:
        # para todos los casos en los que haya impacto
        if columna < 9 and tablero[fila, columna+1] == 1:
            #si a la derecha del impacto hay otro trozo de barco
            inicio = columna
            fin = columna + 1
            while fin < 9 and tablero[fila, fin+1] == 1:
                fin += 1
            return np.all(tablero[fila, inicio:fin+1] == -1)
        elif fila < 9 and tablero[fila+1, columna] == 1:
            inicio = fila
            fin = fila + 1
            while fin < 9 and tablero[fin+1, columna] == 1:
                fin += 1
            return np.all(tablero[inicio:fin+1, columna] == -1)
    return False

# Creamos los tableros sobre los que se juega
tablero_jugador = np.zeros((10, 10))
tablero_maquina = np.zeros((10, 10))

# Creamos los tableros con strings para visualizarlo mejor
tablero_revelar = np.full((10, 10)," ")
tablero_misbarcos = np.full((10,10)," ")

# Creamos la funcion mis barcos para traducir nuestro tablero (jugador) en una matriz con Strings

def misbarcos():
    for fila in  range(len(tablero_jugador)):
        for columna in range(len(tablero_jugador)):
            if tablero_jugador[fila,columna] == 1 : # Si el tablero de zeros es uno quiere decir que hay un barco
                tablero_misbarcos[fila,columna]='#' # Se representa con el simbolo indicado
            elif tablero_jugador[fila,columna]==0: # Si es 0 ponemos una A indicando agua
                tablero_misbarcos[fila,columna]='A'
            elif tablero_jugador[fila,columna] == -1: # Si es -1 han tocado el barco y se sustituye por X
                tablero_misbarcos[fila,columna]='X'


# Creamos los barcos con los que se van a jugar siendo longitud-cantidad 
barcos_jugador = {1: 4, 2: 3, 3: 2, 4: 1}
barcos_maquina = {1: 4, 2: 3, 3: 2, 4: 1}





