# 1. Elaborar un agente que resuelva un rompecabezas de 3X5
#   (utilice un algoritmo que permita resolverlo en menos de 1 minuto).
# Metodo de desarrollo A* con 2 heuristicas

import math
import os
import sys
import time
import copy
from queue import PriorityQueue

#UNICA CLASE YA QUE CON LA OTRA CLASE ME HICE BOLAS
class Romp:
    def __init__(self, estados, est_padre):
        self.tamano_x = 3
        self.tamano = 5
        self.estados = estados
        self.est_padre = est_padre

    def estado_act(self):
        return  self.estados

    def ejecutar_accion(self, accion):
        estado_padre = self.estados[:]
        nuevos_estados = self.estados[:]
        indice_vacio = nuevos_estados.index('0')
        if accion == 'Izquierda':
            if indice_vacio % self.tamano > 0:
                nuevos_estados[indice_vacio - 1], nuevos_estados[indice_vacio] = nuevos_estados[indice_vacio], nuevos_estados[indice_vacio - 1]
        if accion == 'Derecha':
            if indice_vacio % self.tamano < (self.tamano - 1):
                nuevos_estados[indice_vacio + 1], nuevos_estados[indice_vacio] = nuevos_estados[indice_vacio], nuevos_estados[indice_vacio + 1]
        if accion == 'Arriba':
            if indice_vacio - self.tamano >= 0:
                nuevos_estados[indice_vacio - self.tamano], nuevos_estados[indice_vacio] = nuevos_estados[indice_vacio], nuevos_estados[
                    indice_vacio - self.tamano]
        if accion == 'Abajo':
            if indice_vacio + self.tamano < self.tamano_x * self.tamano:
                nuevos_estados[indice_vacio + self.tamano], nuevos_estados[indice_vacio] = nuevos_estados[indice_vacio], nuevos_estados[
                    indice_vacio + self.tamano]
        return Romp(nuevos_estados, estado_padre)
#HEURISTICAS
def validar_1_fila(estado):
    fila = ['1', '2', '3', '4', '5']
    for i in fila:
        if fila.index(i) - estado.index(i) != 0:
            return False
    return True
def heurisitica_escalada_pos(estado):
    cont = 0
    fila1 = ['1', '2', '3', '4', '5']
    fila2 = ['6', '7', '8', '9', '10', '11', '12', '13', '14']
    #fila3 = []
    for i in fila1:
        if fila1.index(i) - estado.index(i) != 0:
            index = estado.index(i)
            #               0   /   3  - 7  /   3               0 % 5   -   7 % 5
            cont += (abs((int(i) / 5) - (index / 5)) + abs((int(i) % 5) - (index % 5)))
            cont *= 2
    for i in fila2:
        if fila2.index(i)+5 - estado.index(i) != 0:
            index = estado.index(i)
            cont += (abs((int(i) / 5) - (index / 5)) + abs((int(i) % 5) - (index % 5)))
    return cont

def euristica_escalada_distancia(estado):
    cont = 0
    fila = ['1', '2', '3', '4', '5']
    for i in fila:
        if fila.index(i) - estado.index(i) != 0:
            index = estado.index(i)
            cont += (abs((int(i) / 3) - (index / 3)) + abs((int(i) % 5) - (index % 5)))
    return cont

def distancia_cero_num(estado):
    cont = 0
    fila = ['1', '2', '3', '4', '5']
    for i in fila:
        if fila.index(i) - estado.index(i) != 0:
            index = estado.index(i)
            cont += (abs((int(i) / 3) - (index / 3)) + abs((int(i) % 5) - (index % 5)))
            index = estado.index('0')
            cont += (abs((int(i) / 3) - (index / 3)) + abs((int(i) % 5) - (index % 5)))
            return cont
    return cont


def heuristica1(estado):
    #PRIMERA LINEA DE ROMPECABEZAS PRIMERA PRIORIDAD Y MAYOR PUNTUACION
    cont = 0
    fila = ['1', '2', '3', '4', '5']
    for i in fila:
        if fila.index(i) - estado.index(i) != 0:
            cont += 3
    return cont

def heuristica2(estado):
    #CUADRANTE 1
    cont = 0
    linea1 = ['6', '7']
    linea2 = ['11', '12']
    for i in linea1:
        if linea1.index(i)+5 - estado.index(i) != 0:
            cont += 2
    for i in linea2:
        if linea2.index(i)+10 - estado.index(i) != 0:
            cont += 2
    return cont

def heurisitca_escuadra(estado):
    cont = 0
    esc_val = ['1', '2', '3', '6', '11']
    ind_val = [0, 1, 2, 5, 10]
    j = 0
    for i in esc_val:
        if (ind_val[j] - estado.index(i)) != 0:
            cont += 1
            j += 1
    return cont

#HEURISTICA ROBADA
def manhattan_calculate(estados):
    '''heuristicaa Manhattan: cuenta el numero de cuadros a partir de una ubicacion en relacion a su posicion final'''
    contador = 0
    for i in range(0, 14):
        index = estados.index(str(i + 1))  # because range starts at 0
        contador += (abs((i / 3) - (index / 3)) + abs((i % 5) - (index % 5)))  # %4 is the column and /4 is the row
    return contador

