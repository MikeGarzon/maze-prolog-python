from pyswip import Prolog

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

def solucion():
	solucion = []
	for r in p.query("camino([i],Sol)"):
		for j in r["Sol"]:
			solucion += [j]
		break
	solucion[-1] = 'i'
	solucion[0] = 'f'
	return solucion

#----------------------------------------------------------------

p = Prolog()
p.consult('laberinto.pl')

maze = leerArchivo("maze.txt")  #CON ESTE CREE EL MAPA

camino = []
encontrar(inicio(maze,0),maze)

while (['0'] in camino): camino.remove(['0']) #AQUI QUITO EL 0 DE LAS HORIZONTALES

ass(list(camino))

sol = solucion()[::-1]   #CON ESTE MUESTRA LA SOLUCION A TRAVES DEL MAPA

print (sol)
