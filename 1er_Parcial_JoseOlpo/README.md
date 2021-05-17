<h1> PRIMER PARCIAL IA 1</h1>

<h4>1. Elaborar un agente que resuelva un rompecabezas de 3X5 (utilice un algoritmo que permita resolverlo en menos de 1 minuto).</h3>
<p>A* A estrella:
        La heuristica es por importancia de lineas mas una heuristica manhattan, aunque el algoritmo puede resolver ejemplos simples no puede resolver ejercicios complejos</p>
<h4>2. Modificar el juego 3 en raya, para que se aplique la misma lógica, pero en un tablero de 4x4 (gana el primero que logra enlazar 3 marcas similares, horizontales, verticales o diagonales).</h3>
<p>Minimax con poda alfa beta</p>
<p>El algoritmo usa un sistema de puntuacion de triadas para determinar la importancia de la posicion en el vector + un nivel de profundidad desde 0 hasta 6 a
a partir de 7 el tiempo de espera es muy largo entre cada jugada, las reglas del 3 en raya siguen siendo las misma en un espacio de 4 x 4</p>

<h4>Elabore un algoritmo genético que encuentre la mejor manera de colocar 12 bloques de color blanco y 12 bloques de color negro, ubicados para conformar un tablero de ajedrez:</h3>
<p>Algoritmo Genetico</p>
<p>La forma mas sencilla de realizar el fitnes fue por simple comparacion, aunque se puede verificar si a izq o derecha tenemos un valor diferente de 0 o 1, la mejor y mas facil manera de obtener un fitness es mediante la comparacion de un objetivo contra la poblacion generada</p>
<p>Solo se uso una clase donde se encuntra mayoria de funciones para poder realizar el alg genetico, ademas de agregar un forma grafica de comprobar con pygame</p>
<p>De igual manera se agrego un fitness extra con las especificaciones hechas en foro</p>
