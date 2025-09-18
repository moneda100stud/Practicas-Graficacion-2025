import turtle
"""aqui configuramos la pantalla y el fondo de la misma"""
screen = turtle.Screen()
screen.title("Práctica 2: Movimiento con Teclado")
screen.bgcolor("lightblue")
screen.setup(width=600, height=600)
screen.tracer(0)
"""aqui configuramos la figura que se movera con el teclado y su color """
figura = turtle.Turtle()
figura.speed(0)
figura.shape("square")
figura.color("darkred")
figura.penup()
figura.goto(0, 0)
""" designacion del teclado a la figura y su movimiento y limitador de borde """
def mover_arriba():
    # El borde superior es y=300. La figura es 20x20, así que su centro no debe pasar de 290.
    if figura.ycor() < 290:
        y = figura.ycor()
        figura.sety(y + 20)

def mover_abajo():
    # El borde inferior es y=-300. Su centro no debe pasar de -290.
    if figura.ycor() > -290:
        y = figura.ycor()
        figura.sety(y - 20)

def mover_izquierda():
    # El borde izquierdo es x=-300. Su centro no debe pasar de -290.
    if figura.xcor() > -290:
        x = figura.xcor()
        figura.setx(x - 20)

def mover_derecha():
    # El borde derecho es x=300. Su centro no debe pasar de 290.
    if figura.xcor() < 290:
        x = figura.xcor()
        figura.setx(x + 20)
"""la seccion de la accion de las teclas y asigancion de teclas a la figura"""
screen.listen()
screen.onkeypress(mover_arriba, "Up")
screen.onkeypress(mover_abajo, "Down")
screen.onkeypress(mover_izquierda, "Left")
screen.onkeypress(mover_derecha, "Right")
"""manetener actualizado la pantalla hasta que se cierre"""
while True:
    screen.update()