def hamming(estados):
    ''' heuristicaa Hamming: cuenta el numero de posiciones erroneas en diferentes estados'''
    distancia = 0
    objetivo_estados = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14']
    for i in objetivo_estados:
        if objetivo_estados.index(i) - estados.index(i) != 0 and i != 0:
            distancia += 1
    return distancia

def heuristica_Combinada(estado):
    c = 0
    c += heurisitca_escuadra(estado)
    #c += heuristica1(estado)
    #c += heurisitica_escalada_pos(estado)
    #c += hamming(estado)
    c += manhattan_calculate(estado)
    return c


#AQUI SE GENERARN LOS BEBES
def generar_hijos(padre):
    hijos = []
    acciones = ['Arriba', 'Abajo', 'Derecha', 'Izquierda']
    for accion in acciones:
        hijo_estado = padre.ejecutar_accion(accion)
        hijo_Nodo = Romp(hijo_estado.estados, padre)
        hijos.append(hijo_Nodo)
    return hijos

#UTILIZAMOS EL MISMO QUE EL DEL EJERCICIO
def gcalc(Nodo):
    ''' calcula g(n): encuentra el costo del estado actual a partir del estado origen o inicial'''
    contador = 0
    while Nodo.est_padre is not None:
        Nodo = Nodo.est_padre
        contador += 1
    return contador

def objetivo():
    return ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '0']

def num_str1(x):
    if len(x)<2:
        return (f" {x}")
    return x

def mostrar_pasos(paso):
    '''Retorna el Proceso'''
    pasos = []
    while (paso.est_padre is not None):
        pasos.append(paso.estados)
        paso = paso.est_padre
    pasos.reverse()
    for i in pasos:
        j = 0
        while(j <14):
            print(f"| {num_str1(i[j])} {num_str1(i[j+1])} {num_str1(i[j+2])}"
                  f" {num_str1(i[j+3])} {num_str1(i[j+4])} |")
            j += 5
        print('--*--*--*--*--*--*')

def a_estrella(estado_inicial, estado_objetivo):
    '''A* Search Algorithm'''
    start_time = time.time()
    frontera = list()
    contador = 0
    obj_visitado = list()
    est_visitado = list()
    frontera.append(estado_inicial)
    obj_visitado.append(estado_inicial)
    est_visitado.append(estado_inicial.estados)
    while frontera:
        valor_Mov = []
        movimientos_pos = []
        for x in frontera:
            #CAMBIAR A UNA SOLA H
            valor_Mov.append(heuristica_Combinada(x.estados) + gcalc(x))
            #HASTA ACA
            movimientos_pos.append(x)


        m = min(valor_Mov)  # finds minimum F value
        estado_inicial = movimientos_pos[valor_Mov.index(m)]

        #print(estado_inicial.estados)
        if estado_inicial.estados == estado_objetivo:  # solution found!
            end_time = time.time()

            print("Solucion:\n\n")
            mostrar_pasos(estado_inicial)

            #print("Movimientos: " + str(' '.join(find_path(estado_inicial))))
            print("Numero de nodos expandidos: " + str(contador))
            print("Tiempo empleado: " + str(round((end_time - start_time), 3)))
            # print("Memory Used: " + str(sys.gettamanoof(visitado) + sys.gettamanoof(frontera)) + " kb")
            break

        frontera.pop(frontera.index(estado_inicial))
        for hijo in generar_hijos(estado_inicial):
            contador += 1
            s = hijo.estados
            #print(s)

            if s not in est_visitado or gcalc(hijo) <= gcalc(obj_visitado[est_visitado.index(s)]):
                est_visitado.append(s)
                obj_visitado.append(hijo)
                frontera.append(hijo)

                # if len(est_visitado) > 30:
                #     est_visitado.pop(0)
                #     obj_visitado.pop(0)
        if time.time() > start_time + 60:
            mostrar_pasos(estado_inicial)
            break

def main():
    # NO REALIZABLES
    #ei = ['2', '14', '3', '5', '1', '6', '8', '12', '4', '0', '13', '7', '11', '9', '10']
    #ei = ['1', '3', '4', '8', '5', '2', '0', '6', '9', '10', '7', '11', '13', '14', '12']
    #ei = ['0', '1', '2', '3', '5', '6', '7', '4', '8', '9', '10', '11', '12', '13', '14']
    # SI REALIZABLES
    #ei = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '0', '11', '12', '13', '14']
    #ei = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '11', '12', '13', '14', '10']

    #ei = ['0', '1', '2', '3', '5', '6', '7', '8', '4', '10', '11', '12', '13', '9', '14']
    ei = ['0', '1', '2', '3', '4', '7', '8', '9', '10', '5', '6', '11', '12', '13', '14']
    a_estrella(Romp(ei, None), objetivo())

    print('----------------FIN----------------')


if __name__ == '__main__':
    main()