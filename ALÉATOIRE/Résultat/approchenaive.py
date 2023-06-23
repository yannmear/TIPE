import graph_tool.all as gt
import time as t
from os import makedirs, listdir
from random import shuffle,randint
from numpy import random
from tqdm import tqdm

from matplotlib.pyplot import show, plot, grid



### DOSSIERS ET NOMS




### GÉNÉRATION D'UN GRAPHE PLANAIRE

def GraphePlanaire(nombre_sommet):
	if "Graphe_"+str(nombre_sommet)+"_"+"0" in listdir("Graphes/"):
		L = listdir("Graphes/")
		L_ = [g.split(str(nombre_sommet)) for g in L]
		L__ = [e for e in L_  if len(e)>1] 
		G = [int(e[1].split("_")[1]) for e in L__]
		m = max(G)
		nom = "Graphe_"+str(nombre_sommet)+"_"+str(m+1)
		makedirs("Graphes/" + nom + "/" + "couverture")	
	else:
		nom = "Graphe_"+str(nombre_sommet)+"_"+"0"
		makedirs("Graphes/" + nom + "/" + "couverture")
		makedirs("Graphes/" + nom + "/" + "couverture/a")
		makedirs("Graphes/" + nom + "/" + "couverture/c")

	t0 = t.time()
	points = random.random((nombre_sommet,2))
	g, pos = gt.triangulation(points, type="delaunay")
	#weight = g.new_edge_property("double")
	#for e in g.edges():
		#weight[e] = sqrt(sum((array(pos[e.source()]) -
	     #                    array(pos[e.target()]))**2))

	sommets = [int(s) for s in g.vertices()]
	arêtes = [(int(ent),int(sort)) for (ent,sort) in g.edges()]
	g.vp["pos"] = pos
	g.save("Graphes/"+nom+"/"+nom +".graphml")  #g.saving.save_property_map(pos,"pos.pmap")
	f = open("Graphes/" + nom + "/" + "données-" + nom + ".txt","a")
	f.write("temps " +str(t.time()-t0))
	f.write("\n sommets :"+ str(sommets) + "\n arêtes : " + str(arêtes))
	f.close() ; print(g)
	gt.is_planar(g)
	gt.remove_random_edges(g,0.3*len(arêtes))
	gt.graph_draw(g, pos=pos, vertex_fill_color="red", edge_pen_width=0.3,output = "Graphes/" + nom + "/" + nom+".pdf")



### COUVERTURE ALÉATOIRE

NOMS = [i for i in listdir("Graphes/")]
GRAPHES = [gt.load_graph("Graphes/"+nom+"/"+nom+".graphml") for nom in NOMS]

nom_graphe = {NOMS[i] : GRAPHES[i] for i in range(len(NOMS))}

def CouvertureAlea(n,nom,export=True):
	g = nom_graphe[nom]
	l = [int(i) for i in g.vertices()] ; longueur = len(l) 
	shuffle(l)
	recouvrement = set([l.pop() for i in range(n)])
	couverts = [] ; A_couv=[]
	for i in recouvrement : 
		Sommets = g.get_all_neighbors(i)
		for s in Sommets : 
			couverts.append(s)
		couverts.append(i)

	couverts = set(couverts)


	A_couv = set(A_couv)
	print(listdir("Graphes/" + nom + "/couverture/"))
	if export : 
		vcolor = g.new_vertex_property("string")
		ecolor = g.new_edge_property("string")
		for e in g.edges():
			ecolor[e] = "black"

		ewidth = g.new_edge_property("float")


		for s in g.vertices():
			if int(s) in recouvrement : 
				vcolor[s] = "blue"
			else : 
				vcolor[s] = "red"



		for s in couverts :
			if int(s) not in recouvrement :
				vcolor[s] = "yellow"
		if listdir("Graphes/" + nom + "/couverture/c/") == [] : 
			gt.graph_draw(g, pos=g.vp.pos , vertex_fill_color=vcolor, edge_color = ecolor, edge_pen_width=0.6, vertex_size = 10, output = "Graphes/" + nom + "/couverture/c/" + "c0.pdf" )
		else : 
			Z = [int(i.split(".")[0].split("c")[1]) for i in listdir("Graphes/" + nom + "/couverture/c/")] ; z = max(Z)+1
			gt.graph_draw(g, pos=g.vp.pos , vertex_fill_color=vcolor, edge_color = ecolor, edge_pen_width=0.6, vertex_size = 10, output = "Graphes/" + nom + "/couverture/c/" + "c" + str(z) + ".pdf" )
	return (len(couverts)/len(l),recouvrement,couverts)


