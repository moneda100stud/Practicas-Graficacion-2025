 

# Práctica 2: Control de Figura con Teclado 🕹️

Este es el código de la  segunda práctica. Es un script de Python que usa la librería `turtle` para hacer un juego simple donde puedes mover una figura con el teclado. El chiste es no salirse de la pantalla.

## Las Partes Principales

*   La Ventana: Configuramos una ventana de 600x600 con un fondo azul claro y un título para que se vea mas cool.
*   La Figura: Creamos un cuadrado rojo oscuro que es el que vamos a mover.
*   Movimiento con Teclado: El programa está configurado para que la figura se mueva con las flechas del teclado (`Arriba`, `Abajo`, `Izquierda`, `Derecha`).
*   Limite de Bordes: Hay codigo que evita que la figura se escape de la pantalla.
*   Animación: El codigo se actualiza todo el tiempo para que el movimiento se vea super fluido y no se quede pasmado.

- - -

## Lo Nuevo: Diferencias con la Practica 1

Esta práctica es mas avanzada porque le metimos interactividad y animación. Checa los bloques de codigo nuevos que no estaban en el primer proyecto:

### 1\. Configuración de la Ventana

Este bloque es el que prepara todo el espacio de trabajo.

*   `screen = turtle.Screen()`: Crea el lienzo o "mundo" para dibujar.
*   `screen.setup()`: Define las medidas de la ventana.
*   `screen.tracer(0)`: Este es clave. Desactiva la animacion por defecto de \`turtle\` para que la figura se mueva al instante.

### 2\. Detección de Teclas

Esto es lo que hace que el programa reaccione a lo que tu haces.

*   `screen.listen()`: Le dice a la ventana que "escuche" las teclas que presionas.
*   `screen.onkeypress()`: Esta funcion es la magia. Asigna una funcion de movimiento (como `mover_arriba`) a una tecla especifica. Asi, cuando la presionas, la figura se mueve.

### 3\. Bucle de Animación

Este codigo hace que el juego funcione sin parar.

*   `while True:`: Es un bucle infinito para que el programa no se cierre y este listo para responder a cada tecla que presiones.
*   `screen.update()`: Actualiza la pantalla en cada vuelta del bucle para mostrar la nueva posicion de la figura, asi se ve todo suave.

- - -

## Funciones para Mover

El script tiene cuatro funciones para mover la figura:

*   `mover_arriba()`: La mueve 20 pixeles para arriba, pero revisa que no se salga del borde.
*   `mover_abajo()`: La mueve 20 pixeles para abajo, con el mismo limite.
*   `mover_izquierda()`: La mueve 20 pixeles a la izquierda, revisando el borde.
*   `mover_derecha()`: La mueve 20 pixeles a la derecha, tambien con limite.

- - -

## Como Correr el Codigo

Esta facil, solo haz esto:

1.  Asegurate de que tengas Python instalado.
2.  Abre la terminal en la carpeta donde esta el archivo.
3.  Escribe el siguiente comando y dale `Enter`:

```
python tu_archivo.py
```

Y listo, se abrira la ventana y podras mover el cuadrado con las flechas. El juego termina cuando cierras la ventana.
