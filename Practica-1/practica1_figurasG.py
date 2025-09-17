"""
Práctica 1: Dibujo de Figuras Geométricas con Turtle.

Este script dibuja una línea, un cuadrado, un triángulo y un círculo
utilizando la librería turtle de Python.
"""
import turtle as t

def teleport(x: float, y: float) -> None:
    """Mueve la tortuga a una coordenada específica sin dibujar."""
    t.penup()
    t.goto(x, y)
    t.pendown()

def draw_line(color: str, length: float):
    """Dibuja una línea recta con un color y longitud determinados."""
    t.pencolor(color)
    t.forward(length)

def draw_square(color: str, length: float):
    """Dibuja un cuadrado con un color y longitud de lado determinados."""
    t.pencolor(color)
    for _ in range(4):
        t.forward(length)
        t.right(90)

def draw_triangle(color: str, length: float):
    """Dibuja un triángulo equilátero con un color y longitud de lado determinados."""
    t.pencolor(color)
    for _ in range(3):
        t.forward(length)
        t.right(120)

def draw_circle(color: str, radius: float):
    """Dibuja un círculo con un color y radio determinados."""
    t.pencolor(color)
    t.circle(radius)

def main():
    """Función principal que dibuja todas las figuras."""
    

    # Dibuja un cuadrado azul en (0, 0)
    teleport(0, 0)
    draw_square("blue", 100)

    # Dibuja una línea roja
    teleport(-150, 50)
    draw_line("red", 100)

    # Dibuja un triángulo verde
    teleport(150, 150)
    draw_triangle("green", 100)

    # Dibuja un círculo amarillo
    teleport(0, -150)
    draw_circle("yellow", 50)

    t.hideturtle()  # Oculta la tortuga al finalizar
    t.done()  # Mantiene la ventana abierta

if __name__ == "__main__":
    main()