#GraphePlanaire(15000)
#print(CouvertureAlea(30,"Graphe_300_0",False))


def N_couvertures_alea(s,N,nom):
	g = nom_graphe[nom]
	Taux_de_recouvrement = [0] #à chaque itération
	Taux_réel  = []
	Recouvrements = []
	Couvertures = []
	for i in tqdm(range(N)):
		(taux,r,c) = CouvertureAlea(s,nom,False)
		Taux_réel.append(taux) ; Recouvrements.append(r), Couvertures.append(c)
		if taux > Taux_de_recouvrement[-1] :
			Taux_de_recouvrement.append(taux)
		else : 
			Taux_de_recouvrement.append(Taux_de_recouvrement[-1])
	tout = {i : (Taux_réel[i],Recouvrements[i],Couvertures[i]) for i in range(len(Taux_réel))}
	tri = sorted(tout, key = tout.get)
	f = open("Graphes/" + nom + "/couverture/recouvrement-"+ str(s) +"_" + str(N) +  ".txt","w")
	M = 50
	for k in range(1,M+1):
		f.write(str(tout[tri[len(tout)-k]])+"\n")
	f.close()
	return (Taux_de_recouvrement[-1],Taux_de_recouvrement)

'''f=open("resultat.txt","w")

print("RÉSULTAT  :",file = f)
print(N_couvertures_alea(3000,1000,"Graphe_15000_1"), file = f)
print("\n \n RÉSULTAT  :",file = f)
print(N_couvertures_alea(600,1000,"Graphe_15000_1") ,file = f )
print("\n \n RÉSULTAT  :",file = f)
print(N_couvertures_alea(1000,1000,"Graphe_15000_1") ,file = f )
print("\n \n RÉSULTAT  :",file = f)
print(N_couvertures_alea(1500,1000,"Graphe_15000_1") ,file = f )
f.close()'''


def CouvertureAleaAméliorée(n,nom,export=True):
	g = nom_graphe[nom]
	l = [int(i) for i in g.vertices()] ; longueur = len(l) 
	shuffle(l)
	recouvrement = [] ; couverts = []
	long = len(recouvrement)
	while len(recouvrement) != n :
		a = l.pop()
		a_c = g.get_all_neighbors(a)
		b = True
		for s in recouvrement : 
			if s in a_c : 
				b = False 
				break
		if b : 
			recouvrement.append(a)
			for s in a_c : 
				couverts.append(s)
			long +=1 
	for i in recouvrement : 
		couverts.append(i)
	couverts = set(couverts)

	if export : 
		vcolor = g.new_vertex_property("string")
		ecolor = g.new_edge_property("string")
		for e in g.edges():
			ecolor[e] = "black"

		ewidth = g.new_edge_property("float")


		for s in g.vertices():
			if int(s) in recouvrement : 
				vcolor[s] = "blue"
			else : 
				vcolor[s] = "red"



		for s in couverts :
			if int(s) not in recouvrement :
				vcolor[s] = "yellow"
		if listdir("Graphes/" + nom + "/couverture/a/") == [] : 
			gt.graph_draw(g, pos=g.vp.pos , vertex_fill_color=vcolor, edge_color = ecolor, edge_pen_width=0.6, vertex_size = 10, output = "Graphes/" + nom + "/couverture/a/" + "a0.pdf" )
		else : 
			Z = [int(i.split(".")[0].split("a")[1]) for i in listdir("Graphes/" + nom + "/couverture/a/")] ;  z = max(Z)+1
			gt.graph_draw(g, pos=g.vp.pos , vertex_fill_color=vcolor, edge_color = ecolor, edge_pen_width=0.6, vertex_size = 10, output = "Graphes/" + nom + "/couverture/a/" + "a" + str(z) + ".pdf" )
	return (len(couverts)/len(l),recouvrement,couverts)


