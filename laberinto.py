from turtle import TurtleScreen, RawTurtle, TK
from time import sleep
 
class Ventana():
    
 
    def __init__(self, titulo, alto, ancho):
        
        assert isinstance(titulo, str)
        assert isinstance(alto, int) and alto > 0
        assert isinstance(ancho, int) and ancho > 0
 
        ## Crea la ventana y un canvas para dibujar
        self.root = TK.Tk()
        self.root.title(titulo)
        self.canvas = TK.Canvas(self.root, width=ancho, height=alto)
        self.canvas.pack()
         
        ## Crea un TurtleScreen y la tortuga para dibujar
        self.fondo_ventana = TurtleScreen(self.canvas)
        self.fondo_ventana.setworldcoordinates(0, alto, ancho, 0)
 
        ## Establece el color de fondo
        self.canvas["bg"] = "blue"
        self.canvas.pack()
 
        ## Crea una tortuga para dibujar
        self.pencil = RawTurtle(self.fondo_ventana)
        self.pencil.pencolor("white")

class Laberinto():    
    
    Xdis = 10
    Ydis = 10

    Alto = 25
    Ancho= 25
 
    @staticmethod
    def deme_posicion(i, j):        
        x = Laberinto.Xdis + j * (Laberinto.Ancho + 1)
        y = Laberinto.Ydis + i * (Laberinto.Alto  + 1)
        return (x, y)
 
             
    def __init__(self, area_dibujo, laberinto):
                
        lista = laberinto.split()
        lista = [ x[:-1] if x[-1] == "\n" else x for x in lista]
        lista = [[int(ch) for ch in x] for x in lista] 
 
        self.laberinto = lista
        self.lienzo = area_dibujo

        self.dibuja_laberinto()
 
    def dibuja_laberinto(self):
        
        self.lienzo.fondo_ventana.tracer(False)
        self.lienzo.pencil.pencolor("white")
 
        for i in range(len(self.laberinto)):
 
            for j in range(len(self.laberinto[i])):
 
                if self.laberinto[i][j] == 1:
                    self.casilla("black", i, j)
                elif self.laberinto[i][j] == 3:
                    self.casilla("red", i, j)
                elif self.laberinto[i][j] == 0:
                    self.casilla("white", i, j)
 
        self.lienzo.fondo_ventana.tracer(True)
 
    def casilla(self, color, i, j):
        
        x, y = Laberinto.deme_posicion(i, j) 
        
        self.lienzo.pencil.fillcolor(color)
        self.lienzo.pencil.pu()
        self.lienzo.pencil.setpos(x, y)
        self.lienzo.pencil.seth(0)
        self.lienzo.pencil.pd()
        self.lienzo.pencil.begin_fill() 

        for i in range(2):
            self.lienzo.pencil.fd(Laberinto.Ancho+1)
            self.lienzo.pencil.left(90)
            self.lienzo.pencil.fd(Laberinto.Alto+1)
            self.lienzo.pencil.left(90)

        self.lienzo.pencil.end_fill()
 
    def recorrido(self, i, j):       
 
        if self.laberinto[i][j] == 3:
            return [(i, j)]
 
        if self.laberinto[i][j] == 1:
            return []
 
        self.laberinto[i][j] = -1
 
        sleep(0.10)
        self.lienzo.fondo_ventana.tracer(False)
        self.casilla("green", i, j)
        self.lienzo.fondo_ventana.tracer(True)
 
        if i > 0 and self.laberinto[i - 1][j] in [0, 3]:     # Norte
            camino = self.recorrido(i - 1, j)
            if camino: return [(i, j)] + camino
 
        if j < len(self.laberinto[i]) - 1 and \
           self.laberinto[i][j + 1] in [0, 3]:               # Este
            camino = self.recorrido(i, j + 1)
            if camino: return [(i, j)] + camino
 
        if i < len(self.laberinto) - 1 and \
           self.laberinto[i + 1][j] in [0, 3]:               # Sur
            camino = self.recorrido(i + 1, j)
            if camino: return [(i, j)] + camino
 
        if j > 0 and self.laberinto[i][j - 1] in [0, 3]:     # Oeste
            camino = self.recorrido(i, j - 1) 
            if camino: return [(i, j)] + camino
 
        sleep(0.10)
        self.lienzo.fondo_ventana.tracer(False)
        self.casilla("white", i, j)
        self.lienzo.fondo_ventana.tracer(True)
 
        return []
 
    def reset(self):
 
        for i in range(len(self.laberinto)):
            for j in range(len(self.laberinto[i])):
                if self.laberinto[i][j] == -1:
                    self.laberinto[i][j] = 0

stringLab = "10111111111111\n" + \
            "10000000010003\n" + \
            "10111111010111\n" + \
            "10100001010001\n" + \
            "10111101111001\n" + \
            "10000001010001\n" + \
            "10111111010111\n" + \
            "10000000010001\n" + \
            "11110111111101\n" + \
            "10000000000001\n" + \
            "11111111111101\n" + \
            "10000000000001\n" + \
            "11111111111111" 
 
def principal():
    ll = Laberinto(Ventana("Laberinto", 380, 380), stringLab)
    ll.recorrido(0,1) ##Inicio
    ll.reset()
 
if __name__ == "__main__":
    principal()