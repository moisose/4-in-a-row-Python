# Librerias importadas
import tkinter as tk
from tkinter import messagebox
import time
import random

# Variables globales paralas funciones
# ______________________________________________________________________________________________________________________
ganadores = []
jugadores = []
guardar_partida = []
id_partida = 0

# Variable que controla el turno, si es True es el jugador 1, False el jugador 2
turno = True

# Cantidad de turnos jugados en la partida
numero_turnos = 0

# Default activa loas funciones por defecto
default = True

# Nombre de los jugadores
jugador1 = []  # Nombre de los jugadores
jugador2 = []

# Activa el modo computadora
modo_computadora = False
computadora = False
combinaciones = []

# Variables de ganadores
ganaJ1 = False
ganaJ2 = False
gana_computadora = False

# Color de los jugadores
color_jugador = 'red'

# Indices de la matriz mostrada
izq = 7  # Posición en la matriz izq
der = 14  # Posición en la matriz der
fil_u = 0  # Posición de la fila arriba
fil_d = 6  # Posición de la fila abajo
contador_arriba = 0  # Contador de espacios que hay arriba de la vista de cuadrícula

# Indices para los numeros de las dilas y columnas
list_column_i = 7
list_column_d = 14
list_row_u = 0
list_row_d = 6


# Comenzar el juego
juego_Comenzado = False

# Lista de indices de las filas de la matriz
# -7, -6, -5, -4, -3, -2, -1 (se añaden a la izquierda si se expande a la izquierda, igual hacia la derecha)
lista_indice_filas = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 17, 18, 19, 20,]

# Matriz logica infinita
matriz = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

# Lista indice de las columnas de la matriz
lista_indice_columnas = [-7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,]

# Matriz de botones (5 filas por 7 columnas)
boton = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
]

# Matriz para controlar el color y el nombre
colores = [[0, 0, 0], [0, 0, 0]]
nombres = [[0,0],[0,0]]

# Indices de las filas y las columnas
indices_columnas = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
indice_filas = [[0], [0], [0], [0], [0], [0]]
# ---------------------------------------------
# Colores de la interfaz
color = '#EEEEEE'
color2 = '#FFFEF2'

# ______________________________________________________________________________________________________________________

# Guardar partida
# Ibtiene los datos de todas las variables globales y los guarda en un archivo para que los datos no se pierdan 
def guardar_partida_empezada():
    global guardar_partida
    global turno
    global numero_turnos
    global id_partida

    global matriz

    global jugador1
    global jugador2

    global ganaJ1
    global ganaJ2
    global gana_computadora
    global color_jugador

    global izq
    global der
    global fil_u
    global fil_d
    global contador_arriba

    global list_column_i
    global list_column_d
    global list_row_u
    global list_row_d

    global computadora
    global modo_computadora
    global combinaciones
    global disponibles

    global default
    #default = False
    numero_turnos = 0

    fecha = time.strftime('%H:%M:%S / %d-%m-%Y', time.localtime())

    ids_usados = []
    for i in guardar_partida:
        ids_usados.append(i[0])
    print(ids_usados)

    if id_partida in ids_usados:
        default = False
        guardar_partida[id_partida-1] = [(id_partida), fecha, turno, numero_turnos, jugador1, jugador2, ganaJ1, ganaJ2, color_jugador, izq, der, fil_u, fil_d, contador_arriba, list_column_i, list_column_d, list_row_u, list_row_d, default, matriz, computadora, modo_computadora, combinaciones, disponibles, gana_computadora]
        guardar('guardar_partida.txt', guardar_partida) 
        mensaje_emergente('Información','La partida ha sido guardada con éxito.')

    else:
        default = False
        datos_guardar = [id_partida, fecha, turno, numero_turnos, jugador1, jugador2, ganaJ1, ganaJ2, color_jugador, izq, der, fil_u, fil_d, contador_arriba, list_column_i, list_column_d, list_row_u, list_row_d, default, matriz, computadora, modo_computadora, combinaciones, disponibles, gana_computadora]
        
        guardar_partida.append(datos_guardar)
        guardar('guardar_partida.txt', guardar_partida) 
        mensaje_emergente('Información','La partida ha sido guardada con éxito.')            

# Cargar partida empezada
# E: numero
# S: none
# Recibe el numero de la oartida y carga los datos en el juego para seguir jugando
def cargar_partida_empezada(num):
    
    global guardar_partida
    global turno
    global numero_turnos
    global id_partida

    global matriz

    global jugador1
    global jugador2

    global ganaJ1
    global ganaJ2
    global gana_computadora
    global color_jugador

    global izq
    global der
    global fil_u
    global fil_d
    global contador_arriba

    global list_column_i
    global list_column_d
    global list_row_u
    global list_row_d

    global default
    default = False
    global computadora
    global modo_computadora
    global combinaciones
    global disponibles

    print ('holaaaaa')
    print(num)
    id_partida = guardar_partida[num][0]
    turno = guardar_partida[num][2]
    numero_turnos = guardar_partida[num][3]
    jugador1 = guardar_partida[num][4]
    jugador2 = guardar_partida[num][5]
    ganaJ1 = guardar_partida[num][6]
    ganaJ2 = guardar_partida[num][7]
    color_jugador = guardar_partida[num][8]
    izq = guardar_partida[num][9]
    der = guardar_partida[num][10]
    fil_u = guardar_partida[num][11]
    fil_d = guardar_partida[num][12]
    contador_arriba = guardar_partida[num][13]
    list_column_i = guardar_partida[num][14]
    list_column_d = guardar_partida[num][15]
    list_row_u = guardar_partida[num][16]
    list_row_d = guardar_partida[num][17]
    default = guardar_partida[num][18]

    matriz = guardar_partida[num][19]
    computadora = guardar_partida[num][20]
    modo_computadora = guardar_partida[num][21]
    combinaciones = guardar_partida[num][22]
    disponibles = guardar_partida[num][23]
    gana_computadora = guardar_partida[num][24]

    print (matriz)

    abrirVentana2()

# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------
# Archivos

# CHECK FILE EXISTANCE
# E: el filepath, nombre del archivo
# S: bool
# determina si el archivo existe en la ruta donde se ejecuta el programa
def checkFileExistance(filePath):
    try:
        with open(filePath, 'r') as f:
            return True
    except FileNotFoundError as e:
        return False
    except IOError as e:
        return False

# CREAR ARCHIVO
# E: filepath, lista
# crea el archivo si no existe en la ruta del .py

def crearArchivo(filePath, stringToWrite):
    fo = open(filePath, 'w')
    fo.write(str(stringToWrite))
    fo.close()

# GUARDAR INFORMACION EN ARCHIVO
# E: el path, string a guardar
# S: la cantidad de caracteres escritos
# guardar el string deseado en el archivo seleccionado
def guardar(filePath, stringToWrite):
    fo = open(filePath, "w")  # crea el file si no existe
    fo.write(str(stringToWrite))
    fo.close()

# LEER ARCHIVO
# E: file path
# S: string con contenido
# retorna el contenido del archivo
def leer(filePath):
    try:
        fo = open(filePath, 'r')
        resultado = fo.read()
        fo.close()
        return resultado
    except:
        return []

# CARGAR ARCHIVOS
# Carga en las variables globales la información de los archivos
# Si los archivo no existen los crea
def cargarArchivos():
    global jugadores
    global ganadores
    global guardar_partida

    if (
        checkFileExistance("files/jugadores.txt") == False
    ):  # verifica que todos los archivos existan, y si no lo crea
        crearArchivo("files/jugadores.txt", jugadores)
    if checkFileExistance("files/ganadores.txt") == False:
        crearArchivo("files/ganadores.txt", ganadores)
    if checkFileExistance("files/guardar_partida.txt") == False:
        crearArchivo("files/guardar_partida.txt", guardar_partida)

    jugadores = eval(leer("files/jugadores.txt"))
    ganadores = eval(leer("files/ganadores.txt"))
    guardar_partida = eval(leer('files/guardar_partida.txt'))

# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------
# Funciones

# GET NEXT ID
# Obtiene el consecutivo siguiente de la lista de detectives
# E: una lista de listas, donde el primer campo es id
# S: numero
def getNextId(lista):
    actual = 0

    for elemento in lista:
        if elemento[0] > actual:
            actual = elemento[0]
    return actual + 1

# TIENE NUMEROS EL NOMBRE
# E: string
# S: bool
# Determina si el string tiene numeros
def tieneNumeros(strValue):
    for elem in strValue:
        if isNumber(elem):
            return True
    return False

# IS INTEGER
# E: string
# S: bool
# Determina si el valor es un numero entero
def isInteger(strValue):
    try:  # intentar hacer estas lineas

        intValue = eval(strValue)

        if type(intValue) == int:
            return True
        else:
            return False
    except:
        # si hay exception o error en ejecucion, pasa al except y ejecuta las intrucciones de alli

        return False

# IS NUMBER
# E: string
# S: bool
# Determina si el valor es un numero
def isNumber(strValue):
    try:
        numberVar = eval(strValue)
        return type(numberVar) == int or type(numberVar) == float
    except:
        return False

def estaJugador(str):
    global jugadores
    for i in jugadores:
        if i[1] == str:
            return True
    return False

# VERIFICAR DERECHA
# E: matriz, numero
# S: bool
# Retorna True si hay 4 numeros consecutivos en la diagonal derecha
def verificarDiagonalDerecha(matriz, jugador):
    # global matriz

    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            contador = 0
            if matriz[i][j] == jugador:
                contador += 1
                try:
                    if matriz[i + 1][j + 1] == jugador:
                        contador += 1
                        try:
                            if matriz[i + 2][j + 2] == jugador:
                                contador += 1
                                try:
                                    if matriz[i + 3][j + 3] == jugador:
                                        contador += 1
                                        if contador == 4:
                                            print(
                                                'Contador es igual a 4, Jugador: ',
                                                jugador,
                                            )
                                            return True
                                except:
                                    continue
                        except:
                            continue
                except:
                    continue
    return False

# VERIFICAR IZQUIERDA
# E: matriz, numero
# S: bool
# Retorna True si hay 4 numeros consecutivos en la diagonal izquierda
def verificarDiagonalIzquierda(matriz, jugador):
    # global matriz

    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            contador = 0
            if matriz[i][j] == jugador:
                contador += 1
                try:
                    if matriz[i - 1][j + 1] == jugador:
                        contador += 1
                        try:
                            if matriz[i - 2][j + 2] == jugador:
                                contador += 1
                                try:
                                    if matriz[i - 3][j + 3] == jugador:
                                        contador += 1
                                        if contador == 4:
                                            print(
                                                'Contador es igual a 4, Jugador: ',
                                                jugador,
                                            )
                                            return True
                                except:
                                    continue
                        except:
                            continue
                except:
                    continue
    return False

# VERIFICAR VERTICAL
# E: matriz, numero
# S: bool
# Retorna True si hay 4 numeros consecutivos en alguna fila
def verificarDiagonalVertical(matriz, jugador):
    # global matriz

    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            contador = 0
            if matriz[i][j] == jugador:
                contador += 1
                try:
                    if matriz[i + 1][j] == jugador:
                        contador += 1
                        try:
                            if matriz[i + 2][j] == jugador:
                                contador += 1
                                try:
                                    if matriz[i + 3][j] == jugador:
                                        contador += 1
                                        if contador == 4:
                                            print(
                                                'Contador es igual a 4, Jugador: ',
                                                jugador,
                                            )
                                            return True
                                except:
                                    continue
                        except:
                            continue
                except:
                    continue
    return False

# VERIFICAR HORIZONTAL
# E: matriz, numero
# S: bool
# Retorna True si hay 4 numeros consecutivos en alguna columna
def verificarDiagonalHorizontal(matriz, jugador):
    # global matriz

    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            contador = 0
            if matriz[i][j] == jugador:
                contador += 1
                try:
                    if matriz[i][j + 1] == jugador:
                        contador += 1
                        try:
                            if matriz[i][j + 2] == jugador:
                                contador += 1
                                try:
                                    if matriz[i][j + 3] == jugador:
                                        contador += 1
                                        if contador == 4:
                                            print(
                                                'Contador es igual a 4, Jugador: ',
                                                jugador,
                                            )
                                            return True
                                except:
                                    continue
                        except:
                            continue
                except:
                    continue
    return False

# VERIFICAR GANADOR
# E: matriz, numero
# S: bool
# Retorna True si encuentra que el jugador ganó
def ganador(matriz, jugador):
    # global matriz
    if verificarDiagonalHorizontal(matriz, jugador):
        print('verificarDiagonalHorizontal')
        if jugador == 1:
            ganaJ1 = True
        else:
            ganaJ2 = True
        return True
    elif verificarDiagonalVertical(matriz, jugador):
        print('verificarDiagonalVertical')
        if jugador == 1:
            ganaJ1 = True
        else:
            ganaJ2 = True
        return True
    elif verificarDiagonalDerecha(matriz, jugador):
        print('verificarDiagonalDerecha')
        if jugador == 1:
            ganaJ1 = True
        else:
            ganaJ2 = True
        return True
    elif verificarDiagonalIzquierda(matriz, jugador):
        print('verificarDiagonalIzquierda')
        if jugador == 1:
            ganaJ1 = True
        else:
            ganaJ2 = True
        return True
    else:
        return False

#-----------------------------
# Verifiar siete derecha
# E: 2 numeros
# Verifica que las jugadas solo se puedan hacer a 7 espacios a la derecha de una ficha jugada
def verificarSieteDerecha(num, j):
    global matriz
    #contador_arriba = 0
    global contador_arriba
    global numero_turnos

    if matriz[(num + contador_arriba)][j] == 0:
        try:
            if (matriz[(num + contador_arriba)][j + 1] == 1 or matriz[(num + contador_arriba)][j + 1] == 2) and numero_turnos > 0:
                return True
        except:
            pass

        try:
            if (matriz[(num + contador_arriba)][j + 2] == 1 or matriz[(num + contador_arriba)][j + 2] == 2) and numero_turnos > 0:
                return True
        except:
            pass

        try:
            if (matriz[(num + contador_arriba)][j + 3] == 1 or matriz[(num + contador_arriba)][j + 3] == 2) and numero_turnos > 0:
                return True
        except:
            pass

        try:
            if (matriz[(num + contador_arriba)][j + 4] == 1 or matriz[(num + contador_arriba)][j + 4] == 2) and numero_turnos > 0:
                return True
        except:
            pass

        try:
            if (matriz[(num + contador_arriba)][j + 5] == 1 or matriz[(num + contador_arriba)][j + 5] == 2) and numero_turnos > 0:
                return True
        except:
            pass

        try:
            if (matriz[(num + contador_arriba)][j + 6] == 1 or matriz[(num + contador_arriba)][j + 6] == 2) and numero_turnos > 0:
                return True
        except:
            pass

        try:
            if (matriz[(num + contador_arriba)][j + 7] == 1 or matriz[(num + contador_arriba)][j + 7] == 2) and numero_turnos > 0:
                return True
        except:
            pass

        if numero_turnos == 0:
            return True

        return False
    return False

