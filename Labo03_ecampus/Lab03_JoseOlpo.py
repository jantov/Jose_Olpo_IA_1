#Implemente un algoritmo genético para resolver el problema del tablero de interruptores que generan un numero clave
# de acceso. Se cuenta con un tablero con 32 interruptores binarios, que cada uno de ellos puede estar en encendido
# o apagado y cada 8 se considera que es una letra o caracter ascii, dada una clave determinada que se introducirá
# por teclado, el algoritmo genético deberá encontrar la combinación respectiva de interruptores que le permita
# generar la clave introducida

import random
import numpy as np

class cifrado():
    def __init__(self, clave_intr, tam_poblacion, n_select, prob_mutar, n_generaciones):
        self.clave_intr = clave_intr
        self.tam_poblacion = tam_poblacion
        self.n_select = n_select
        self.prob_mutar = prob_mutar
        self.n_generaciones = n_generaciones
        self.sol = self.clave_binario(self.clave_intr)
        self.mejor_solucion = None

    #LISTA DE OPERACIONES Y TRANSFORMACIONES
    def binario_decimal(self, bin ):
        dec = 0
        for i,j in enumerate(bin):
            dec = dec + j*2**i
        return int(dec)
    def decimal_binario(self, dec):
        bin = []
        for i in range(8):
            res = int(dec%2)
            dec = dec//2
            bin.append(res)
        return bin

    def binario_clave(self, binario):
        clave = ''
        for i in range(0,32,8):
            dec = self.binario_decimal(binario[i:i+7])
            cl1 = chr(int(dec))
            clave = clave + str(cl1)
        return clave


    def clave_binario(self, clave):
        binario = []
        for i in range(len(clave)):
            num = ord(clave[i])
            bin1 = self.decimal_binario(num)
            binario = binario + bin1
        return binario


    def gen_ind(self):
        ind = []
        for i in range(len(self.sol)):
            ind.append(random.randint(0, 1))
        return ind

    def gen_poblacion(self):
        poblacion = []
        for i in range(self.tam_poblacion):
            poblacion.append(self.gen_ind())
        return poblacion


    #FITNESS QUE CALCULA EL VALOR CADA 8 BITS Y COMPARA CON EL VALOR DECIMAL DE LA CLAVE(POCO EFICIENTE)
    def fitness(self, ind):
        punt = 0
        for i in range(0, 32, 8):
            punt = punt + abs(self.binario_decimal(ind[i: i+8]) - self.binario_decimal(self.sol[i: i+8]))
        return punt
    # FItness pa comparar si es igual el codigogeneteico
    def fitness2(self, ind):
        punt = 0
        for i in range(len(ind)):
            if self.sol[i] != ind[i]:
                punt+= 1
        return punt

    def ordenar_por_fit(self, poblacion):
        pob_fit = []
        pob_ord = []
        for i in poblacion:
            pob_fit.append((self.fitness2(i), i))
        for i in sorted(pob_fit):
            pob_ord.append(i[1])
        return pob_ord


    def seleccion(self, poblacion):
        selec_1 = self.ordenar_por_fit(poblacion)
        seleccionados = selec_1[:self.n_select]
        self.mejor_solucion = seleccionados[0]
        return seleccionados

    def cruzar1(self, poblacion):
        medio = np.random.randint(1, len(self.sol) - 1)
        pob = self.ordenar_por_fit(poblacion)[self.n_select:]
        sel = self.seleccion(poblacion)
        if random.randint(0, 1) == 0:
            hijos = sel[:]
            for i in range(len(pob)//2):
                hijos.append(pob[0][:medio]+pob[1][medio:])
                hijos.append(pob[1][:medio]+pob[0][medio:])
                pob.pop(0)
                pob.pop(0)
        else:
            hijos = pob[:]
            for i in range(len(sel)//2):
                hijos.append(sel[0][:medio] + sel[1][medio:])
                hijos.append(sel[1][:medio] + sel[0][medio:])
                sel.pop(0)
                pob.pop(0)
        return hijos

    #CRUZAR 2 ES POCO EFICIENTE
    def cruzar2(self, poblacion):
        medio = np.random.randint(1, len(self.sol) - 1)
        pob = self.ordenar_por_fit(poblacion)[self.n_select:]
        sel = self.seleccion(poblacion)
        hijos = sel[:]
        for i in range(len(pob)//2):
            hijos.append(pob[0][:medio]+pob[1][medio:])
            hijos.append(pob[1][:medio]+pob[0][medio:])
            pob.pop(0)
            pob.pop(0)
        print(len(hijos))
        return hijos

    def mutar(self, poblacion):
        for i in range(len(poblacion)):
            if random.random() <= self.prob_mutar:
                pos = random.randint(0, len(self.sol) - 1)
                poblacion[i][pos] = (poblacion[i][pos] + 1) % 2
        return poblacion

    def algoritmo_genetico(self):
        poblacion = self.gen_poblacion()
        for i in range(self.n_generaciones):
            print("Nueva Poblacion: ")
            print(poblacion)

            poblacion = self.cruzar1(poblacion)
            poblacion = self.mutar(poblacion)

        clav_retor = self.binario_clave(self.mejor_solucion)
        clave_inicial = self.binario_clave((self.sol))
        print(f"\n\nRespuesta:{self.sol} con su clave: {clave_inicial} \nLa mejor opcion es : {self.mejor_solucion} y su clave es: {clav_retor}")
        print(len(self.mejor_solucion))

#SE PODRIA PONER UNA FUNCION PARA PARA VALIDAR EL ASCII EN CASO DE QUE AÑADAMOS CARACTERES DEL UNICODE
while True:
    clave = str(input("Ingrese la clave (la clave debe ser de 4 caracteres exactos): "))
    if len(clave)!=4:
        print("ERRO_001: Ingrese Nuevamente la clave")
    else:
        break
#clave_intr, tam_poblacion, n_select, prob_mutar, n_generaciones
cifr = cifrado(clave, 30, 14, 0.1, 500)
cifr.algoritmo_genetico()
