"""importamos la libreria turtle"""
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
#def draw_square(color,length,start_x,start_y):
    #pen=t.Turtle()
    #pen.penup()
    #pen.goto(start_x,start_y)
    #pen.pendown()
    #pen.pencolor(color)
"""aqui realizamos un for para repetir la direccion de la linea y asi realizar el cuadrado"""
    #for i in range(4):
     #   pen.forward(length)
      #  pen.right(90)
"""aqui invocamos el documento principal para que asegure el correr el codigo """
#if __name__=="__main__":
#    draw_square("blue",100,0,0)
#t.done()
"""realizaremos el bloque de la figura del triangulo con turtle"""""
"""en esta parte se creo el def para hacer mencion de la figura del triangulo"""
#def draw_triangle(color,length,start_x,start_y):
   # pen=t.Turtle()
    #pen.penup()
    #pen.goto(start_x,start_y)
    #pen.pendown()
    #pen.pencolor(color)
"""en esta seccion del bloque se realizar un for para repetir el la recta hasta dar con el angulo de 120 grados y asi realizar el triangulo """
    #for i in range(3):
        #pen.forward(length)
        #pen.right(120)
"""mencionamos el codigo principal main para realizar correctamente el codigo y asi evitar conflictos de modulos tambien cambiamos los color a verde para marcar la diferencia de figuras"""
#if __name__=="__main__":
    #draw_triangle("green",100,0,0)
#t.done() # t.done nos sirve crucialmente para mantener la ventana del tkinter abierto y correr el codigo correctamente
"""por ultimo crear la figurar circulo procediendo a realizar un def_circle"""
def draw_circle(color,radius,start_x,start_y):
    """realizamos el mismo procedimiento como las anteriores figuras """
    pen=t.Turtle() #aqui declaramos el objeto a llamar pen 
    pen.penup() #se levantar el lapiz del turtle 
    pen.goto(start_x,start_y) # el uso de las coordenas x, y,
    pen.pendown() # se bajar el lapiz del turtle 
    pen.pencolor(color) # realizar el color destinado o mencionado en los parametros 
    pen.circle(radius) # se utilizar el codigo del radios haciendo un llamado a que haga referencia al radio de un circulo 
"""se agregar el uso del if para mencionar el archivo main py y llenar los parametros del circulo y el color elegido """
if __name__=="__main__":
    draw_circle("yellow",100,0,-70)
t.done()