# Verifiar siete izquierda
# E: 2 numeros
# Verifica que las jugadas solo se puedan hacer a 7 espacios a la izquierda de una ficha jugada
def verificarSieteIzquierda(num, j):
    global matriz
    #contador_arriba = 0
    global contador_arriba

    if matriz[(num + contador_arriba)][j] == 0:
        try:
            if (matriz[(num + contador_arriba)][j - 1] == 1 or matriz[(num + contador_arriba)][j - 1] == 2) and numero_turnos > 0:
                return True
        except:
            pass

        try:
            if (matriz[(num + contador_arriba)][j - 2] == 1 or matriz[(num + contador_arriba)][j - 2] == 2) and numero_turnos > 0:
                return True
        except:
            pass

        try:
            if (matriz[(num + contador_arriba)][j - 3] == 1 or matriz[(num + contador_arriba)][j - 3] == 2) and numero_turnos > 0:
                return True
        except:
            pass

        try:
            if (matriz[(num + contador_arriba)][j - 4] == 1 or matriz[(num + contador_arriba)][j - 4] == 2) and numero_turnos > 0:
                return True
        except:
            pass

        try:
            if (matriz[(num + contador_arriba)][j - 5] == 1 or matriz[(num + contador_arriba)][j - 5] == 2) and numero_turnos > 0:
                return True
        except:
            pass

        try:
            if (matriz[(num + contador_arriba)][j - 6] == 1 or matriz[(num + contador_arriba)][j - 6] == 2) and numero_turnos > 0:
                return True
        except:
            pass

        try:
            if (matriz[(num + contador_arriba)][j - 7] == 1 or matriz[(num + contador_arriba)][j - 7] == 2) and numero_turnos > 0:
                return True
        except:
            pass
        if numero_turnos == 0:
            return True

        return False
    return False

# -------------------------------------------------------------
# Agregar ganador
# E: numero
# Agrega el ganador a la base de datos, lo guarda en archivos
def agregar_ganador(jugador):
    global ganadores

    ganan = []
    for jug in ganadores:
        ganan.append(jug[0])

    if jugador in ganan:
        for i in ganadores:
            if i[0] == jugador:
                i[1] += 1
                guardar("ganadores.txt", ganadores)
    else:
        gana = [jugador, 1]
        ganadores.append(gana)
        guardar("ganadores.txt", ganadores)


# -------------------------------------------------------------

# CREAR RANGO
# E: 2 numeros
# S: una lista
# Retorna una lista con los números enteros que están en el rango de los dos números dados
def crear_Rango(n1, n2):
    res = []
    while n1 < n2:
        res.append(n1)
        n1 += 1
    return res

    # print(crear_Rango(izq - 7, der - 7))

# Actualizar indices columnas
# Actualiza los indices de las columnas cuandos se mueve la matriz
def actualizar_indices_columnas():
    global lista_indice_columnas
    global indices_columnas
    global list_column_i
    global list_column_d
    valores = crear_Rango(list_column_i - 7, list_column_d - 7)
    print(list_column_i, list_column_d)

    for i in range(0, 1):
        for j in range(0, 7):
            indices_columnas[i][j].config(text=valores[0])
            valores.pop(0)

# Actualizar indices filas
# Actualiza los indices de las filas cuando se mueve la interfaz
def actualizar_indices_filas():
    global list_row_u
    global list_row_d
    valores = crear_Rango(list_row_u, list_row_d)
    print(crear_Rango(list_row_u, list_row_d))

    for i in range(0, 6):
        for j in range(0, 1):
            indice_filas[i][j].config(text=valores[-1])
            valores.pop(-1)

# Cambiar color
# Cambia el color del jugador dependiendo del truno
def cambiar_color():
    global turno
    global jugador1
    global jugador2
    global computadora
    global modo_computadora
    
    if turno:
        colores[0][0].config(bg='red')
    else:
        colores[0][0].config(bg='blue')

# Cambiar nombre
# Cambia el nombre del jugador dependiendo el nombre
def cambiar_nombre():
    global turno
    global nombres
    global jugador1
    global jugador2
    global computadora
    global modo_computadora

    if modo_computadora:
        nombres[0][0].config(text = jugador1)

    elif turno:
        nombres[0][0].config(text = jugador1)
    else:
        nombres[0][0].config(text = jugador2)

# Pintar tablero
# Pinta el tablero de juego con colores intercalados
# Algorito para hacer pruebas
def pintar_tablero():

    global boton

    imgBoton = tk.PhotoImage(file="img/ball_red.png")
    imgBoton2 = tk.PhotoImage(file="img/ball_blue.png")

    var = True
    for i in range(6):
        for j in range(7):
            var = not (var)
            if var == True:
                boton[i][j].config(bg='red')
            else:
                boton[i][j].config(bg=color2)

# Verificar colores
# Actualiza los colores del tablero dependiendo si en el lugar de juego hay un 1 o un 2
def verificar_colores():
    global boton
    global matriz
    global lista_indice_filas
    global izq
    global der
    global fil_u
    global fil_d
    global contador_arriba

    filas = 6
    iteracion = 0

    # cambiar_color()
    # rojo = tk.PhotoImage(file='ball_red.png')
    # blue = tk.PhotoImage(file='ball_blue.png')

    for num in range(fil_u, fil_d):
        iteracion += 1
        # print(iteracion)
        for j in range(izq, der):
            # print(num,j)
            if matriz[num][j] == 1:
                boton[num - contador_arriba][j - izq].config(bg='red', borderwidth=1)  # bg='#FFFCF0',
            elif matriz[num][j] == 2:
                boton[num - contador_arriba][j - izq].config(bg='blue', borderwidth=1)
            elif matriz[num][j] == 0:
                boton[num - contador_arriba][j - izq].config(bg='white', borderwidth=1)

            # else:
            # boton[num][j-7].config(bg=color2, borderwidth = 1)

    # for i in range(6):
    # for j in range(7):
    # if matriz[i][j] == 1:
    # boton[i][j].config(bg='red', borderwidth = 1) # bg='#FFFCF0',
    # elif matriz[i][j] == 2:
    # boton[i][j].config(bg='blue', borderwidth = 1)
    # else:
    # boton[i][j].config(bg=color2, borderwidth = 1)

# Agregar jugadas
# E: numero
# Verifica que el boton jugado tenga el mismo string que el de la posicion de la matriz para agregar la jugada
def agregar_jugadas(bot):
    global matriz
    global izq
    global der
    global boton
    global fil_u
    global fil_d
    global contador_arriba

    # filas = 6

    for num in range(fil_u - contador_arriba, fil_d - contador_arriba):
        # print('agregar_jugadas')
        for j in range(izq, der):
            # print('El boton es: ', num,j-izq)
            if str(boton[num][j - izq]) == str(bot):
                agregar_numero(num, j)  # bg='#FFFCF0',
                # print('Lo agregó')
                break