def N_couvertures_alea_am(s,N,nom):
	g = nom_graphe[nom]
	Taux_de_recouvrement = [0] #à chaque itération
	Taux_réel  = []
	Recouvrements = []
	Couvertures = []
	for i in tqdm(range(N)):
		(taux,r,c) = CouvertureAleaAméliorée(s,nom,False)
		Taux_réel.append(taux) ; Recouvrements.append(r), Couvertures.append(c)
		if taux > Taux_de_recouvrement[-1] :
			Taux_de_recouvrement.append(taux)
		else : 
			Taux_de_recouvrement.append(Taux_de_recouvrement[-1])
	tout = {i : (Taux_réel[i],Recouvrements[i],Couvertures[i]) for i in range(len(Taux_réel))}
	tri = sorted(tout, key = tout.get)
	f = open("Graphes/" + nom + "/couverture/recouvrement-a-"+ str(s) +"_" + str(N) +  ".txt","w")
	M = 50
	for k in range(1,M+1):
		f.write(str(tout[tri[len(tout)-k]])+"\n")
	f.close()
	return (Taux_de_recouvrement[-1],Taux_de_recouvrement)


def N_couvertures_alea_var(e,s,N,nom):
	sommet = e
	g = nom_graphe[nom]
	Taux_de_recouvrement = [0] #à chaque itération
	Taux_réel  = []
	Recouvrements = []
	Couvertures = []
	for i in tqdm(range(N)):
		(taux,r,c) = CouvertureAlea(sommet,nom,False)
		Taux_réel.append(taux) ; Recouvrements.append(r), Couvertures.append(c)
		if taux > Taux_de_recouvrement[-1] :
			Taux_de_recouvrement.append(taux)
		else : 
			Taux_de_recouvrement.append(Taux_de_recouvrement[-1])
		sommet += (s-e)//2
	tout = {i : (Taux_réel[i],Recouvrements[i],Couvertures[i]) for i in range(len(Taux_réel))}
	tri = sorted(tout, key = tout.get)
	f = open("Graphes/" + nom + "/couverture/recouvrement-"+ str(s) +"_" + str(N) +  ".txt","w")
	M = 50
	for k in range(1,M+1):
		f.write(str(tout[tri[len(tout)-k]])+"\n")
	f.close()
	f=open("Graphes/" + nom + "/couverture/resultat "+str(e) + "_" + str(s)+".txt","w")
	print("RÉSULTAT  :",file = f)
	print(N_couvertures_alea(3000,1000,"Graphe_15000_1"), file = f)
	return (Taux_de_recouvrement[-1],Taux_de_recouvrement)


'''
L_A = [ CouvertureAleaAméliorée(1500,"Graphe_15000_1",False)[0] for i in tqdm(range(10))]
L = [ CouvertureAlea(1500,"Graphe_15000_1",False)[0] for i in tqdm(range(10))]

la = sum(L_A)/1000 *100
l = sum(L)/1000 *100
f = open("Graphes/Graphe_15000_1/ameliore_vs_normal2.txt","w")
f.write("AMELIORE :" +  str(la) + "\n")
f.write("NORMAL :" + str(l) + "\n")
f.close()
'''

temps = t.time()
print(CouvertureAleaAméliorée(1500,"Graphe_15000_0",False)[0])
print(t.time() - temps)

### TRACÉ DES RÉSULTATS