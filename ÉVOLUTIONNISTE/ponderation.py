from graph_tool.all import *
from numpy import *
import time as t
from os import makedirs, listdir
import pickle as pck

from random import shuffle,randint
from math import sqrt

def distance(a,b):
	return sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2 )

## Génération d'un graphe pondéré
def GraphePondere(s,n=0):
	points = random.random((s,2))
	g, pos = triangulation(points,type="delaunay")
	vcolor = g.new_vertex_property("string")
	ecolor = g.new_edge_property("string")
	weight = g.new_edge_property("double")
	labels = g.new_edge_property("string")

	def Étiquette(x):
		if x ==1 : 
			return "ruelle"
		if x ==2 : 
			return "rue"
		if x==3 : 
			return "grande rue"
		if x==4 : 
			return "avenue"
		if x==5 : 
			return "boulevard"

	z = 0 ; longueur_aretes = len(list(g.edges()))
	for e in g.edges():
		if z < longueur_aretes//6 :
			weight[e] = randint(3,5)
			labels[e] = Étiquette(weight[e])
		else : 
			weight[e]=randint(1,2)
			labels[e] = Étiquette(weight[e])
		z+=1
	'''
	for k in range(len(list(pos))):
	    adj = g.get_all_neighbors(k)
	    dist = [distance(pos[k], pos[i]) for i in adj]
	    if any(d < 1 for d in dist):
	        avg_x = sum(pos[i][0] for i in adj) / len(adj)
	        avg_y = sum(pos[i][1] for i in adj) / len(adj)
	        pos[k][0] = avg_x
	        pos[k][1] = avg_y
	'''

	sommets = [int(i) for i in g.vertices()] ; longueur_sommets = len(sommets) 
	shuffle(sommets)
	recouvrement = [sommets.pop() for i in range(n)]
	couverts = []
	for i in recouvrement : 
		Sommets = g.get_all_neighbors(i)
		for s in Sommets : 
			couverts.append(s)





	for e in g.edges():
		ecolor[e] = "black"



	for s in g.vertices():
		if int(s) in recouvrement : 
			vcolor[s] = "blue"
		else : 
			vcolor[s] = "red"



	for s in couverts :
		if s not in recouvrement :
			vcolor[s] = "yellow"

	remove_random_edges(g,0.1*longueur_aretes)
	g.vp['pos'] = pos ; g.ep['weight'] = weight ; g.ep['labels'] = labels ; g.save("pondere.graphml")
	graph_draw(g, pos=pos, vertex_fill_color=vcolor, edge_color = ecolor, edge_pen_width=weight, vertex_size = 5, edge_text = weight, edge_font_size = 3, output = "pondere.pdf")
	graph_draw(g, pos=pos, vertex_fill_color=vcolor, edge_color = ecolor, edge_pen_width=weight, vertex_size = 5, edge_text = weight, edge_font_size = 8)

GraphePondere(200)