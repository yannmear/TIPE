from graph_tool.all import * 

from graph_tool.all import *
from numpy import *
import time as t
from os import makedirs, listdir
import pickle as pck
from tqdm import tqdm

from random import shuffle,randint

'''
points = random.random((100,2))
g, pos = triangulation(points,type="delaunay")
proppos = g.new_vertex_property("vector<double>")
g.vp["pos"] = pos

graph_draw(g, pos = pos)
g.save("graph.graphml",fmt="graphml")
'''
g = load_graph("graph.graphml")


sommets = [s for s in g.vertices()]


n = 1000000

def Taux(L):
	return len(set(L))/len(sommets)

def MeilleuresCouvertures(n,N) :
	sommets_ = list(sommets)
	shuffle(sommets_)
	recouvrements,couvertures = {},{}
	for j in tqdm(range(0,n)):
		recouvrements['rc_%s' % j] = []
		couvertures['c_%s' % j ] = []
		sommets_ = list(sommets)
		shuffle(sommets_)
		for l in range(10):
			z = sommets_.pop()
			recouvrements['rc_%s' % j].append(z)
			Z = g.get_all_neighbors(z)
			for z_ in Z : 
				couvertures['c_%s' % j ].append(z_)
	RecCouv = [(Taux(couvertures['c_%s' % j]),recouvrements['rc_%s' % j],set(couvertures['c_%s' % j])) for j in range(n)]
	RecCouv.sort() ; RecCouv.reverse()
	return RecCouv[0 : N]


f = open("meilleures.txt","r")
MeilleuresRecCouv = list(f.read())