# Agregar numero
# E: 2 numeros
# Recibe dos numeros y con ellos agrega la jugada a la matriz, luego actualiaz los colores de la interfaz
def agregar_numero(num, j):
    global matriz
    global turno
    global contador_arriba
    global numero_turnos
    global ganaJ1
    global ganaJ2
    global computadora
    global modo_computadora
    global combinaciones
    global gana_computadora
    print('Agregar: ', num, j)
    print('El len de matriz es:', len(matriz))
    print('El numero buscado es:', num + contador_arriba + 1)
    print('EL contador arriba es: ', contador_arriba)

    if modo_computadora == False:
        if ganaJ1 == False and ganaJ2 == False:
            try:
                if (matriz[(num + contador_arriba) + 1][j] == 1 or matriz[(num + contador_arriba) + 1][j] == 2) and matriz[(num + contador_arriba)][j] == 0:
                    if turno:
                        print('Matriz en la posicion: ', (num + contador_arriba) + 1, j)
                        matriz[num + contador_arriba][j] = 1
                        verificar_colores()
                        #print(matriz)
                        turno = not turno
                        cambiar_color()
                        cambiar_nombre()
                        numero_turnos += 1
                        if ganador(matriz, 1):
                            mensaje_emergente('Ganador', 'Jugador 1')
                            ganaJ1 = True
                            agregar_ganador(jugador1)
                            # respuesta = messagebox.askquestion(
                            #'Confirm', '¿Desea jugar una nueva partida?'
                            # )
                            # if respuesta == True:
                            # print('if')
                            # pass
                            # else:
                            # print('else')
                            # ventana.state(newstate="normal")

                    else:
                        print('Matriz en la posicion: ', (num + contador_arriba) + 1, j)
                        matriz[num + contador_arriba][j] = 2
                        verificar_colores()
                        #print(matriz)
                        turno = not turno
                        cambiar_color()
                        cambiar_nombre()
                        numero_turnos += 1
                        if ganador(matriz, 2):
                            mensaje_emergente('Ganador', 'Jugador 2')
                            ganaJ2 = True
                            agregar_ganador(jugador2)
                
            except:
                if (num + contador_arriba + 1) == len(matriz) and matriz[(num + contador_arriba)][j] == 0:
                    if verificarSieteDerecha(num,j) == True or verificarSieteIzquierda(num,j) == True:
                        if turno:
                            matriz[num + contador_arriba][j] = 1
                            verificar_colores()
                            #print(matriz)
                            turno = not turno
                            cambiar_color()
                            cambiar_nombre()
                            numero_turnos += 1
                            if ganador(matriz, 1):
                                mensaje_emergente('Ganador', 'Jugador 1')
                                ganaJ1 = True
                                agregar_ganador(jugador1)
                        else:
                            matriz[num + contador_arriba][j] = 2
                            verificar_colores()
                            #print(matriz)
                            turno = not turno
                            cambiar_color()
                            cambiar_nombre()
                            numero_turnos += 1
                            if ganador(matriz, 2):
                                mensaje_emergente('Ganador', 'Jugador 2')
                                ganaJ2 = True
                                agregar_ganador(jugador2)
                    else:
                        mensaje_emergente('Advertencia', 'Debe de jugar a máximo 7 fichas de distancia')
        else:
            mensaje_emergente('Atención!','Ya hay un ganador, por favor regrese al menu principal')



    elif modo_computadora == True:
        if ganaJ1 == False and gana_computadora == False:
            try:
                if (matriz[(num + contador_arriba) + 1][j] == 1 or matriz[(num + contador_arriba) + 1][j] == 2) and matriz[(num + contador_arriba)][j] == 0:
                    if turno:
                        print('Matriz en la posicion: ', (num + contador_arriba) + 1, j)
                        matriz[num + contador_arriba][j] = 1
                        verificar_colores()
                        #print(matriz)
                        turno = not turno
                        computadora = not computadora
                        cambiar_color()
                        cambiar_nombre()
                        numero_turnos += 1
                        
                        if ganador(matriz, 1):
                            mensaje_emergente('Ganador', 'Jugador 1')
                            ganaJ1 = True
                            agregar_ganador(jugador1)
                        else:
                            jugada_computadora()
                        if ganador(matriz, 2):
                            mensaje_emergente('Ganador', 'Computadora')
                            gana_computadora = True
                            agregar_ganador(jugador1)
                           
                
            except:
                if (num + contador_arriba + 1) == len(matriz) and matriz[(num + contador_arriba)][j] == 0:
                    if verificarSieteDerecha(num,j) == True or verificarSieteIzquierda(num,j) == True:
                        if turno:
                            matriz[num + contador_arriba][j] = 1
                            verificar_colores()
                            #print(matriz)
                            turno = not turno
                            computadora = not computadora
                            cambiar_color()
                            cambiar_nombre()
                            numero_turnos += 1
                            
                            if ganador(matriz, 1):
                                mensaje_emergente('Ganador', 'Jugador 1')
                                ganaJ1 = True
                                agregar_ganador(jugador1)
                            else:
                                jugada_computadora()
                            if ganador(matriz, 2):
                                mensaje_emergente('Ganador', 'Computadora')
                                gana_computadora = True
                                agregar_ganador(jugador1)
                    else:
                        mensaje_emergente('Advertencia', 'Debe de jugar a máximo 7 fichas de distancia')
        else:
            mensaje_emergente('Atención!','Ya hay un ganador, por favor regrese al menu principal')
    time.sleep(0.2)


# -------------------------------------------------------------------
# Tres seguidas horizontal
# Verifica que el jugador no tenga tres fivhas seguidas en horizontal,
# si las hay, la computadora bloqueara la jugada ganadora
def tres_seguidas_horizontal():
    global matriz
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if (matriz[i][j] == 1 and matriz[i][j-1] == 0) and i == len(matriz)-1:
                if matriz[i][j+1] == 1:
                    if matriz[i][j+2] == 1:
                        return [i,j-1]
            else:
                if matriz[i][j] == 1 and i == len(matriz)-1:
                    if matriz[i][j+1] == 1:
                        if matriz[i][j+2] == 1:
                            if matriz[i][j+3] == 0:
                                return [i,j+3]
    return 3
#print(tres_seguidas_horizontal())

# Dos seguidas horizontal
def dos_seguidos_horizontal():
    global matriz
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] == 1 and matriz[i][j-1] == 0:
                if matriz[i][j+1] == 1:
                    return [i,j-1]
            else:
                if matriz[i][j] == 1:
                    if matriz[i][j+1] == 1:
                        if matriz[i][j+2] == 0:
                            return [i,j+2]
    return 3

# Jugada aleatoria
# S: lista
# Analiza la matriz, detecta cuales lugares son aptos para jugar y retorna una lista
# con las posiciones disponibles
def jugada_aleatoria():
    global fil_u
    global fil_d
    global izq
    global der
    global matriz
    global computadora
    global modo_computadora
    global combinaciones
    global disponibles
    disponibles = []
    print('el rango es: ', range(fil_u, fil_d))
    iteraciones = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            iteraciones += 1
            try:
                if matriz[i][j] == 0 and (matriz[i+1][j] == 1 or matriz[i+1][j] == 2):
                    print(i,j) 
                    if [i,j] not in combinaciones:                 
                        disponibles.append([i,j])
                        #combinaciones.append([i,j])                             
            except:
                continue
            try:
                if matriz[i][j] == 0 and i == len(matriz):
                    if [i,j] not in combinaciones:                 
                        disponibles.append([i,j])
                        #combinaciones.append([i,j])
            except:
                continue
    print(iteraciones)
    return disponibles

# Detectar jugada
# S: lista
# Detecta la primera jugada del juego y retorn una lista con las jugadas a la par de ella
def detectar_jugada():
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] == 1:
                return [i,j]

# Jugada computadora
# Realiza la jugada de la computadora
def jugada_computadora():
    global matriz
    global turno
    global contador_arriba
    global numero_turnos
    global ganaJ1
    global ganaJ2
    global computadora
    global modo_computadora
    global fil_u
    global fil_d
    global izq
    global der
    global combinaciones
    global disponibles
    print('\nJugada computadora')
    print('Turno es: ', turno, '   computadora es: ', computadora)
    pasos = 0

    if turno == False and computadora == True:
        # if numero_turnos == 1:
        #     x = random.randint(0,1)
        #     if x == 0:
        #         play = detectar_jugada()
        #         matriz[5][play[1]+1] = 2
        #         print(matriz)
        #         computadora = not computadora
        #         turno = not turno
        #         verificar_colores()
        #         cambiar_color()
        #         if ganador(matriz, 2):
        #             mensaje_emergente('Ganador', 'Te ha ganado la computadora')
        #             ganaJ2 = True

        #     if x == 1:
        #         play = detectar_jugada()
        #         matriz[5][play[1]-1] = 2
        #         print(matriz)
        #         computadora = not computadora
        #         turno = not turno
        #         verificar_colores()
        #         cambiar_color()
        #         if ganador(matriz, 2):
        #             mensaje_emergente('Ganador', 'Te ha ganado la computadora')
        #             ganaJ2 = True
        # elif type(dos_seguidos_horizontal()) == list and numero_turnos > 1:
        #     x = dos_seguidos_horizontal()
        #     print(x)
        #     matriz[x[0]][x[1]] = 2
        #     print(matriz)
        #     computadora = not computadora
        #     turno = not turno
        #     verificar_colores()
        #     cambiar_color()
        #     if ganador(matriz, 2):
        #         mensaje_emergente('Ganador', 'Te ha ganado la computadora')
        #         ganaJ2 = True
        if type(tres_seguidas_horizontal()) == list and numero_turnos > 1:
            print('llego aqui')
            x = tres_seguidas_horizontal()
            print(x)
            matriz[x[0]][x[1]] = 2
            print (matriz)
            computadora = not computadora
            turno = not turno
            verificar_colores()
            cambiar_color()
            if ganador(matriz, 2):
                mensaje_emergente('Ganador', 'Te ha ganado la computadora')
                ganaJ2 = True

        else:
            x = jugada_aleatoria()
            print('\n aleatorio es: ', x)
            largo = len(x)
            r = random.randint(0,largo-1)
            print(r)
            x = x[r]
            matriz[x[0]][x[1]] = 2
            combinaciones.append([x[0],x[1]])
            #print(matriz)
            computadora = not computadora
            turno = not turno
            verificar_colores()
            cambiar_color()
            if ganador(matriz, 2):
                mensaje_emergente('Ganador', 'Te ha ganado la computadora')
                ganaJ2 = True

