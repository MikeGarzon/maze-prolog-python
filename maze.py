from pyswip import Prolog
from laberinto import principal

def leerArchivo(archivo):
	c = [line.splitlines() for line in (open(archivo, "r"))]
	c = [i[0].split() for i in c]
	return c

def inicio(mapa,cont):
	if mapa == []: return (-1,-1)
	if "i" in mapa[0]: return ([cont,mapa[0].index("i")])
	return inicio(mapa[1:],cont+1)

def buscar(x, y, maze):
  if maze[x][y] == 'f':
      camino.append(['f'])
      return True
  elif maze[x][y] == '|':  return False
  elif maze[x][y] == '-':  return False
  elif maze[x][y] == '--': return False
  elif maze[x][y] == 'o':  return False
  else: camino.append([maze[x][y]])
  maze[x][y] = 'o'

  if ((x < len(maze)-1 and buscar(x+1, y,maze)) or
  	(y > 0 and buscar(x, y-1,maze)) or
  	(x > 0 and buscar(x-1, y,maze)) or
  	(y < len(maze[0])-1 and buscar(x, y+1,maze))):
    return True
  return False

def encontrar(lista, maze):
  if(buscar(lista[0], lista[1], maze)): return True
  return False

def ass(camino):
  for x in range(0 , len(camino) - 1):
    p.assertz("conecta("+camino[x][0]+","+camino[x+1][0]+")")

def solu(camino):
  s = []
  aux =[]

  for x in range(0 , len(camino)):
    for j in range(0 , len(camino[x]) ):
      if (camino[x][j] == 'o' or camino[x][j] == 'f'):

        aux = [str(x),str(j)]
        s.append(aux)

  return s

def solucion():
	solucion = []
	for r in p.query("camino([i],Sol)"):
		for j in r["Sol"]:
			solucion += [j]
		break
	solucion[-1] = 'i'
	solucion[0] = 'f'
	return solucion

#-------------------------"MAIN"----------------------------------

p = Prolog()
p.consult('laberinto.pl')

maze = leerArchivo("maze.txt")  #CON ESTE CREE EL MAPA

#----------------------------------------------------------------

dibujo = ''                     #PARA DIBUJAR EL MAPA

for i in range(len(maze)):
    for j in range(len(maze[i])):
        if (maze[i][j] == '|' or maze[i][j] ==  '--') : dibujo += '1'
        elif maze[i][j] == 'f': dibujo+= '3'
        else : dibujo += '0'
    dibujo += '\n'

#----------------------------------------------------------------

camino = []
encontrar(inicio(maze,0),maze)    #CONECTA LOS CAMINOS

#----------------------------------------------------------------

while (['0'] in camino): camino.remove(['0']) #AQUI QUITO EL 0 DE LAS HORIZONTALES

ass(list(camino))               #ASSERTZ's

sol = solucion()[::-1]   #Guardo lo que manda prolog

print(sol)

#----------------------------------------------------------------

principal(dibujo,solu(list(maze)))  #Dibuja el camino

