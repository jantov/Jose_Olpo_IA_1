#2. Modificar el juego 3 en raya, para que se aplique la misma lógica, pero en un tablero de 4x4
# (gana el primero que logra enlazar 3 marcas similares, horizontales, verticales o diagonales).

# coding: utf-8

# Importar librerias

import numpy as np
import random
import platform
import time
from os import system
import math

TAMANO = 4

# FUNCIONES DE TABLERO
def tablero_crear(tamano):
    tablero = list()
    for i in range(1, tamano * tamano+1):
        tablero.append(str(i))

    return tablero

def devolverNum(tablero, num):

    x = tablero[num]
    if len(x) < 2:
        return (f' {x}')
    else:
        return x

def mostrar_tablero(tablero):
    for i in range(0, len(tablero), int(math.sqrt(len(tablero)))):
        print(f"| {devolverNum(tablero,i)}   {devolverNum(tablero,i+1)}   "
              f"{devolverNum(tablero,i+2)}   {devolverNum(tablero,i+3)} |")

def marcar(tablero, posicion, turno):
    tablero[posicion-1] = turno




#FUNCIONES DE GANAR PERDER O EMPATAR
def empate(tablero):
    tablero_2 = tablero_crear(TAMANO)
    for i in range(len(tablero)):
        if tablero[i] == tablero_2[i]:
            return False
    return True

