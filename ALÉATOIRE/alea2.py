from graph_tool.all import *
from numpy import *
import time as t
from os import makedirs, listdir
import pickle as pck

from random import shuffle,randint

points = random.random((30,2))
g, pos = triangulation(points,type="delaunay")

l = [int(i) for i in g.vertices()] ; longueur = len(l) 
shuffle(l)
recouvrement = [l.pop() for i in range(5)]
couverts = []
for i in recouvrement : 
	Sommets = g.get_all_neighbors(i)
	for s in Sommets : 
		couverts.append(s)




vcolor = g.new_vertex_property("string")
ecolor = g.new_edge_property("string")
weight = g.new_edge_property("float")

print(list(g.iter_edges()))

'''
for i in range(longueur_edges/4):
	weight[g.iter_edges()[i]] = randint(2,4)

for i in range(longueur_edges/4,longueur_edges):
	weight[g.iter_edges()[i]] = randint(1,2)
'''


for e in g.edges():
	ecolor[e] = "black"

'''

for s in g.vertices():
	if int(s) in recouvrement : 
		vcolor[s] = "blue"
	else : 
		vcolor[s] = "red"



for s in couverts :
	if s not in recouvrement :
		vcolor[s] = "yellow"
'''
graph_draw(g, pos=pos, vertex_fill_color="black", edge_color = ecolor, edge_pen_width=1, vertex_size = 10)