# c0
# Algoritmo dummy para pruebas
def c0():
    global turno
    if turno:
        boton[5][4].config(bg='yellow')
    else:
        boton[5][4].config(bg='blue')
    turno = not turno

# Mover derecha
# Mueve la interfaz del tablero de juego hacia la derecha
def mover_derecha():
    global der
    global izq

    global list_column_i
    global list_column_d
    if izq - 1 > -1:
        der -= 1
        izq -= 1
        list_column_i -= 1
        list_column_d -= 1
        verificar_colores()
        actualizar_indices_columnas()
    # print (der)

# Mover izquierda
# Mueve la interfaz del tablero de juego hacia la izquierda
def mover_izquierda():
    global der
    global izq
    global matriz

    global list_column_i
    global list_column_d
    if der + 1 < len(matriz[0]) + 1:
        der += 1
        izq += 1
        list_column_i += 1
        list_column_d += 1
        verificar_colores()
        actualizar_indices_columnas()
    # print (der)

# Mover arriba
# Mueve la interfaz del tablero de juego hacia arriba
def mover_arriba():
    global der
    global izq
    global matriz
    global contador_arriba
    global fil_u
    global fil_d

    global list_row_u
    global list_row_d

    if contador_arriba > 0:
        fil_u -= 1
        fil_d -= 1
        contador_arriba -= 1
        list_row_u += 1
        list_row_d += 1
        verificar_colores()
        actualizar_indices_filas()

# Mover abajo
# Mueve la interfaz del tablero de juego hacia abajo
def mover_abajo():
    global der
    global izq
    global matriz
    global contador_arriba
    global fil_u
    global fil_d

    global list_row_u
    global list_row_d
    print('se movio')
    print('contador es:', contador_arriba)
    print('fila_u se:', fil_u)
    print('fila_d es', fil_d)
    if contador_arriba > -1:
        if fil_d < len(matriz):
            fil_u += 1
            fil_d += 1
            contador_arriba += 1
            list_row_u -= 1
            list_row_d -= 1
            print('se movio')
            print('se movio')
            print('contador es:', contador_arriba)
            print('fila_u se:', fil_u)
            print('fila_d es', fil_d)
            verificar_colores()
            actualizar_indices_filas()

# Agregar izquierda
# Agrega espacios adicionales a la izquierda de la matriz para seguir jugando
def agregar_izq():
    global matriz
    global izq
    global der
    for i in matriz:
        i[:0] = [0]
    izq += 1
    der += 1
    # print(matriz)
    print(izq)
    print(der)

# Agregar derecha
# Agrega espacios adicionales a la derecha de la matriz para seguir jugando
def agregar_der():
    global matriz
    for i in matriz:
        i.append(0)
    print(matriz)

# Agregar arriba
# Agrega espacios adicionales arriba de la matriz para seguir jugando
def agregar_up():
    global matriz
    global fil_u
    global fil_d
    global contador_arriba
    num = len(matriz[0])
    valor = 0
    lista = []
    while valor < num:
        lista.append(0)
        valor += 1
    matriz[:0] = [lista]
    fil_u += 1
    fil_d += 1
    contador_arriba += 1
    print(matriz)

# Matriz en blanco
# Coloca en todas las posiciones de la matriz un 0
def matriz_en_blanco():
    global matriz
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            matriz[i][j] = 0
    verificar_colores()


# Fucion para showmessage
#_________________________________________________________
# Ventana de mensaje
def mensaje_emergente(texto1, texto2):
    messagebox.showinfo(texto1, texto2)

# Ventana de error
def error(texto1, texto2):
    messagebox.showerror(texto1, texto2)


# ----------------------
# Regresar
# Funcion que cierra la ventana actual y devuelve al menu principal
def regresar(x_ventana):
    ventana.state(newstate="normal")
    x_ventana.destroy()


# Valores por defecto
# Coloca en las variables globales los valores por defecto
def valores_por_defecto():
    global matriz
    global vn
    global boton
    global turno
    global indices_columnas
    global guardar_partida

    global izq
    global der
    global fil_u
    global fil_d
    global contador_arriba
    global list_column_i
    global list_column_d
    global list_row_d
    global list_row_u
    global numero_turnos

    global ganaJ1
    global ganaJ2
    global default
    global id_partida

    global computadora
    global modo_computadora
    global combinaciones
    global disponibles
    global gana_computadora

    computadora = False
    modo_computadora = False
    combinaciones = []
    disponibles = []
    id_partida = getNextId(guardar_partida)

    turno = True

    izq = 7  # Posición en la matriz izq
    der = 14  # Posición en la matriz der
    fil_u = 0  # Posición de la fila arriba
    fil_d = 6  # Posición de la fila abajo
    contador_arriba = 0  # Contador de espacios que hay arriba de la vista de cuadrícula


    list_column_i = 7
    list_column_d = 14
    list_row_u = 0
    list_row_d = 6

    list_column_i = 7
    list_column_d = 14
    list_row_u = 0
    list_row_d = 6
    numero_turnos = 0

    ganaJ1 = False
    ganaJ2 = False

    default = True
    gana_computadora = False
    matriz_en_blanco()

    matriz = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

# Ventana opciones
# Ventana que da las opciones demodo de juego para elegir
def ventana_opciones():
    global turno
    global vo

    vo = tk.Toplevel()
    ventana.withdraw()
    vo.title('Selección de modo de juego')
    vo.geometry('680x350+700+350')
    vo.resizable(0, 0)
    vo.iconbitmap("img/control1.ico")
    Label = tk.Label(vo, text='Seleccione el modo de juego', font=('Tricks Hollow', 30), fg='red3')
    Label.place(x=100, y=60)

    pvp = tk.Button(vo, text = '1. Jugador vs Jugador', font=('Players', 15), borderwidth=3, command = abrirVentanaNombres)
    pvp.place(x=240, y=125)

    pvc = tk.Button(vo, text = '2. Jugador vs Computadora', font=('Players', 15), borderwidth=3, command = ventana_computadora)
    pvc.place(x=210, y=175)

    load = tk.Button(vo, text = '3. Cargar partida', font=('Players', 15), borderwidth=3, command=abrir_ventana_cargar)
    load.place(x=260,y=225)

    regresar1 = tk.Button(vo, text = 'Regresar', command = lambda:regresar(vo))
    regresar1.place(x=10,y=10)

    vo.mainloop()

