from pyswip import Prolog 

p = Prolog()
p.consult('laberinto.pl')

 
for r in p.query("sol."):
    lista = r

print (lista) 