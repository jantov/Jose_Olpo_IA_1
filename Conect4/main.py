import numpy as np
import pygame
import sys
import math
import random

AZUL = (0, 0, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
AMARILLO = (255, 255, 0)

NUMRENGLONES = 6
NUMCOLUMNAS = 7

JUGADOR = 0
IA = 1

VACIO = 0
PIEZAJUGADOR = 1
PIEZA_IA = 2

TAMVENTANA = 4

def crearTablero():
	#LIB_numpy : zeros crea un vector o matriz lleno de ceros zeros()
	tablero = np.zeros((NUMRENGLONES, NUMCOLUMNAS))
	return tablero

def soltarPieza(tablero, renglon, columna, pieza):
	tablero[renglon][columna] = pieza

def movimientoValido(tablero, columna):
	#Retorna True existe al menos una casilla vacia en la columna y False y la columna esta llena
	return tablero[NUMRENGLONES-1][columna] == 0

def getRenglonValido(tablero, columna):
	#Determina si una posicion renglonm columna se encuentra disponible y retorna la posicion mas proxima vacia
	for r in range(NUMRENGLONES):
		if tablero[r][columna] == 0:
			return r

def checarEmpate(tablero):
	#Solo valida si hay empate
	if 0 in tablero:
		return False
	return True

def imprimirTablero(tablero):
	#Imprime el tablero de manera inversa
	print("---*")
	#print(tablero)
	#Flip da la vuelta la matriz de manera "0" que es de forma vertical
	print(np.flip(tablero, 0))

def checarVictoria(tablero, pieza):
	#SI POR ALGUN MOTIVO RETORNA TRUE EL JURGO TERMINA Y MUESTRA AL GANADOR
	# Revisa posiciones horizontales para ver si existe un 4 conectados (Izquierda a derecha)
	for c in range(NUMCOLUMNAS-3):
		for r in range(NUMRENGLONES):
			if tablero[r][c] == pieza and tablero[r][c+1] == pieza and tablero[r][c+2] == pieza and tablero[r][c+3] == pieza:
				return True

	# Revisa posiciones verticales para ver si existe un 4 conect (Abajo hacia Arriba)
	for c in range(NUMCOLUMNAS):
		for r in range(NUMRENGLONES-3):
			if tablero[r][c] == pieza and tablero[r+1][c] == pieza and tablero[r+2][c] == pieza and tablero[r+3][c] == pieza:
				return True

	# Revisa posiciones diagonales (Izquierda a derecha)
	for c in range(NUMCOLUMNAS-3):
		for r in range(NUMRENGLONES-3):
			if tablero[r][c] == pieza and tablero[r+1][c+1] == pieza and tablero[r+2][c+2] == pieza and tablero[r+3][c+3] == pieza:
				return True

	# Revisa posiciones diagonales (Derecha a Izquierda)
	for c in range(NUMCOLUMNAS-3):
		for r in range(3, NUMRENGLONES):
			if tablero[r][c] == pieza and tablero[r-1][c+1] == pieza and tablero[r-2][c+2] == pieza and tablero[r-3][c+3] == pieza:
				return True

def esMoviementoFinal(tablero):
	#Revisa tres instancias
	#1 si esl jugador Humano ganó
	#2 si la IA Gano
	#3 Si ya no existen Movimientos Validos
	return checarVictoria(tablero, PIEZAJUGADOR) or checarVictoria(tablero, PIEZA_IA) or len(getMovimientosValidos(tablero)) == 0

#LLEGAMOS A LA JOYA
def minimax(tablero, profundidad, alpha, beta, maximizando):
	#(matriz, entero, inf, -inf, bool)
	#Getmovimientos validos Alamacena los movimientos restantes disponibles (Casillas vacias)
	movimientosPosibles = getMovimientosValidos(tablero)
	#esmovfinal devuelve true o false determina si existe un ganador
	esFinal = esMoviementoFinal(tablero)
	#Si la profundidad es 0 no hace ninguna accion y salia un hermoso ERROR hasta que adapte un numero random
	if profundidad == 0 or esFinal:
		if esFinal:
			if checarVictoria(tablero, PIEZA_IA):
				return (None, 100000000000000)
			elif checarVictoria(tablero, PIEZAJUGADOR):
				return (None, -10000000000000)
			else: 
				return (None, 0)
		else:
			return (random.randint(0,7), puntPosicion(tablero, PIEZA_IA))
	#SI MAXIMIZANDO TRUE
	if maximizando:
		valor = -math.inf
		#Columna contiene un valor randomico de la lista de posibles movimientps
		columna = random.choice(movimientosPosibles)
		for col in movimientosPosibles:
			#renglon contiene el renglon mas proximo disponible de la columna
			renglon = getRenglonValido(tablero, col)
			copiaTablero = tablero.copy()
			#Se simula el juego en una copia del tablero
			soltarPieza(copiaTablero, renglon, col, PIEZA_IA)
			#Continuamos ahora con el min el elemento extra [1] hace referencia a que solo tomara el valor 2do valor
			#que duevuelve minimax
			nuevaPuntuacion = minimax(copiaTablero, profundidad-1, alpha, beta, False)[1]
			if nuevaPuntuacion > valor:
				valor = nuevaPuntuacion
				columna = col
			alpha = max(alpha, valor)
			if alpha >= beta:
				break
		return columna, valor

	else:
		valor = math.inf
		columna = random.choice(movimientosPosibles)
		for col in movimientosPosibles:
			renglon = getRenglonValido(tablero, col)
			copiaTablero = tablero.copy()
			soltarPieza(copiaTablero, renglon, col, PIEZAJUGADOR)
			nuevaPuntuacion = minimax(copiaTablero, profundidad-1, alpha, beta, True)[1]
			if nuevaPuntuacion < valor:
				valor = nuevaPuntuacion
				columna = col
			beta = min(beta, valor)
			if alpha >= beta:
				break
		return columna, valor


def getMovimientosValidos(tablero):
	#Alamacena los movimientos restantes disponibles (Casillas vacias)
	posicionesValidas = []
	for col in range(NUMCOLUMNAS):
		#return tablero[NUMRENGLONES-1][columna] == 0
		if movimientoValido(tablero, col):
			posicionesValidas.append(col)
	return posicionesValidas

#ESTA FUNCION NO SE UTILIZA AUN, PARECE UNA HEURISTICA
def escogerMejorMovimiento(tablero, pieza):
	#almacena los movimientos posibles en la lista posValidas
	posValidas = getMovimientosValidos(tablero)
	mejorPuntuacion = -10000
	print("Hecho")

	for col in posValidas:
		renglon = getRenglonValido(tablero, col)
		tableroTemporal = tablero.copy()
		soltarPieza(tableroTemporal, renglon, col, pieza)
		score = score_position(tableroTemporal, pieza)

		if score > mejorPuntuacion:
			mejorPuntuacion = score
			mejorColumna = col

	return mejorColumna

def evaluarVentana(window, pieza):
	puntuacion = 0
	#print("H2")
	piezaDeOponente = PIEZAJUGADOR

	if pieza == PIEZAJUGADOR:
		piezaDeOponente = PIEZA_IA
	# Window es la ventana [0,0,0,0] y window.count cuenta cuantas pieza = 1 o 2 se encuentran en la ventana
	if window.count(pieza) == 4:
		puntuacion += 100
	#VACIO ES IGUAL: 0
	elif window.count(pieza) == 3 and window.count(VACIO) == 1:
		puntuacion += 5
	elif window.count(pieza) == 2 and window.count(VACIO) == 2:
		puntuacion += 2
	#DESCRIBE LA POSIBILIDAD DEL OPONENTE
	if window.count(piezaDeOponente) == 3 and window.count(VACIO) == 1:
		puntuacion -= 4

	return puntuacion

def puntPosicion(tablero, turno):
	puntuacion = 0
	#print("H3")
	# puntuacion centro (Puntuacion de movimientos disponibles)
	colCentro = [int(i) for i in list(tablero[:, NUMCOLUMNAS//2])]
	contCentro = colCentro.count(turno)
	puntuacion += contCentro * 3

	# posicion Horizontal
	for r in range(NUMRENGLONES):
		#renglon se almacena una lista [0,0,0,0,0,0] donde se almacenan renglones horizontales
		renglon = [int(i) for i in list(tablero[r,:])]
		#print("----*----")
		#print(renglon)
		#print(tablero[r,:])
		#print(turno)
		#C va de 0 a 4 para determinar las ventanas que son [0,0,0,0]
		for c in range(NUMCOLUMNAS-3):
			ventana = renglon[c:c+TAMVENTANA]
			#print("---*---")
			#print(ventana)
			#Nos vamos a revisar la funcion evaluar ventana
			puntuacion += evaluarVentana(ventana, turno)

	# puntuacion Vertical
	for c in range(NUMCOLUMNAS):
		columna = [int(i) for i in list(tablero[:,c])]
		for r in range(NUMRENGLONES-3):
			ventana = columna[r:r+TAMVENTANA]
			puntuacion += evaluarVentana(ventana, turno)

	# puntuacion diagonales
	for r in range(NUMRENGLONES-3):
		for c in range(NUMCOLUMNAS-3):
			ventana = [tablero[r+i][c+i] for i in range(TAMVENTANA)]
			puntuacion += evaluarVentana(ventana, turno)

	for r in range(NUMRENGLONES-3):
		for c in range(NUMCOLUMNAS-3):
			ventana = [tablero[r+3-i][c+i] for i in range(TAMVENTANA)]
			puntuacion += evaluarVentana(ventana, turno)
	#DEVUELVE LA PUNTUACION DE ESTADO DE POSIBILIDADES QUE TIENE YA SEA LA PC O EL JUGADOR
	#Se podria decir que esto es como la heuristica
	return puntuacion

#PYGAME ES ALGO COMPLEJO NO LO ANALICÉ
def dibujarTablero(tablero):
	for c in range(NUMCOLUMNAS):
		for r in range(NUMRENGLONES):
			pygame.draw.rect(pantalla, AZUL, (c*TAMCUADROS, r*TAMCUADROS+TAMCUADROS, TAMCUADROS, TAMCUADROS))
			pygame.draw.circle(pantalla, NEGRO, (int(c*TAMCUADROS+TAMCUADROS/2), int(r*TAMCUADROS+TAMCUADROS+TAMCUADROS/2)), RADIO)
	
	for c in range(NUMCOLUMNAS):
		for r in range(NUMRENGLONES):		
			if tablero[r][c] == 1:
				pygame.draw.circle(pantalla, ROJO, (int(c*TAMCUADROS+TAMCUADROS/2), largo-int(r*TAMCUADROS+TAMCUADROS/2)), RADIO)
			elif tablero[r][c] == 2: 
				pygame.draw.circle(pantalla, AMARILLO, (int(c*TAMCUADROS+TAMCUADROS/2), largo-int(r*TAMCUADROS+TAMCUADROS/2)), RADIO)
	pygame.display.update()

#SE CREA EL TABLERO
tablero = crearTablero()
#MUESTRA EL TABLERO EN CONSOLA
imprimirTablero(tablero)
#ESTADO DE JUEGO GRAL
juegoTerminado = False
#SIEMPRE SERA PRIMERO EL TURNO DE LA PC
turno = 1
#INICIAMOS EL PYGAME
pygame.init()

TAMCUADROS = 100

ancho = NUMCOLUMNAS * TAMCUADROS
largo = (NUMRENGLONES+1) * TAMCUADROS

#TUPLA CON ANCHO Y LARGO
tam = (ancho, largo)

RADIO = int(TAMCUADROS/2 - 5)

pantalla = pygame.display.set_mode(tam)
dibujarTablero(tablero)
pygame.display.update()

myFuente = pygame.font.SysFont("monospace", 18)

#Aqui se especifica quien empieza
turno = IA
#la profundidad esta relacionada con la dificultad
#teoricamente si el primero turno es la IA 
#y la profunidad es 6 no hay manera de ganarle
PROFUNDIDAD = 0

while not juegoTerminado:
	#INICIA PYGAME Y SUS CONDICIONES DE FINALIZACION
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		#EVENTOS CON EL MOUSE
		if event.type == pygame.MOUSEMOTION:
			pygame.draw.rect(pantalla, NEGRO, (0, 0, ancho, TAMCUADROS))
			posx = event.pos[0]
			if turno == JUGADOR:
				pygame.draw.circle(pantalla, ROJO, (posx, int(TAMCUADROS/2)), RADIO)

		pygame.display.update()
		#MAS EVENTOS CON EL MOUSE AL HACER CLICK
		if event.type == pygame.MOUSEBUTTONDOWN:
			pygame.draw.rect(pantalla, NEGRO, (0,0, ancho, TAMCUADROS))
			if turno == JUGADOR:
				posx = event.pos[0]
				columna = int(math.floor(posx/TAMCUADROS))

				if movimientoValido(tablero, columna):
					renglon = getRenglonValido(tablero, columna)
					soltarPieza(tablero, renglon, columna, PIEZAJUGADOR)

					if checarVictoria(tablero, PIEZAJUGADOR):
						mensaje = myFuente.render("Jugador 1 GANA!", 1, ROJO)
						pantalla.blit(mensaje, (40,10))
						juegoTerminado = True

					turno += 1
					turno = turno % 2

					imprimirTablero(tablero)
					dibujarTablero(tablero)


	#Turno inteligencia artificial
	if turno == IA and not juegoTerminado:
		#Math.inf = Infinito para eso sirve esa wea y NOS VAMOS AL MINIMAX + a b
		columna, puntuacion = minimax(tablero, PROFUNDIDAD, -math.inf, math.inf, True)

		if movimientoValido(tablero, columna):
			renglon = getRenglonValido(tablero, columna)
			soltarPieza(tablero, renglon, columna, PIEZA_IA)

			if checarVictoria(tablero, PIEZA_IA):
				mensaje = myFuente.render("Gano la computadora", 1, AMARILLO)
				pantalla.blit(mensaje, (40,10))
				juegoTerminado = True	


			imprimirTablero(tablero)
			dibujarTablero(tablero)

			turno += 1
			turno = turno % 2

	if checarEmpate(tablero):
		mensaje = myFuente.render("Empate", 1, AZUL)
		pantalla.blit(mensaje, (40,10))
		juegoTerminado = True
			
	if juegoTerminado:
		pygame.time.wait(3000)