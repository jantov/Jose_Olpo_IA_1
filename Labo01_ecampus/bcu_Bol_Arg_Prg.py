# Búsqueda Coste Uniforme - Uniform Cost Search
# -*- coding: utf-8 -*-
from Nodos import Nodo

def Comparar(nodo):
    return nodo.get_costo()

def busqueda_BCU(conecciones, estado_inicial, solucion):
    resuelto = False
    nodos_visitados = []
    nodos_frontera = []
    nodo_raiz = Nodo(estado_inicial)
    nodo_raiz.set_costo(0)
    nodos_frontera.append(nodo_raiz)
    while (not resuelto) and len(nodos_frontera) != 0:
        # Ordenar lista de nodos frontera
        nodos_frontera = sorted(nodos_frontera, key=Comparar)
        nodo_actual = nodos_frontera[0]
        # Extraer nodo y añadirlo a visitados
        nodos_visitados.append(nodos_frontera.pop(0))
        if nodo_actual.get_estado() == solucion:
            # Solucion encontrada
            resuelto = True
            return nodo_actual
        else:
            # Expandir nodos hijo (ciudades con conexion)
            datos_nodo = nodo_actual.get_estado()
            lista_hijos = []
            for achild in conecciones[datos_nodo]:
                hijo = Nodo(achild)
                costo = conecciones[datos_nodo][achild]
                hijo.set_costo(nodo_actual.get_costo() + costo)
                lista_hijos.append(hijo)
                if not hijo.en_lista(nodos_visitados):
                    # Si está en la lista lo sustituimos con el nuevo valor de coste si es menor
                    if hijo.en_lista(nodos_frontera):
                        for n in nodos_frontera:
                            if n.equal(hijo) and n.get_costo() > hijo.get_costo():
                                nodos_frontera.remove(n)
                                nodos_frontera.append(hijo)
                    else:
                        nodos_frontera.append(hijo)
            nodo_actual.set_hijo(lista_hijos)