# Abrir ventana cargar
# Ventana que muestra las partidas guardadas y al seleccionar una la carga para jugarla
def abrir_ventana_cargar():
    global guardar_partida
    global id_partida

    def validar_numero():
        global id_partida
        n1 = eleccion.get()
        id_partida = int(n1)
        ventana_cargar.destroy()
        cargar_partida_empezada(int(n1)-1)

    ventana_cargar = tk.Toplevel()
    vo.withdraw()
    ventana_cargar.title('Cargar Partidas')
    ventana_cargar.geometry('570x700+700+200')
    ventana_cargar.resizable(0, 0)
    ventana_cargar.iconbitmap("img/control1.ico")
    Label = tk.Label(ventana_cargar, text='Partidas Guardadas', font=('Players', 19))
    Label.place(x=175, y=30)
    b1 = tk.Button(ventana_cargar, text = 'Regresar', command = lambda:regresar(ventana_cargar))
    b1.place(x=10,y=10)

    y = 75
    id = 0
    for i in guardar_partida:
        l1 = tk.Label(ventana_cargar, text = str(i[0]) + '.\t' + i[1] + '\tJ1: ' + i[4] + '\tJ2: ' + i[5], bg = 'lightgrey', borderwidth=2, relief="ridge", font=('Verdana', 9)).place(x=65,y=y)
        id += 1
        y+=30

    y += 50
    tk.Label(ventana_cargar, text='Digite el número de la partida: ', font=('Verdana', 9)).place(x=185,y=y-25)
    eleccion = tk.Entry(ventana_cargar, bd=2, width=5)
    eleccion.place(x=255,y=y)
    tk.Button(ventana_cargar, text='Cargar', command = validar_numero, font=('Verdana', 9)).place(x=245, y=y+25)

        #print('Le numero es: ', numero)
        #guardadas.append([])
        #l1 = tk.Button(ventana_cargar, text = i[0] + '\tJ1: ' + i[3] + '\tJ2: ' + i[4])
        #l1.place(x= 75, y = y)


        #y += 30
        #numero += 1
        
    #guardadas[0].config(command=lambda:cargar_partida_empezada(0))
    #guardadas[1].config(command=lambda:cargar_partida_empezada(1))
    #guardadas[2].config(command=lambda:cargar_partida_empezada(2))
    #guardadas[3].config(command=lambda:cargar_partida_empezada(3))
        
    ventana_cargar.mainloop()


# Ventana nombres
# Ventana en la que se solicitan los nombres de los jugadores
def abrirVentanaNombres():
    global turno
    global vn
    

    def obtener_nombres():
        global default
        global jugador1
        global jugador2
        global jugadores
        global modo_computadora
        j1 = nombreJ1.get()
        j2 = nombreJ2.get()

        if j1.strip() == '':
            error('Error', 'El nombre del jugador 1 no puede estar vacío.')
        elif isNumber(j1):
            error('Error', 'El nombre del jugador 1 no puede ser solo números.')

        elif j2.strip() == '':
            error('Error', 'El nombre del jugador 2 no puede estar vacío.')
        elif isNumber(j2):
            error('Error', 'El nombre del jugador 2 no puede ser solo números.')

        else:
            jugador1 = j1.title()
            if estaJugador(jugador1) == False:
                consecutivo = getNextId(jugadores)
                jugadores.append([consecutivo, jugador1])
                guardar("jugadores.txt", jugadores)
            else:
                mensaje_emergente('Atención', 'El jugador 1 ya se encuentra registrado')

            jugador2 = j2.title()
            if estaJugador(jugador2) == False:
                consecutivo2 = getNextId(jugadores)
                jugadores.append([consecutivo2, jugador2])
                guardar("jugadores.txt", jugadores)
            else:
                mensaje_emergente('Atención', 'El jugador 2 ya se encuentra registrado')

            default = True
            modo_computadora = False
            print(jugador1)
            print(jugador2)
            vn.withdraw()
            
            abrirVentana2()

    vn = tk.Toplevel()
    vo.withdraw()
    vn.title('Nombre Jugadores')
    vn.geometry('525x200+700+350')
    vn.resizable(0, 0)
    vn.iconbitmap("img/control1.ico")
    Label = tk.Label(vn, text='Ingrese el nombre de los jugadores', font=('Players', 19))
    Label.place(x=60, y=30)

    # Variables de datos
    varEntry1 = tk.StringVar()
    varEntry2 = tk.StringVar()

    jug1 = tk.Label(vn, text='Jugador 1:', font=('Verdana', 10))
    jug1.place(x=100, y=70)

    nombreJ1 = tk.Entry(vn, bd=2, width=40)
    nombreJ1.place(x=185, y=70)

    jug2 = tk.Label(vn, text='Jugador 2:', font=('Verdana', 10))
    jug2.place(x=100, y=105)

    nombreJ2 = tk.Entry(vn, bd=2, width=40)
    nombreJ2.place(x=185, y=105)

    tk.Button(vn, text='Siguiente', command=obtener_nombres, font=('Verdana', 10)).place(x=280, y=140)
    tk.Button(vn, text='Regresar', command=lambda:regresar(vn), font=('Verdana', 10)).place(x=195, y=140)

    vn.mainloop()

# Ventana computadora
# Ventana para jugar en modo computadora, y asigna a las avriables globales el modo computadora
def ventana_computadora():
    global computadora

    def obtener_nombre():
        global default
        global jugador1
        global jugador2
        global jugadores
        global computadora
        global modo_computadora
        global turno
        global combinaciones
        global disponibles
        global id_partida
        global matriz
        global numero_turnos
        global ganaJ1
        global ganaJ2
        global izq
        global der
        global fil_u
        global fil_d
        global contador_arriba
        global list_column_i
        global list_column_d
        global list_row_u
        global list_row_d
        global gana_computadora
        j1 = nombreJ1.get()

        if j1.strip() == '':
            error('Error', 'El nombre del jugador 1 no puede estar vacío.')
        elif isNumber(j1):
            error('Error', 'El nombre del jugador 1 no puede ser solo números.')

        else:
            jugador1 = j1.title()
            if estaJugador(jugador1) == False:
                consecutivo = getNextId(jugadores)
                jugadores.append([consecutivo, jugador1])
                guardar("jugadores.txt", jugadores)
            else:
                mensaje_emergente('Atención', 'El jugador 1 ya se encuentra registrado')

            default = False
            modo_computadora = True
            computadora = False
            turno = True
            jugador2 = 'Computadora'
            combinaciones = []
            disponibles = []
            id_partida = getNextId(guardar_partida)


            numero_turnos = 0

            ganaJ1 = False
            ganaJ2 = False
            #usados = 0
            #fin = False

            # Variables globales
            izq = 7  # Posición en la matriz izq
            der = 14  # Posición en la matriz der
            fil_u = 0  # Posición de la fila arriba
            fil_d = 6  # Posición de la fila abajo
            contador_arriba = 0  # Contador de espacios que hay arriba de la vista de cuadrícula


            list_column_i = 7
            list_column_d = 14
            list_row_u = 0
            list_row_d = 6


            matriz = [
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    ]



            gana_computadora = False

            print('El id de la partida es: ', id_partida)
            print(jugador1)
            print(jugador2)
            ventana_c.withdraw()
            
            abrirVentana2()

    ventana_c = tk.Toplevel()
    vo.withdraw()
    ventana_c.title('Jugador vs Computadora')
    ventana_c.geometry('525x200+700+350')
    ventana_c.resizable(0,0)
    ventana_c.iconbitmap("img/control1.ico")

    Label = tk.Label(ventana_c, text='Ingrese el nombre del jugador', font=('Players', 19))
    Label.place(x=85, y=30)

    jug1 = tk.Label(ventana_c, text='Jugador 1:', font=('Verdana', 10))
    jug1.place(x=95, y=80)

    nombreJ1 = tk.Entry(ventana_c, bd=2, width=40)
    nombreJ1.place(x=180, y=80)

    tk.Button(ventana_c, text='Siguiente', command=obtener_nombre, font=('Verdana', 10)).place(x=270, y=115)
    tk.Button(ventana_c, text='Regresar', command=lambda:regresar(ventana_c), font=('Verdana', 10)).place(x=185, y=115)


    ventana_c.mainloop()

