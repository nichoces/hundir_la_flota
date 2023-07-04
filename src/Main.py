# Importamos tanto los objetos creados como las librerias
import objetosy_y_funciones as of
import numpy as np

# Colocamos los barcos llamando a la funcion.
of.colocar_barcos(of.tablero_jugador, of.barcos_jugador)
of.colocar_barcos(of.tablero_maquina, of.barcos_maquina)

# Contabilizamos las coordenadas en las que se ha tirado.
Lista_jugador=[]


# Comienza el bucle de juego.
while True:
    print("----- TURNO DEL JUGADOR -----")
    of.misbarcos()
    of.mostrar_tablero(of.tablero_misbarcos)
    print("----- TABLERO A REVELAR -----")
    print(of.tablero_revelar)
    fila = int(input("Ingrese la fila: "))
    columna = int(input("Ingrese la columna: "))
    Lista_jugador.append(fila*10 + columna)
    if of.tablero_revelar[fila, columna] == "X" or of.tablero_revelar[fila,columna]=='A':
        print(np.random.choice(["Ya has tirado en estas coordenadas, marinero de agua dulce","mi abuela es tuerta y atinaría mejor que tú. ¡Ya has tirado allí!","Grumete, disparando en el mismo sitio no generaremos nuevos daños, estudia mejor la situación."]))
        continue
    elif of.tablero_maquina[fila, columna] == 1:
        of.tablero_maquina[fila, columna] = -1
        if not 1 in of.tablero_maquina:
                print("¡Has ganado!")
                break
        elif of.tablero_maquina[fila,columna]==1:
            print("Tocado")
            of.tablero_revelar[fila,columna] = str("X")
            
    else:
        print("Agua")
        of.tablero_revelar[fila,columna] = str("A")

    print("----- TURNO DE LA MÁQUINA -----")
    fila = np.random.randint(0, 10)
    columna = np.random.randint(0, 10)
    while True:
        if of.tablero_jugador[fila, columna] == -1 or of.tablero_jugador[fila,columna]== 7:
            continue
        elif of.tablero_jugador[fila, columna] == 1:
            of.tablero_jugador[fila, columna] = -1
            if not 1 in of.tablero_jugador:
                print("¡La máquina ha ganado!")
                break
            elif of.tablero_jugador[fila,columna] == 1:
                print("Tocado. \nLa máquina ha disparado en la fila %s y en la columna %s" % (fila,columna))
                
            elif not 1 in of.tablero_jugador:
                    print("¡La máquina ha ganado!")
                    break
        else:
            of.tablero_jugador[fila,columna]= 7
            print("Agua. \nLa máquina ha disparado en la fila %s y en la columna %s" % (fila,columna))
            break
    



