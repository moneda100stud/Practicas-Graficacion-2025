# Practicas-Graficacion-2025
repositorio de Luis Alfonso santacruz-5ss Practica-1
  Guía de Práctica con Turtle 

# Práctica-1: Dibujo de Figuras Geometricas con Turtle 
## Descripción de la Práctica

El objetivo principal de esta práctica es familiarizarse con la librería \`turtle\` y su uso para la creación de gráficos básicos. Se requiere la implementación de funciones que dibujen un cuadrado, un triángulo, un círculo y una línea recta. Cada función debe ser personalizable en cuanto a su color y la posición de inicio del dibujo.
## Contenido del Repositorio
*   \`practica1\_figurasG.py\`: El script principal que contiene todo el código fuente.
*   \`README.md\`: Este archivo, que explica el propósito y la estructura de la práctica.
## Funcionalidades Implementadas
El script \`practica1\_figurasG.py\` incluye cuatro funciones principales, cada una con parámetros específicos para controlar el dibujo:

*   \`draw\_square(color, side\_length, start\_x, start\_y)\`: Dibuja un cuadrado.
*   \`draw\_triangle(color, side\_length, start\_x, start\_y)\`: Dibuja un triángulo.
*   \`draw\_circle(color, radius, start\_x, start\_y)\`: Dibuja un círculo.
*   \`draw\_line(color, length, start\_x, start\_y)\`: Dibuja una línea recta.

Cada función utiliza comandos básicos de la librería \`turtle\` como \`forward()\`, \`right()\`, \`pencolor()\`, \`penup()\` y \`pendown()\` para controlar el movimiento y las propiedades del "lápiz".

## Comandos de Turtle más Comunes

A continuación se listan algunos de los métodos más utilizados de la librería \`turtle\`, que te servirán para esta y futuras prácticas.

| Método | Parámetros | Descripción |
| --- | --- | --- |
| \`forward()\` | \`distancia\` | Mueve la tortuga hacia adelante la distancia especificada. |
| \`backward()\` | \`distancia\` | Mueve la tortuga hacia atrás la distancia especificada. |
| \`right()\` | \`ángulo\` | Gira la tortuga a la derecha el ángulo indicado (en grados). |
| \`left()\` | \`ángulo\` | Gira la tortuga a la izquierda el ángulo indicado (en grados). |
| \`penup()\` | (ninguno) | Levanta el "lápiz" para que la tortuga se mueva sin dibujar. |
| \`pendown()\` | (ninguno) | Baja el "lápiz" para que la tortuga empiece a dibujar de nuevo. |
| \`goto()\` | \`x\`, \`y\` | Mueve la tortuga a las coordenadas absolutas \`(x, y)\`. |
| \`pencolor()\` | \`color\_nombre\` | Cambia el color de la línea de dibujo. |
| \`pensize()\` | \`grosor\` | Cambia el grosor de la línea. |
| \`speed()\` | \`velocidad\` | Establece la velocidad de la animación (0-10, 0 es la más rápida). |
| \`hideturtle()\` | (ninguno) | Oculta el cursor de la tortuga para que no se vea el resultado final. |
| \`done()\` | (ninguno) | Mantiene la ventana de dibujo abierta hasta que se cierre manualmente. |

## Cómo Ejecutar el Código

Para ejecutar el script, sigue estos sencillos pasos:

1.  Asegúrate de tener Python instalado en tu sistema.
2.  Navega a la carpeta donde guardaste el archivo \`practica1\_figurasG.py\` usando la terminal.
3.  Ejecuta el archivo con el siguiente comando:

python practica1\_figurasG.py

Al ejecutar el script, se abrirá una nueva ventana donde \`turtle\` dibujará las figuras geométricas definidas en las funciones.