# Ventana puntuaciones
# Ventana que muestra la tabla de puntuaciones del juego,  de la mejor puntuación a la peor
def ventana_puntuaciones():
    global ganadores

    puntuaciones = tk.Toplevel()
    ventana.withdraw()
    puntuaciones.title('Tabla de puntuaciones')
    puntuaciones.geometry('614x700+700+150')
    puntuaciones.resizable(0, 0)
    puntuaciones.iconbitmap("img/control1.ico")
    puntuaciones.grid
    b1 = tk.Button(puntuaciones, text='Regresar', font=('Verdana', 10), command = lambda:regresar(puntuaciones))
    b1.grid(column = 0, row = 0, padx = 1, pady = 20)
    Label = tk.Label(puntuaciones, text='> Mejores jugadores :', font=('Players', 18)).grid(row=1,column=0)
    label2 = tk.Label(puntuaciones, text = 'Nombre', bg = 'grey', fg = 'white', width=25, font=('Verdana', 11)).grid(row=2, column=0)
    label3 = tk.Label(puntuaciones, text = 'Puntos', bg = 'green', fg = 'white', width=25, font=('Verdana', 11)).grid(row=2, column=1)
    datos = []

    if ganadores != []:
        puntos = []

        for i in ganadores:
            puntos.append(i[1])
        print(puntos)

        puntos = set(puntos)
        puntos = list(puntos)

        puntos.sort(reverse=True)
        print(puntos)
        orden = []

        for i in puntos:
            for jugador in ganadores:
                if i == jugador[1]:
                    orden.append(jugador)
                    
        #return orden
        row = 2
        column = 1
        for dato in orden:
            print (dato)
            row+=1
            lab = tk.Label(puntuaciones, text=dato[0], justify='left', font=('dogica',9), borderwidth=2, relief="ridge", width=25, height=2).grid(column=0, row=row)
            lab2 = tk.Label(puntuaciones, text=dato[1], font=('dogica',9), borderwidth=2, relief="ridge", width=25, height=2).grid(column=1, row=row)
            datos.append(lab)




    puntuaciones.mainloop()


