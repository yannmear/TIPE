from graph_tool.all import *
from numpy import *
import time as t
from os import makedirs, listdir
import pickle as pck

from random import shuffle

#Attribution du nom
def dossiers(endroit): #retourne la liste des noms de dossiers de l' 'endroit'
	g = [int(i) for i in endroit if len(i.split("."))==1]
	return g

nb = max(dossiers(listdir()))+1; nom = str(nb)

#Génération d'un graphe planaire
def GraphePlanaire():
	makedirs(nom)
	t0 = t.time()
	points = random.random((1000,2))
	g, pos = triangulation(points, type="delaunay")
	f = open(nom+"/"+nom+"-pos"+".txt","a")
	f.write(str(pos))
	f.close()
	weight = g.new_edge_property("integer")
	pen = g.new_edge_property("float")
	for e in g.edges():

	sommets = [int(s) for s in g.vertices()]
	arêtes = [(int(ent),int(sort)) for (ent,sort) in g.edges()]
	g.save(nom+"/"+"graph"+nom+".graphml") ; saving.save_property_map(pos,"pos.pmap")
	f = open(nom+"/"+nom+".txt","a")
	f.write("temps " +str(t.time()-t0))
	f.write("\n sommets :"+ str(sommets) + "\n arêtes : " + str(arêtes))
	f.close() ; print(g)
	remove_random_edges(g,0.2*len(arêtes))
	graph_draw(g, pos=pos, vertex_fill_color="red", edge_pen_width=0.3,output = nom+"/"+nom+".pdf")

'''Remarque : si on prend par exemple la ville de Paris, il existe des polygones à plus de trois côtés délimités, donc 
il faut arbitrairement retirer des arêtes à notre triangulation'''
GraphePlanaire()

#Couverture aléatoire
#g = load_graph("7/graph7.graphml")
def CouvertureAlea(n,g):
	l = [int(i) for i in g.vertices()] ; longueur = len(l) 
	shuffle(l)
	recouvrement = [l.pop() for i in range(n)]
	couverts = [] ; couleur = {(i for i in g.vertices()) : "red"}
	for i in recouvrement : 
		Sommets = g.get_all_neighbors(i)
		for s in Sommets : 
			couverts.append(s)
			couleur[s] = "blue"
	#f = open(nom+'/'+nom+"-"+str(n)+"-couverture.txt","a")
	ratio = len(couverts)/longueur
	#f.write(str(ratio) + "\n" + str(recouvrement))
	print(is_planar(g))
	return (len(couverts)/longueur)


def CouvertureAleaFois(essais,n,g):
	L = []
	for loop in range(essais):
		L.append(CouvertureAlea(n,g))
	return max(L)



