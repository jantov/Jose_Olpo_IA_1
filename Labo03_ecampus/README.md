<h2>Laboratorio 03 IA 1</h2>
<h4>
Implemente un algoritmo genético para resolver el problema del tablero de interruptores que generan un numero clave de acceso. Se cuenta con un tablero con 32 interruptores binarios, que cada uno de ellos puede estar en encendido o apagado y cada 8 se considera que es una letra o caracter ascii, dada una clave determinada que se introducirá por teclado, el algoritmo genético deberá encontrar la combinación respectiva de interruptores que le permita generar la clave introducida. </h4>
<p>Para el desarrollo del algoritmo se tuvo que realizar funciones de conversion de ascii a binario y de binario a ascii mediante subfunciones para convertir
de binario a decimal y viceversa</p>
<p>A un principio se manejaba elementos de 8 bits para comparar entre el objetivo y el individuo pero fue poco eficiente asi que se opto por una simple comparacion de bits</p>
<p>En cuanto al metodo de cruce se hizo una variante donde seleccionados y poblacion restante se alternaban en generar hijos pero resulto ser poco eficiente tambien asi
que se opto por un cruce de la poblacion restante solamente</p>
<p>Al final utilizando el debido fitness y cruce se logro dar con el objetivo en la mayoria de la pruebas realizada antes de la presentacion</p>
