#3. Elabore un algoritmo genético que encuentre la mejor manera de colocar
#12 bloques de color blanco y 12 bloques de color negro, ubicados para conformar un tablero de ajedrez:

# coding: utf-8

import random
import numpy as np
import pygame,sys
from pygame.locals import *
import math

crema = (255, 255, 199)
cafe = (128, 64, 0)

class tablero ():
    def __init__ (self,genes_disp, tab_final,  tamano_pob, n_select, porc_muta, n_generaciones):
        self.genes_disp = genes_disp
        self.tab_final = tab_final
        self.tamano_pob = tamano_pob
        self.n_select = n_select
        self.porc_muta = porc_muta
        self.n_generaciones = n_generaciones
        self.mejor_tab = None

    #SOLO CREA UN INDIVIDUO
    def crear_ind(self):
        ind = []
        for i in range(len(self.tab_final)):
            valor = self.genes_disp[random.randint(0, len(self.genes_disp)-1)]
            ind.append(valor)
        return ind

    #CREA LA POBLACION
    def crear_poblacion(self):
        poblacion = []
        for i in range(self.tamano_pob):
            ind = self.crear_ind()
            poblacion.append(ind)
        return poblacion

    #EVALUACION DE UN INDIVIDUO --- Fitness
    def fitness(self, ind):
        punt = 0
        for i in range (len(ind)):
            if ind[i] == self.tab_final[i]:
                punt += 1
        return punt
    
    def fitness_2(self, ind):
        punt = 0
        for i in range(len(ind)):
            if ind[i] == 0:
                if (i + 1) % 6 != 1 and ind[i - 1] == 1:
                    punt += 1
                if (i + 1) % 6 != 0 and ind[i + 1] == 1:
                    punt += 1
                if i + 6 < len(ind) and ind[i + 6] == 1:
                    punt += 1
                if i - 6 >= 0 and ind[i - 6] == 1:
                    punt +=1
            else:
                if (i + 1) % 6 != 1 and ind[i - 1] == 0:
                    punt += 1
                if (i + 1) % 6 != 0 and ind[i + 1] == 0:
                    punt += 1
                if i + 6 < len(ind) and ind[i + 6] == 0:
                    punt += 1
                if i - 6 >= 0 and ind[i - 6] == 0:
                    punt += 1
        return punt
    
    #SELECCIONADOS ALMACENADOS EN TUPLAS EN UNA LISTA
    def seleccion(self, poblacion):

        tab_sel = []
        for i in poblacion:
            tab_sel.append((self.fitness(i), i))

        tab_sel_ordenado = []
        for i in sorted(tab_sel):
            tab_sel_ordenado.append(i[1])

        seleccionados = tab_sel_ordenado[len(tab_sel_ordenado)-self.n_select:]
        self.mejor_tab = tab_sel_ordenado[len(tab_sel_ordenado)-1]
        return seleccionados

    #SE GENERA EL CRUCE
    def cruzar(self, poblacion, seleccionados):
        medio = 0
        padre = []

        for i in range(len(poblacion)):
            medio = np.random.randint(1, len(self.tab_final)-1)
            #Se selecciona una tupla de padres de seleccionados para crear la nueva poblacion
            padre = random.sample(seleccionados, 2)
            #print(padre)
            poblacion[i][:medio] = padre[0][:medio]
            poblacion[i][medio:] = padre[1][medio:]

        return poblacion

    def mutar(self, poblacion):
        for i in range(len(poblacion)):
            if random.random() <= self.porc_muta:
                point = random.randint(1,len(self.tab_final) - 1)
                new_value = np.random.randint(0, 2)

                while new_value == poblacion[i][point]:
                    new_value = np.random.randint(0, 2)
                poblacion[i][point] = new_value
        return poblacion

    def corre_alg_gen(self):
        poblacion = self.crear_poblacion()

        for i in range(self.n_generaciones):

            print("Nueva Poblacion: ")
            print(poblacion)

            seleccionados = self.seleccion(poblacion)
            poblacion = self.cruzar(poblacion, seleccionados)
            poblacion = self.mutar(poblacion)

        print(f"La mejor opcion es : {self.mejor_tab}")


# FUNCIONES PARA MOSTRAR
def dibujar_pygame(tablero,ventana,inicio_x):
    tam = 90
    pos = 0
    for i in range(4):
        y = i
        for j in range(6):
            if tablero[pos] == 1:
                pygame.draw.rect(ventana, crema, (inicio_x + j * tam, y * tam, tam, tam))
            else:
                pygame.draw.rect(ventana, cafe, (inicio_x + j * tam, y * tam, tam, tam))
            pos += 1


def dibujar_dis(dis):
    for i in range(0, 24, 6):
        print(f"| {dis[i]}  {dis[i+1]}  {dis[i+2]}  "
              f"{dis[i+3]}  {dis[i+4]}  {dis[i+5]} |")

#INICIO DEL PROCESO DE GENERACIONES
tab_final = [0, 1, 0, 1, 0, 1,
             1, 0, 1, 0, 1, 0,
             0, 1, 0, 1, 0, 1,
             1, 0, 1, 0, 1, 0]
#(genes, objetivo, tamaño de la poblacion, numero de selesccionados, posibilidad de mutar, numero de genereaciones)
tab = tablero([0, 1], tab_final, 20, 7, 0.05, 100)
tab.corre_alg_gen()
dibujar_dis(tab.mejor_tab)


# PARTE EN PYGAME
pygame.init()
vent_inicial =pygame.display.set_mode((1100, 400))
pygame.display.set_caption("Hola Mundo")

dibujar_pygame(tab_final, vent_inicial, 0)
dibujar_pygame(tab.mejor_tab, vent_inicial, 550)

while True:
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
