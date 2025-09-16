"""importamos la libreria turtle"""
import turtle as t 

"""aqui realizamos una linea recta de 100 pixeles sencillo """
#t.forward(100)
#t.right(90)
"""para hacer un recta con color tenemos que aplicar un def draw_line """
def draw_line(color,length,start_x,start_y):
    """hacemos de pen un objeto para poder evitar conflictos de modulos como t turtle"""
    pen=t.Turtle()
    pen.penup()
    pen.goto(start_x,start_y)
    pen.pendown()
    pen.pencolor(color)
    pen.forward(length)
if __name__=="__main__":
    draw_line("red",100,0,0)
t.done() 
