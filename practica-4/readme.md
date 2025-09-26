# Práctica 4: Dibujante de Turtle con Archivo de Instrucciones

Este proyecto consiste en un programa en Python que utiliza el módulo `turtle` para crear dibujos en una ventana gráfica. La particularidad de este programa es que no tiene las instrucciones de dibujo directamente en el código, sino que las lee desde un archivo de texto externo (`dibujante.txt`). Esto permite generar diferentes gráficos simplemente modificando el archivo de instrucciones, sin necesidad de alterar el código fuente de Python.

## Descripción del Funcionamiento

El script `practica4_archivo_instruccionesG.py` realiza las siguientes acciones:

1.  **Configura la ventana de Turtle:** Prepara un lienzo de color gris claro para dibujar.
2.  **Define funciones de dibujo:** Contiene funciones para dibujar figuras geométricas básicas como cuadrados, triángulos, círculos y líneas.
3.  **Lee y procesa un archivo de instrucciones:** La función `ejecutar_instrucciones` abre un archivo llamado `dibujante.txt`, lee cada línea y la interpreta como un comando de dibujo.
4.  **Maneja errores:** El programa es capaz de gestionar errores como la ausencia del archivo de instrucciones, comandos desconocidos, número incorrecto de argumentos o valores no válidos.
5.  **Ejecuta los comandos:** Por cada línea válida en el archivo, invoca a la función de dibujo correspondiente con los parámetros especificados (coordenadas, tamaño, color).

## Dependencias

Este programa utiliza el módulo `turtle`, el cual es parte de la **biblioteca estándar de Python**. Por lo tanto, **no se requiere la instalación de ninguna dependencia externa**. Solo necesitas tener una instalación de Python en tu sistema.

## Instrucciones de Ejecución

Para ejecutar el programa, sigue estos pasos:

1.  **Crea el archivo de instrucciones:**
    En el mismo directorio donde se encuentra el script `practica4_archivo_instruccionesG.py`, crea un archivo de texto llamado `dibujante.txt`.

2.  **Añade comandos al archivo:**
    Escribe en `dibujante.txt` los comandos de dibujo que desees, uno por línea. El formato de los comandos es el siguiente:

    *   **Cuadrado:** `cuadrado x_inicial y_inicial lado color`
    *   **Triángulo:** `triangulo x_inicial y_inicial lado color`
    *   **Círculo:** `circulo x_inicial y_inicial radio color`
    *   **Línea:** `linea x_inicial y_inicial x_final y_final color`

    > **Nota:** Los colores pueden ser nombres en inglés (ej. `red`, `blue`, `green`) o códigos hexadecimales (ej. `#FF5733`).

    **Ejemplo de contenido para `dibujante.txt`:**

    ```
    # Esto es un comentario y será ignorado
    
    # Dibujar una casa simple
    cuadrado -50 -100 100 brown
    triangulo -50 0 100 red
    
    # Dibujar un sol
    circulo 150 100 30 yellow
    
    # Dibujar una línea para el suelo
    linea -200 -100 200 -100 green
    ```

3.  **Ejecuta el script de Python:**
    Abre una terminal o línea de comandos, navega hasta el directorio del proyecto y ejecuta el siguiente comando:

    ```bash
    python practica4_archivo_instruccionesG.py
    ```

4.  **Visualiza el resultado:**
    Se abrirá una ventana mostrando el dibujo generado por la tortuga. La ventana permanecerá abierta hasta que hagas clic sobre ella.

## Uso de Inteligencia Artificial (IA)

Para la elaboración de este archivo `README.md`, se utilizó el asistente de codificación **Gemini Code Assist**.

*   **¿Qué se generó?**
    Se solicitó la creación completa de este archivo `README.md`.

*   **¿Cómo se adaptó?**
    El prompt o instrucción proporcionada al asistente fue:

    > "realizar un readme.md en un nuevo archivo que explique el funcionamiento y tenga estos puntos abarcados: Si se usó IA, está claramente documentado en el código (comentarios) y en el README (qué se generó y cómo se adaptó). README completo: explicación de la práctica, instrucciones de ejecución, dependencias y notas sobre uso de IA (si aplica)."

    El asistente analizó el código Python proporcionado (`practica4_archivo_instruccionesG.py`) para entender su funcionamiento y generó este documento en formato Markdown. El resultado fue revisado para asegurar que la explicación, las instrucciones y los ejemplos fueran claros y precisos, sin necesidad de realizar adaptaciones significativas.

---