# Abrir ventana2
# Ventana que crea la interfaz de juego 
def abrirVentana2():
    global matriz
    global vn
    global boton
    global turno
    global indices_columnas

    global izq
    global der
    global fil_u
    global fil_d
    global contador_arriba
    global list_column_i
    global list_column_d
    global list_row_d
    global list_row_u
    global numero_turnos

    global ganaJ1
    global ganaJ2
    global default
    
    #vn.destroy()

    #turno = True

    #izq = 7  # Posición en la matriz izq
    #der = 14  # Posición en la matriz der
    #fil_u = 0  # Posición de la fila arriba
    #fil_d = 6  # Posición de la fila abajo
    #contador_arriba = 0  # Contador de espacios que hay arriba de la vista de cuadrícula


    #list_column_i = 7
    #list_column_d = 14
    #list_row_u = 0
    #list_row_d = 6

    #list_column_i = 7
    #list_column_d = 14
    #list_row_u = 0
    #list_row_d = 6
    #numero_turnos = 0

    #ganaJ1 = False
    #ganaJ2 = False

    ventana.withdraw()
    app = tk.Toplevel()
    app.title('4 en Linea')
    app.geometry("625x650+700+200")
    app.resizable(0, 0)
    app.iconbitmap("img/control1.ico")
    # vp.grid()

    vp = tk.Frame(app)
    vp.grid(column=0, row=0, padx=(50, 50), pady=(20, 20))
    vp.columnconfigure(0, weight=1)
    vp.rowconfigure(0, weight=1)
    vp.config(bg=color)

    imgBack = tk.PhotoImage(file="img/back_button.png")
    boton_regresar = tk.Button(app, image=imgBack, borderwidth=0, command=lambda: regresar(app))
    boton_regresar.place(x=510, y=10)

    imgUp = tk.PhotoImage(file="img/u_arrow.png")
    boton_arriba = tk.Button(vp)
    boton_arriba.config(bg=color, image=imgUp, borderwidth=0, command=mover_arriba)
    boton_arriba.grid(column=6, row=1)

    imgBottom = tk.PhotoImage(file="img/b_button.png")
    boton_abajo = tk.Button(vp)
    boton_abajo.config(bg=color, image=imgBottom, borderwidth=0, command=mover_abajo)
    boton_abajo.grid(column=6, row=11)

    boton_add_up = tk.Button(vp, bg=color, text="+", borderwidth=1, command=agregar_up).grid(column=6, row=0)

    label_espacio_1 = tk.Label(vp, bg=color).grid(pady=0, column=6, row=2)

    imgLeft = tk.PhotoImage(file="img/l_arrow3.png")
    boton_izquierda = tk.Button(vp, bg=color, text="<", image=imgLeft, borderwidth=0, command=mover_derecha).grid(column=0, row=5)

    boton_add_izq = tk.Button(vp, bg=color, text="+", borderwidth=1, command=agregar_izq).grid(column=0, row=6)

    label_espacio_2 = tk.Label(vp, bg=color, width=1).grid(padx=10, column=1, row=5)

    imgRight = tk.PhotoImage(file="img/r_arrow3.png")
    boton_derecha = tk.Button(vp, bg=color, text=">", image=imgRight, borderwidth=0, command=mover_izquierda).grid(column=12, row=5)

    boton_add_der = tk.Button(vp, bg=color, text="+", borderwidth=1, command=agregar_der).grid(column=12, row=6)

    label_espacio_3 = tk.Label(vp, bg=color, width=1).grid(padx=10, column=11, row=5)

    imgPlay = tk.PhotoImage(file="img/play_button1.png")
    label_espacio_4 = tk.Label(vp, bg=color, width=1).grid(pady=0, column=6, row=10)
    boton_jugar = tk.Button(vp,bg=color, text="Guardar Partida", borderwidth=2, command=guardar_partida_empezada, font=('Verdana', 11)).grid(column=5, row=14, columnspan=3)
    label_espacio_6 = tk.Label(vp, bg=color, width=1).grid(pady=10, column=6, row=13)

    label_espacio_5 = tk.Label(vp, bg=color, fg='black', text='Color del jugador:', font=('Players', 13)).grid(column=3, row=13, columnspan=4)

    if turno:
        turno_jugador = 'Rojo'
        color_jugador1 = 'red'
    else:
        turno_jugador = 'Azul'
        color_jugador1 = 'blue'
    # label_espacio_6 = tk.Label(vp, bg=color, fg=color_jugador1, text=turno_jugador).grid(column=6, row=13, columnspan=1)

    # barras de menu
    menubar = tk.Menu(app)
    # crear los menus
    mnuArchivo = tk.Menu(menubar)
    mnuEdicion = tk.Menu(menubar)
    # crear
    mnuArchivo.add_command(label="Abrir")
    mnuArchivo.add_command(label="Nuevo")
    mnuArchivo.add_command(label="Guardar")
    mnuArchivo.add_command(label="Cerrar")
    mnuArchivo.add_separator()
    mnuArchivo.add_command(label="Salir")
    # ----------------------------------
    mnuEdicion.add_command(label="Copiar")
    mnuEdicion.add_command(label="Pegar")
    mnuEdicion.add_command(label="Deshacer")
    mnuEdicion.add_command(label="Rehacer")
    # agregar los menus a la barra de menu
    menubar.add_cascade(label="Archivo", menu=mnuArchivo)
    menubar.add_cascade(label="Edición", menu=mnuEdicion)
    # indicamos que la barra de menu está en la ventana
    app.config(menu=menubar)

    # Label global para poder cambiarla con eventos
    #texto = ''
    #texto = "Estado del juego: No Iniciado."
    
    tk.Label(vp, text='Turno del jugador: ', bg=color, font=('Players', 13)).grid(column=2, row=12, columnspan=5)
    # label_nombre = tk.Label(vp, text='Moises ', bg=color)
    # label_nombre.grid(column=4, row=12, columnspan=5)

    # For para crear la cuadrícula de juego
    for r in range(3, 9):
        for c in range(3, 10):
            # print(boton[r-3][c-3])
            text = str(r - 3) + ',' + str(c - 3)
            # cell = Button(vp, width = 4, height=2, text=text)
            cell = tk.Button(
                vp, bg=color2, width=6, height=3, text='', borderwidth=1
            )  # bg = '#FFFCF0',
            cell.grid(padx=0, pady=0, row=r, column=c)
            # cell.insert(0, '({},{})'.format(r,c))

            boton[r - 3][c - 3] = cell
            # --------------------------------------------------------------
    if default == True:
        valores_por_defecto()

    for i in range(13, 14):
        for j in range(15, 16):
            but = tk.Button(vp, bg='yellow', width=6, height=0, borderwidth=0, command = verificar_colores)
            but.grid(padx=0, pady=0, row=i, column=7)

            colores[i - 13][j - 15] = but


    for i in range(12,13):
        for j in range(6,7):
            label_name = tk.Label(vp , text = jugador1, font=('Verdana', 11))
            label_name.grid(row=i, column = 7, columnspan = 3)

            nombres[i-12][j-6] = label_name


    for i in range(2, 3):
        for j in range(3, 10):
            la1 = tk.Label(vp, bg=color, text='1')
            la1.grid(padx=0, pady=3, row=i, column=j, columnspan=1)

            indices_columnas[i - 2][j - 3] = la1

    for i in range(3, 9):
        for j in range(2, 3):
            la2 = tk.Label(vp, bg=color, text='1')
            la2.grid(padx=10, pady=0, row=i, column=j, columnspan=1)

            indice_filas[i - 3][j - 2] = la2

    imgBoton = tk.PhotoImage(file="img/ball_red.png")
    imgBoton2 = tk.PhotoImage(file="img/ball_blue.png")
    # boton[0][0].config(bg="yellow", text = "p", command = pintar_tablero)
    # boton[5][2].config(bg="brown", text = 'c', command = verificar_colores)
    # boton[0][4].config(bg='purple', text = '0', command = c0)
    # boton[1][5].config(bg='lightblue', image = imgBoton2, width=32, height=34.5)

    # def funciones_botones():
    # global boton
    # for i in range(len(boton)):
    # for j in range(len(boton[0])):
    # boton[i][j].config(command = lambda:agregar_jugadas(boton[i][j]))
    # print ('si')
    # print(boton)
    # funciones_botones()

    boton[0][0].config(command=lambda: agregar_jugadas(boton[0][0]))
    boton[0][1].config(command=lambda: agregar_jugadas(boton[0][1]))
    boton[0][2].config(command=lambda: agregar_jugadas(boton[0][2]))
    boton[0][3].config(command=lambda: agregar_jugadas(boton[0][3]))
    boton[0][4].config(command=lambda: agregar_jugadas(boton[0][4]))
    boton[0][5].config(command=lambda: agregar_jugadas(boton[0][5]))
    boton[0][6].config(command=lambda: agregar_jugadas(boton[0][6]))
    boton[1][0].config(command=lambda: agregar_jugadas(boton[1][0]))
    boton[1][1].config(command=lambda: agregar_jugadas(boton[1][1]))
    boton[1][2].config(command=lambda: agregar_jugadas(boton[1][2]))
    boton[1][3].config(command=lambda: agregar_jugadas(boton[1][3]))
    boton[1][4].config(command=lambda: agregar_jugadas(boton[1][4]))
    boton[1][5].config(command=lambda: agregar_jugadas(boton[1][5]))
    boton[1][6].config(command=lambda: agregar_jugadas(boton[1][6]))
    boton[2][0].config(command=lambda: agregar_jugadas(boton[2][0]))
    boton[2][1].config(command=lambda: agregar_jugadas(boton[2][1]))
    boton[2][2].config(command=lambda: agregar_jugadas(boton[2][2]))
    boton[2][3].config(command=lambda: agregar_jugadas(boton[2][3]))
    boton[2][4].config(command=lambda: agregar_jugadas(boton[2][4]))
    boton[2][5].config(command=lambda: agregar_jugadas(boton[2][5]))
    boton[2][6].config(command=lambda: agregar_jugadas(boton[2][6]))
    boton[3][0].config(command=lambda: agregar_jugadas(boton[3][0]))
    boton[3][1].config(command=lambda: agregar_jugadas(boton[3][1]))
    boton[3][2].config(command=lambda: agregar_jugadas(boton[3][2]))
    boton[3][3].config(command=lambda: agregar_jugadas(boton[3][3]))
    boton[3][4].config(command=lambda: agregar_jugadas(boton[3][4]))
    boton[3][5].config(command=lambda: agregar_jugadas(boton[3][5]))
    boton[3][6].config(command=lambda: agregar_jugadas(boton[3][6]))
    boton[4][0].config(command=lambda: agregar_jugadas(boton[4][0]))
    boton[4][1].config(command=lambda: agregar_jugadas(boton[4][1]))
    boton[4][2].config(command=lambda: agregar_jugadas(boton[4][2]))
    boton[4][3].config(command=lambda: agregar_jugadas(boton[4][3]))
    boton[4][4].config(command=lambda: agregar_jugadas(boton[4][4]))
    boton[4][5].config(command=lambda: agregar_jugadas(boton[4][5]))
    boton[4][6].config(command=lambda: agregar_jugadas(boton[4][6]))
    boton[5][0].config(command=lambda: agregar_jugadas(boton[5][0]))
    boton[5][1].config(command=lambda: agregar_jugadas(boton[5][1]))
    boton[5][2].config(command=lambda: agregar_jugadas(boton[5][2]))
    boton[5][3].config(command=lambda: agregar_jugadas(boton[5][3]))
    boton[5][4].config(command=lambda: agregar_jugadas(boton[5][4]))
    boton[5][5].config(command=lambda: agregar_jugadas(boton[5][5]))
    boton[5][6].config(command=lambda: agregar_jugadas(boton[5][6]))

    actualizar_indices_columnas()
    actualizar_indices_filas()

    verificar_colores()
    #matriz_en_blanco()
    cambiar_color()
    cambiar_nombre()
    
    
    #cargar_partida_empezada(0)
    print('Turno: ', turno)
    print ('numero de turnos: ', numero_turnos)
    print('jugador1: ', jugador1)
    print('jugador2: ', jugador2)
    print('ganaj1: ', ganaJ1)
    print('ganaJ2: ', ganaJ2)
    print('color jugador: ', color_jugador)
    print('izq: ', izq)
    print('der: ', der)
    print('fil u: ', fil_u)
    print('default: ', default)

    #print('matriz\n', matriz)
    app.mainloop()


# --------------------------------------------

ventana = tk.Tk()
ventana.title("Menu Principal")
ventana.geometry("550x300+725+300")
ventana.config(bg="black")
ventana.resizable(0, 0)
# ventana.iconbitmap("icono.ico")
ventana.iconbitmap("img/control1.ico")

cargarArchivos()

imgPortada = tk.PhotoImage(file="img/letrero_2.png")
# label1 = tk.Label(ventana, text="4 en línea", font=("Verdana",24))
label1 = tk.Label(ventana, image=imgPortada, bg="black")
label1.pack(fill=tk.BOTH, side=tk.TOP, pady=65)

label2 = tk.Label(
    ventana, text="Version 2.1", bg="black", font=("dogica", 7), fg="white"
)
label2.place(x=3, y=277)

boton1 = tk.Button(
    ventana, text="Jugar", width=13, height=2, font=('Players', 14), command=ventana_opciones
)
boton1.place(x=113, y=150)

boton2 = tk.Button(ventana, text="Puntajes", width=13, height=2, font=('Players', 14), command = ventana_puntuaciones)
boton2.place(x=275, y=150)

ventana.mainloop()
