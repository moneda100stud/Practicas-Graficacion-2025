import turtle

# --- Configuración de la pantalla ---
wn = turtle.Screen()
wn.title("Dibujante de Turtle")
wn.bgcolor("lightgray")
t = turtle.Turtle()
t.speed(5) # Establecer la velocidad de la tortuga

# --- Definición de funciones de dibujo ---

def dibujar_cuadrado(x_inicial, y_inicial, lado, color):
    """Dibuja un cuadrado con el lado especificado, a partir de las coordenadas iniciales y con el color dado."""
    t.penup()
    t.goto(x_inicial, y_inicial)
    t.pendown()
    t.pencolor(color)
    print(f"Dibujando un cuadrado de lado {lado} en ({x_inicial}, {y_inicial}) de color {color}")
    for _ in range(4):
        t.forward(lado)
        t.right(90)

def dibujar_triangulo(x_inicial, y_inicial, lado, color):
    """Dibuja un triángulo equilátero con el lado especificado, a partir de las coordenadas iniciales y con el color dado."""
    t.penup()
    t.goto(x_inicial, y_inicial)
    t.pendown()
    t.pencolor(color)
    print(f"Dibujando un triángulo de lado {lado} en ({x_inicial}, {y_inicial}) de color {color}")
    for _ in range(3):
        t.forward(lado)
        t.left(120)

def dibujar_circulo(x_inicial, y_inicial, radio, color):
    """Dibuja un círculo con el radio especificado, a partir de las coordenadas iniciales y con el color dado."""
    t.penup()
    t.goto(x_inicial, y_inicial - radio) # La tortuga comienza a dibujar desde abajo
    t.pendown()
    t.pencolor(color)
    print(f"Dibujando un círculo de radio {radio} en ({x_inicial}, {y_inicial}) de color {color}")
    t.circle(radio)

def dibujar_linea(x_inicial, y_inicial, x_final, y_final, color):
    """Dibuja una línea recta desde las coordenadas iniciales a las finales y con el color dado."""
    t.penup()
    t.goto(x_inicial, y_inicial)
    t.pendown()
    t.pencolor(color)
    print(f"Dibujando una línea desde ({x_inicial}, {y_inicial}) a ({x_final}, {y_final}) de color {color}")
    t.goto(x_final, y_final)

# --- Procesar el archivo de instrucciones ---
def ejecutar_instrucciones(nombre_archivo):
    """Lee y ejecuta las instrucciones de un archivo de texto."""
    try:
        with open(nombre_archivo, 'r') as archivo:
            for i, linea in enumerate(archivo):
                # Limpiar la línea y dividirla en partes
                linea = linea.strip().lower()
                partes = linea.split()
                
                if not partes:
                    continue # Saltar líneas vacías
                
                comando = partes[0]
                argumentos = partes[1:]
                print(f"Instrucción {i+1}: '{linea}'")

                try:
                    if comando == 'cuadrado':
                        if len(argumentos) == 4:
                            x_inicial, y_inicial, lado, color = float(argumentos[0]), float(argumentos[1]), float(argumentos[2]), argumentos[3]
                            dibujar_cuadrado(x_inicial, y_inicial, lado, color)
                        else:
                            print(f"Advertencia: 'cuadrado' requiere 4 argumentos (x, y, lado, color), se recibieron {len(argumentos)}.")
                    elif comando == 'triangulo':
                        if len(argumentos) == 4:
                            x_inicial, y_inicial, lado, color = float(argumentos[0]), float(argumentos[1]), float(argumentos[2]), argumentos[3]
                            dibujar_triangulo(x_inicial, y_inicial, lado, color)
                        else:
                            print(f"Advertencia: 'triangulo' requiere 4 argumentos (x, y, lado, color), se recibieron {len(argumentos)}.")
                    elif comando == 'circulo':
                        if len(argumentos) == 4:
                            x_inicial, y_inicial, radio, color = float(argumentos[0]), float(argumentos[1]), float(argumentos[2]), argumentos[3]
                            dibujar_circulo(x_inicial, y_inicial, radio, color)
                        else:
                            print(f"Advertencia: 'circulo' requiere 4 argumentos (x, y, radio, color), se recibieron {len(argumentos)}.")
                    elif comando == 'linea':
                        if len(argumentos) == 5:
                            x_inicial, y_inicial, x_final, y_final, color = float(argumentos[0]), float(argumentos[1]), float(argumentos[2]), float(argumentos[3]), argumentos[4]
                            dibujar_linea(x_inicial, y_inicial, x_final, y_final, color)
                        else:
                            print(f"Advertencia: 'linea' requiere 5 argumentos (x1, y1, x2, y2, color), se recibieron {len(argumentos)}.")
                    else:
                        print(f"Advertencia: Comando desconocido '{comando}'.")
                except ValueError:
                    print("Advertencia: Argumentos no válidos. Asegúrate de que los valores numéricos sean correctos.")
                finally:
                    print("-" * 20)
    except FileNotFoundError:
        print(f"Error: El archivo '{nombre_archivo}' no fue encontrado. Por favor, asegúrate de que exista.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

# --- Ejecución principal del programa ---
if __name__ == "__main__":
    ejecutar_instrucciones("dibujante.txt")
    
    # Mantener la ventana abierta hasta que se haga clic
    turtle.exitonclick()