def fin(tablero, turno):
    p = tablero[:]
    #Posiciones horizonatles
    # range (0,16,4) 
    for i in range(0, len(p), int(math.sqrt(len(p)))):
        for j in range(0,int(math.sqrt(len(p) ) )-2):
            if p[i+j] == turno and p[i+j+1] == turno and p[i+j+2] == turno:
                return True
    # Posiciones Verticales
    # range (0,4) 0 1 2 3
    for i in range(0, int(math.sqrt(len(p)))):
        for j in range(0, int(math.sqrt(len(p))) + 1, 4):
            if p[i + j] == turno and p[i + j + 4] == turno and p[i + j + 8] == turno:
                return True
    # Posiciones Diagonal positiva izq  a derch de arriba abajo
    # range (0,2) 0 1
    for i in range(0, int(math.sqrt(len(p)))//2):
        # range (0,5,4) 0 4
        for j in range(0, int(math.sqrt(len(p))) + 1, 4):
            if p[i + j] == turno and p[i + j + 5] == turno and p[i + j + 10] == turno:
                return True
    # Posiciones Diagonal NEGATIVA DERCH  A IZQ de arriba abajo
    # range (2,4) 2 3
    for i in range(int(math.sqrt(len(p)))//2, int(math.sqrt(len(p)))):
        # range (0,5,4) 0 4
        for j in range(0, int(math.sqrt(len(p))) + 1, 4):
            if p[i + j] == turno and p[i + j + 3] == turno and p[i + j + 6] == turno:
                return True


#FUNCIONES PARA EL JUGADOR
def espacio_libre (tablero, posicion):
    x = tablero[posicion - 1]
    if x != 'X' and x!= 'O':
        return True
    return False
def valor_no_aceptado(posicion):
    if(posicion > 16 or posicion < 1):
        return False
    return True

def turno_Jugador (tablero):
    while True:
        try:
            mov = int(input("Escoja una posicion: "))


            if espacio_libre(tablero, mov) and valor_no_aceptado(mov):
                return mov
            else:
                print("Error 001: Jugado No Valida, Intente otra vez")
        except (KeyError, ValueError):
            print('Error 003: valor introducido no valido')


#FUNCIONES PARA IA
def movimientos_validos(tablero):
    pos_validas = []
    tablero_inicial = tablero_crear(TAMANO)
    for i in range(len(tablero)):
        if tablero_inicial[i] == tablero[i]:
            pos_validas.append(i+1)
    return pos_validas

def mov_final(tablero):
    return fin(tablero,icono_H) or fin(tablero, icono_IA) or empate(tablero)

def puntuacion(tablero, icon):
    punt = 0
    cuadrante_medio = [tablero[5], tablero[6], tablero[9], tablero[10]]
    cont_centro = cuadrante_medio.count(icon)
    punt += cont_centro * 3

    #Posiciones Horizontales
    for i in range(0, len(tablero), int(math.sqrt(len(tablero)))):
        for j in range(0,int(math.sqrt(len(tablero)))-2):
            triada = [tablero[i+j], tablero[i+j+1], tablero[i+j+2]]
            punt += evalua_triada(triada,icon)
            #print(triada)

    #Posiciones Verticales
    for i in range(0, int(math.sqrt(len(tablero)))):
        for j in range(0, int(math.sqrt(len(tablero))) + 1, 4):
            triada = [tablero[i+j], tablero[i+j+4], tablero[i+j+8]]
            punt += evalua_triada(triada,icon)
    #Posicion vertical pos
    for i in range(0, int(math.sqrt(len(tablero)))//2):
        # range (0,5,4) 0 4
        for j in range(0, int(math.sqrt(len(tablero))) + 1, 4):
            triada = [tablero[i+j], tablero[i+j+5], tablero[i+j+10]]
            punt += evalua_triada(triada, icon)
    return punt

def evalua_triada(triada, icon):
    punt = 0
    i_enem = icono_H
    if icon == icono_H:
        i_enem = icono_IA
    if triada.count(icon) == 3:
        punt += 100
    elif triada.count(icon) == 2 and triada.count(i_enem) == 0:
        punt += 5
    elif triada.count(icon) == 1 and triada.count(i_enem) == 0:
        punt += 2
    if triada.count(i_enem) == 2 and triada.count(icon) == 0:
        punt -= 4
    return punt

def minimax(tablero, profundidad, alpha, beta, maxim):

    mov_Posibles = movimientos_validos(tablero)
    esFinal = mov_final(tablero)
    # Si la profundidad es 0 no hace ninguna accion y salia un hermoso ERROR hasta que adapte un numero random
    if profundidad == 0 or esFinal:
        if esFinal:
            if fin(tablero, icono_IA):
                return (None, 100000000000000)
            elif fin(tablero, icono_H):
                return (None, -10000000000000)
            else:
                return (None, 0)
        else:
            #return (random.choice(mov_Posibles), puntuacion(tablero, icono_IA))
            return (random.choice(mov_Posibles), puntuacion(tablero, icono_IA))
    # SI MAXIMIZANDO TRUE
    if maxim:
        valor = -math.inf

        pos_final = random.choice(mov_Posibles)
        # col hace la iteracion una lista[0,1,2,3,4] en el caso de que existan columnas disponibles
        for pos in mov_Posibles:

            copiaTablero = tablero.copy()
            # Se simula el juego en una copia del tablero
            marcar(copiaTablero,pos,icono_IA)
            # que duevuelve minimax que es la puntuacion
            nuevaPuntuacion = minimax(copiaTablero, profundidad - 1, alpha, beta, False)[1]  # Llamada recursiva
            # El minimax se ejecuta hasta que profundidad sea igual a 0 o hasta que a>=b
            if nuevaPuntuacion > valor:
                valor = nuevaPuntuacion
                pos_final = pos
            alpha = max(alpha, valor)
            # si alpha supera a beta ese sera el mejor valor encontrado
            if alpha >= beta:
                break

        return pos_final, valor

    else:
        valor = math.inf
        pos_final = random.choice(mov_Posibles)  # Ojo movimentosPosibles solo tiene el numero de columnas
        for pos in mov_Posibles:

            copiaTablero = tablero.copy()
            # Ojo aqui juega con la pieza de jugador
            marcar(copiaTablero,pos,icono_H)
            # En caso de que sea 6 termina aqui
            nuevaPuntuacion = minimax(copiaTablero, profundidad - 1, alpha, beta, True)[1]
            if nuevaPuntuacion < valor:
                valor = nuevaPuntuacion
                pos_final = pos
            beta = min(beta, valor)
            if alpha >= beta:
                break
        return pos_final, valor


#PRUEBAS
turno = random.randint(0,1)
profundidad = 3

tablero = tablero_crear(TAMANO)
while True:
    icon = str(input("Ingresa el icono que utilizara >X<  o >O<: " )).upper()
    if icon == 'X' or icon == 'O':
        if icon == 'X':
            icono_H = icon
            icono_IA = 'O'
            break
        else:
            icono_IA = 'X'
            icono_H = icon
            break
    else:
        print("Error 002: Icono No Disponible")

while True:
    #print(icono_IA)
    #print(icono_H)
    if turno == 1:
        mostrar_tablero(tablero)
        #Turno de Jugador
        mov = turno_Jugador(tablero)
        marcar(tablero, mov, icono_H)

        if fin(tablero, icono_H):
            mostrar_tablero(tablero)
            print("Gano el jugador")
            break

        if empate(tablero):
            print("Empate \n Se acabo el juego")
            break
        turno = (turno + 1) % 2

    # Turno de la IA
    elif turno == 0:
        #(tablero, profundidad, alpha, beta, max )
        mov1, punt = minimax(tablero, profundidad, -math.inf, math.inf, True)
        marcar(tablero, mov1, icono_IA)
        print(icono_IA)
        mostrar_tablero(tablero)

        if fin(tablero, icono_IA):
            mostrar_tablero(tablero)
            print("Gano la IA, lo siento suerte pa la proxima")
            break

        if empate(tablero):
            print("Empate \n Se acabo el juego")
            break
        turno = (turno + 1) % 2