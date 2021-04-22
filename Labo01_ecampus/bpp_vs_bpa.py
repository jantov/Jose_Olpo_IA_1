# Puzle lineal con Busqueda en Profundidad - Deep First Search
# UTILIZAR EN MISMA CARPTEA DONDE SE ENCUENTRA EL ARCHIVO NODOS.py
from Nodos import Nodo

def busqueda_BPA(estado_inicial, solucion):
    resuelto = False
    nodos_visitados = []
    nodos_frontera = []
    nodo_raiz = Nodo(estado_inicial)
    nodos_frontera.append(nodo_raiz)
    while (not resuelto) and len(nodos_frontera) != 0:
        nodo_actual = nodos_frontera.pop(0)
        # Extraer nodo y añadirlo a visitados
        nodos_visitados.append(nodo_actual)
        if nodo_actual.get_estado() == solucion:
            # Solucion encontrada
            resuelto = True
            return nodo_actual
        else:
            # Expandir nodos hijos
            datos_nodo = nodo_actual.get_estado()
            # Operador 1
            hijo = [datos_nodo[1], datos_nodo[0], datos_nodo[2], datos_nodo[3], datos_nodo[4]]
            hijo_1 = Nodo(hijo)
            if not hijo_1.en_lista(nodos_visitados) and not hijo_1.en_lista(nodos_frontera):
                nodos_frontera.append(hijo_1)
            # Operador 2
            hijo = [datos_nodo[0], datos_nodo[2], datos_nodo[1], datos_nodo[3], datos_nodo[4]]
            hijo_2 = Nodo(hijo)
            if not hijo_2.en_lista(nodos_visitados) and not hijo_2.en_lista(nodos_frontera):
                nodos_frontera.append(hijo_2)
            # Operador 3
            hijo = [datos_nodo[0], datos_nodo[1], datos_nodo[3], datos_nodo[2], datos_nodo[4]]
            hijo_3 = Nodo(hijo)
            if not hijo_3.en_lista(nodos_visitados) and not hijo_3.en_lista(nodos_frontera):
                nodos_frontera.append(hijo_3)
            # Operador 4
            hijo = [datos_nodo[0], datos_nodo[1], datos_nodo[2], datos_nodo[4], datos_nodo[3]]
            hijo_4 = Nodo(hijo)
            if not hijo_4.en_lista(nodos_visitados) and not hijo_4.en_lista(nodos_frontera):
                nodos_frontera.append(hijo_4)
            nodo_actual.set_hijo([hijo_1, hijo_2, hijo_3, hijo_4])



def busqueda_BPP(estado_inicial, solucion):
    resuelto = False
    nodos_visitados = []
    nodos_frontera = []
    nodo_raiz = Nodo(estado_inicial)
    nodos_frontera.append(nodo_raiz)
    while (not resuelto) and len(nodos_frontera) != 0:
        nodo_actual = nodos_frontera.pop()
        # Extraer nodo y añadirlo a visitados
        nodos_visitados.append(nodo_actual)
        if nodo_actual.get_estado() == solucion:
            # Solucion encontrada
            resuelto = True
            return nodo_actual
        else:
            # Expandir nodos hijos
            datos_nodo = nodo_actual.get_estado()
            # Operador 1
            hijo = [datos_nodo[1], datos_nodo[0], datos_nodo[2], datos_nodo[3], datos_nodo[4]]
            hijo_1 = Nodo(hijo)
            if not hijo_1.en_lista(nodos_visitados) and not hijo_1.en_lista(nodos_frontera):
                nodos_frontera.append(hijo_1)
            # Operador 2
            hijo = [datos_nodo[0], datos_nodo[2], datos_nodo[1], datos_nodo[3], datos_nodo[4]]
            hijo_2 = Nodo(hijo)
            if not hijo_2.en_lista(nodos_visitados) and not hijo_2.en_lista(nodos_frontera):
                nodos_frontera.append(hijo_2)
            # Operador 3
            hijo = [datos_nodo[0], datos_nodo[1], datos_nodo[3], datos_nodo[2], datos_nodo[4]]
            hijo_3 = Nodo(hijo)
            if not hijo_3.en_lista(nodos_visitados) and not hijo_3.en_lista(nodos_frontera):
                nodos_frontera.append(hijo_3)
            # Operador 4
            hijo = [datos_nodo[0], datos_nodo[1], datos_nodo[2], datos_nodo[4], datos_nodo[3]]
            hijo_4 = Nodo(hijo)
            if not hijo_4.en_lista(nodos_visitados) and not hijo_4.en_lista(nodos_frontera):
                nodos_frontera.append(hijo_4)
            nodo_actual.set_hijo([hijo_1, hijo_2, hijo_3, hijo_4])


if __name__ == "__main__":
    estado_inicial = [4, 3, 5, 2, 1]
    solucion = [1, 2, 3, 4, 5]
    nodo_solucion_BPA = busqueda_BPA(estado_inicial, solucion)
    nodo_solucion_BPP = busqueda_BPP(estado_inicial, solucion)
    # Mostrar resultado
    resultado1 = []
    resultado2 = []
    nodo_actual1 = nodo_solucion_BPA
    nodo_actual2 = nodo_solucion_BPP
    c1 = 0
    c2 = 0
    while nodo_actual1.get_padre() is not None:
        c1 += 1
        resultado1.append(nodo_actual1.get_estado())
        nodo_actual1 = nodo_actual1.get_padre()

    while nodo_actual2.get_padre() is not None:
        c2 += 1
        resultado2.append(nodo_actual2.get_estado())
        nodo_actual2 = nodo_actual2.get_padre()

    resultado1.append(estado_inicial)
    resultado1.reverse()
    print('Iteraciones totales son {}'.format(c1))
    print(resultado1)
    print('Iteraciones totales son {}'.format(c2))
    print(resultado2)
