"""importamos la libreria turtle"""
from tracemalloc import start
import turtle as t 

"""aqui realizamos una linea recta de 100 pixeles sencillo """
#t.forward(100)
#t.right(90)
"""para hacer un recta con color tenemos que aplicar un def draw_line """
#def draw_line(color,length,start_x,start_y):
"""hacemos de pen un objeto para poder evitar conflictos de modulos como t turtle"""
    #pen = t.Turtle()
    #pen.penup()
    #pen.goto(start_x, start_y)
    #pen.pendown()
    #pen.pencolor(color)
    #pen.forward(length)
#if __name__=="__main__":
    #draw_line("red",100,0,0)
#t.done() 
"""este bloque realizaremos un cuadrado con turtle creamos un def draw_square"""""
def draw_square(color,length,start_x,start_y):
    pen=t.Turtle()
    pen.penup()
    pen.goto(start_x,start_y)
    pen.pendown()
    pen.pencolor(color)
    """aqui realizamos un for para repetir la direccion de la linea y asi realizar el cuadrado"""
    for i in range(4):
        pen.forward(length)
        pen.right(90)
"""aqui invocamos el documento principal para que asegure el correr el codigo """
if __name__=="__main__":
    draw_square("blue",100,0,0)
t.done()