if __name__ == "__main__":
    conecciones = {
        'Sucre': {'Potosi': 155, 'Cochabamba': 330, 'Oruro': 331, 'Santa Cruz': 484, 'Filadelfia': 984},
        'Potosi': {'Sucre': 155, 'Oruro': 311, 'Tarija': 346, 'San Salvador de Jujuy': 630},
        'Tarija': {'Potosi': 346, 'Santa Cruz': 666, 'Filadelfia': 642, 'Salta': 520, 'San Salvador de Jujuy': 460},
        'Oruro': {'Cochabamba': 214, 'La Paz': 226, 'Potosi': 311, 'Sucre': 331},
        'Cochabamba': {'Sucre': 330, 'La Paz': 378, 'Oruro': 214, 'Santa Cruz': 483, 'Trinidad': 925},
        'Santa Cruz': {'Sucre': 484, 'Tarija': 666, 'Trinidad': 554, 'Filadelfia': 882},
        'Trinidad': {'Santa Cruz': 554, 'Cobija': 1190, 'La Paz': 597, 'Cochabamba': 925},
        'Cobija': {'Trinidad': 1190, 'La Paz': 1306},
        'La Paz': {'Oruro': 226, 'Cochabamba': 378, 'Trinidad': 597, 'Cobija': 1306},

        'Filadelfia': {'Sucre': 984, 'Tarija': 642, 'Fuerte Olimpo': 351, 'Villa Hayes': 282, 'Asuncion': 453,
                       'Santa Cruz': 882, 'Salta': 844},
        'Fuerte Olimpo': {'Filadelfia': 351},
        'Villa Hayes': {'Concepcion': 102, 'Filadelfia': 282, 'Asuncion': 356},
        'Concepcion': {'Villa Hayes': 102, 'Pedro Juan Caballero': 214, 'San Pedro': 195, 'Salto de Guaira': 490,
                       'Caacupe': 392, 'Asuncion': 412, 'Coronel Oviedo': 350},
        'Pedro Juan Caballero': {'Salto de Guaira': 531,'Concepcion': 214, 'San Pedro': 276, 'Asuncion': 452,
                                 'Caacupe': 432, 'Coronel Oviedo': 390},
        'San Pedro': {'Concepcion': 195, 'Pedro Juan Caballero': 214,'Asuncion': 327,'Coronel Oviedo':265,
                      'Salto de Guaira': 405, 'Caacupe': 307},
        'Salto de Guaira': {'Concepcion': 490, 'San Pedro': 405, 'Pedro Juan Caballero': 531, 'Caacupe': 388,
                            'Asuncion': 408, 'Ciudad del Este': 234, 'Coronel Oviedo': 315},
        'Asuncion': {'Filadelfia': 453, 'Villa Hayes': 356, 'Concepcion': 412, 'Pedro Juan Caballero': 452,
                     'San Pedro': 327, 'Salto de Guaira': 408,'Aregua': 24},
        'Caacupe': {'Concepcion': 392, 'Pedro Juan Caballero': 432, 'San Pedro': 307, 'Salto de Guaira': 388,
                    'Aregua':37, 'Paraguari': 39, 'Coronel Oviedo': 98, 'Villarrica': 113, 'Ciudad del Este': 268},
        'Aregua': {'Asuncion': 24, 'Caacupe': 37, 'Paraguari':58},
        'Coronel Oviedo': {'Concepcion': 350, 'Pedro Juan Caballero': 390, 'San Pedro': 265, 'Caacupe': 98,
                           'Salto de Guaira': 265, 'Ciudad del Este': 206, 'Villarrica': 59},
        'Ciudad del Este': {'Encarnacion': 291, 'Villarrica': 219, 'Salto de Guaira': 234, 'Caacupe': 268,
                            'Coronel Oviedo': 206},
        'Villarrica': {'Caazapa': 54, 'Paraguari': 87, 'Ciudad del Este': 206, 'Coronel Oviedo': 59, 'Caacupe': 113},
        'Paraguari': {'Villarrica': 87, 'Aregua': 58, 'Caacupe': 39, 'San Juan Bautista': 113},
        'Pilar': {'Caazapa': 369, 'San Juan Bautista': 166, 'Encarnacion': 271, 'Formosa': 117, 'Corrientes': 164},
        'San Juan Bautista': {'Pilar': 166, 'Paraguari': 113, 'Encarnacion': 166},
        'Encarnacion': {'Caazapa': 182, 'Pilar': 271, 'San Juan Bautista': 166, 'Ciudad del Este': 268, 'Posadas': 31},
        'Caazapa':{'Villarrica': 54, 'Encarnacion': 182, 'Pilar': 369, },

        'Salta': {'Tarija': 520, 'San Salvador de Jujuy': 93, 'Corrientes': 836, 'Tucuman': 307, 'Santa Fe': 1034,
                  'Cordoba': 876, 'Filadelfia': 844},
        'San Salvador de Jujuy': {'Salta': 93, 'Tarija': 460, 'Potosi': 630, },
        'Tucuman':{'Salta': 307, 'Mendoza': 957, 'Cordoba': 570, 'Corrientes': 787, 'Santa Fe': 777},
        'Formosa': {'Corrientes': 187, 'Pilar': 117, 'Asuncion': 156},
        'Santa Fe': {'Corrientes': 565, 'Salta': 1034, 'Tucuman': 777, 'Parana': 31, 'Ciudad de Buenos Aires': 468,
                     'Cordoba': 362},
        'Cordoba': {'Santa Fe': 362, 'Mendoza': 656, 'Salta': 876, 'Tucuman': 559, 'Ciudad de Buenos Aires': 695,
                    'Neuquen': 1116},
        'Mendoza': {'Tucuman': 957, 'Cordoba': 656, 'Neuquen': 795, 'Ciudad de Buenos Aires': 1050},
        'Corrientes': {'Formosa': 187, 'Pilar': 164, 'Posadas': 319, 'Salta': 836, 'Tucuman': 787, 'Santa Fe': 565,
                       'Ciudad de Buenos Aires': 917},
        'Posadas': {'Encarnacion': 31, 'Corrientes': 319, 'Ciudad de Buenos Aires': 1001, 'Parana': 755},
        'Parana': {'Posadas': 755, 'Ciudad de Buenos Aires': 453, 'Santa Fe': 31},
        'La Plata': {'Ciudad de Buenos Aires': 58, 'Mar del Plata': 370, 'Neuquen': 1163, 'Rawson': 1438},
        'Ciudad de Buenos Aires': {'La Plata': 58, 'Parana': 453, 'Posadas': 1001, 'Corrientes': 917, 'Mendoza': 1050,
                                   'Cordoba': 695, 'Santa Fe': 468, 'Neuquen': 1142},
        'Mar del Plata': {'La Plata': 370, 'Neuquen': 997, 'Rawson': 1198},
        'Neuquen': {'Rawson': 744, 'Mar del Plata': 997, 'Ciudad de Buenos Aires':1142, 'La Plata': 1163, 'Mendoza': 795,
                    'Cordoba': 1116},
        'Rawson': {'Neuquen': 744, 'Mar del Plata': 997, 'La Plata': 1438, 'Rio Gallegos': 1162},
        'Rio Gallegos': {'Rawson': 1162},
        
        'Arica': {'La Paz': 489, 'Oruro': 474, 'Iquique': 309, 'Calama':599},
        'Iquique': {'Arica': 309, 'Oruro': 479, 'Antofagasta': 416, 'Calama': 384},
        'Calama': {'Potosi': 631, 'Arica': 599, 'Iquique': 384, 'Antofagasta': 217,'San Salvador de Jujuy': 576},
        'Antofagasta': {'Iquique': 316, 'Calama': 217, 'Copiapo': 539},
        'Copiapo': {'Antofagasta': 539, 'Tucuman': 1033, 'La Serena': 337},
        'La Serena': {'Copiapo': 337, 'Mendoza': 666, 'Valparaiso': 431, 'Santiago': 472},
        'Valparaiso': {'Santiago': 115, 'La Serena': 431, },
        'Santiago': {'Mendoza': 363, 'Valparaiso': 115, 'La Serena': 472, 'Ranacagua': 87},
        'Ranacagua': {'Santiago': 87, 'Talca': 172},
        'Talca': {'Ranacagua': 172, 'Chillan': 151},
        'Chillan': {'Talca': 151, 'Concepcion': 99, 'Temuco': 277},
        'Cocepcion': {'Temuco': 293, 'Chillan': 99},
        'Temuco': {'Chillan': 277, 'Concepcion': 293, 'Neuquen': 513, 'Valdivia': 169},
        'Valdivia': {'Temuco': 169, 'Puerto Mont': 213},
        'Puerto Mont': {'Valdivia': 213, 'Coyhaique': 660},
        'Coyhaique': {'Rawson': 776, 'Puerto Mont': 660, 'Rio Gallegos': 1152},
        'Punta Arenas': {'Rio Gallegos': 262}
    }
    estado_inicial = 'Punta Arenas'
    solucion = 'Cobija'
    nodo_solucion = busqueda_BCU(conecciones, estado_inicial, solucion)
    # Mostrar resultado
    resultado = []
    nodo = nodo_solucion
    while nodo.get_padre() is not None:
        resultado.append(nodo.get_estado())
        nodo = nodo.get_padre()
    resultado.append(estado_inicial)
    resultado.reverse()
    print(resultado)
    print("Costo: %s" % str(nodo_solucion.get_costo()))
