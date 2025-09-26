import turtle

""" 
--- Asistencia de IA (Gemini Code Assist) ---
 Este código fue revisado y refactorizado con la asistencia de Gemini.
La IA ayudó a:
 1. Modularizar el código, extrayendo la lógica de dibujar un píxel a su propia función.
 2. Introducir constantes para valores de configuración (tamaño de píxel, nombre de archivo).
3. Añadir "type hints" para mejorar la legibilidad y robustez del código.
El código original fue proporcionado por el autor, y las sugerencias de la IA fueron revisadas e integradas manualmente.
"""

def configurar_pantalla():
   """configuracion del tamaño de ventana y el cambio de titulos y ademas de agregar la ocultacion de la tortuga ,definir su velocidad"""
    screen = turtle.Screen()
    screen.setup(600, 600)
    screen.title("Dibujo de Imagen con Matriz Numérica")
    turtle.hideturtle()  
    turtle.speed(0)     
    turtle.tracer(100, 0) 
"""aqui definimos el uso del def para poder usar el archivo y asi devolver el uso de las instrucciones numericas tambien definimos errores de no encontrar el archivo o no tener las instrucciones correctas."""
def leer_matriz(nombre_archivo):
   
    matriz = []
    try:
        with open(nombre_archivo, 'r') as archivo:
            for linea in archivo:
                fila = [int(num) for num in linea.strip()]
                matriz.append(fila)
        return matriz
    except FileNotFoundError:
        print(f"Error: El archivo '{nombre_archivo}' no se encontró.")
        return None
    except ValueError:
        print("Error: El archivo contiene caracteres no numéricos.")
        return None

def dibujar_imagen(matriz, mapa_colores, tamano_pixel=5):
    """
    Dibuja la imagen pixel a pixel usando la matriz y el mapa de colores.
    
    El origen del dibujo se desplaza para centrar la imagen de 100x100
    en la pantalla.
    """
    if not matriz:
        return

    """Origen del dibujo para centrar la matriz de 100x100"""
    origen_x = - (len(matriz[0]) * tamano_pixel) / 2
    origen_y = + (len(matriz) * tamano_pixel) / 2

    """Itera sobre cada píxel de la matriz"""
    for fila_idx, fila in enumerate(matriz):
        for col_idx, valor in enumerate(fila):
    """Obtiene el color del mapa, por defecto usa 'white' si el número no está"""
            color = mapa_colores.get(valor, 'white')
            
    """Mueve la tortuga sin dibujar esto nos ayudar a darle control ala ubicacion donde se pintara"""
            turtle.penup()
            x = origen_x + (col_idx * tamano_pixel)
            y = origen_y - (fila_idx * tamano_pixel)
            turtle.goto(x, y)
            
    """ la tortuga se detiene en la ubicacion para poder pintar y realizar las instrucciones numericas y pintarlo """
            turtle.pendown()
            turtle.fillcolor(color)
            turtle.begin_fill()
            for _ in range(4):
                turtle.forward(tamano_pixel)
                turtle.right(90)
            turtle.end_fill()
    """una vez realizado se realizar el levantamiento de la tortuga para finalizar el rango de la instrucciones que haya en el archivo txt"""        
    turtle.penup()
    turtle.goto(0, 0)
    turtle.update()
    
    print("Dibujo completado. Haz clic en la ventana para cerrarla.")
    turtle.exitonclick()

def main():
    """Función principal del script.
    Define la asignación de números a colores
    Puedes expandir este diccionario para más colores """
    mapa_colores = {
        0: "white",   # Fondo
        1: "blue",
        2: "red",
        3: "green",
        4: "purple",
        5: "orange",
        6: "cyan",
        7: "magenta",
        8: "yellow",
        9: "gray"
    }

    """ declaramos la Ruta del archivo de la matriz """
    nombre_archivo = "matriz_colores.txt"
    
    """Leer el archivo y obtener la matriz""" 
    matriz_numerica = leer_matriz(nombre_archivo)
""" este if nos permite la interraccion de los bloques de codigos principales para realizar correctamente el objetivo de pintar con las instrucciones"""
    if matriz_numerica:
        configurar_pantalla()
        dibujar_imagen(matriz_numerica, mapa_colores)
"""nos aseguramos que haga su funcion en el archivo principal main y evitar conflictos de archivos """
if __name__ == "__main__":
    main()

