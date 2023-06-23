import graph_tool.all as gt
from tqdm import tqdm
from numpy import array
import pandas as pd


import math

files = ["croisement3.json"]
rd = [pd.read_json(i) for i in files]


Croisements_orientés = rd[0]['rues'].to_dict() 
Coordonnées_croisements = rd[0]['pos'].to_dict()
Rues_connexes_orientées = {}

Noms_c = list(Croisements_orientés.values())
Clefs =  list(Croisements_orientés.keys())
Code_intersection = {str(Noms_c[i]) : Clefs[i] for i in range(len(Croisements_orientés))}




############################




'''On liste les croisements, à noter que le jeu de données des
croisements donne le sens. [i1,i2] révèle qu'on peut aller
sur la rue i1 depuis la rue i2'''

'''for i in Croisements_orientés : 
	i1,i2 = Croisements_orientés[i][0],Croisements_orientés[i][1]
	if i1 in Rues_connexes_orientées : 
		Rues_connexes_orientées[i1].append(i2)
	else : 
		Rues_connexes_orientées[i1] = [i2]'''


#On constate ici l'inutilité d'une intersection sachant qu'elle est intégralement contenue dans l'autre


'''
print(Croisements_orientés[5])
print(Croisements_orientés[785])

def Inclusion(L,G):
	return set(L)<set(G)
print(len(Croisements_orientés))
inclus  =[]
for i in tqdm(Croisements_orientés) :
	for j in Croisements_orientés : 
		if Inclusion(Croisements_orientés[j], Croisements_orientés[i]) :
			inclus.append(j)
print(inclus)
print(len(Croisements_orientés))'''

Inclus = [785, 2340, 3229, 3316, 3076, 25, 2025, 2853, 111, 3488, 3489, 3494, 3504, 3429, 3216, 124, 2930, 2931, 2085, 2089, 172, 2454, 2455, 1548, 1551, 3497, 1212, 7440, 275, 276, 2456, 3041, 1326, 303, 321, 1212, 367, 376, 376, 3588, 2072, 2317, 404, 7694, 396, 2251, 406, 425, 1039, 1041, 428, 1886, 1886, 2088, 2917, 556, 2086, 461, 1911, 2958, 685, 497, 2161, 1608, 2857, 1025, 512, 517, 517, 3465, 2061, 2068, 1923, 6880, 7484, 553, 2848, 2897, 1930, 2776, 581, 2852, 590, 594, 3610, 1741, 6087, 1516, 2296, 635, 640, 650, 2007, 2007, 5348, 8182, 921, 2137, 2137, 715, 1024, 733, 2837, 8982, 733, 8982, 929, 1461, 425, 1379, 6437, 7844, 1458, 827, 2901, 2902, 3211, 3247, 3248, 2982, 3143, 2953, 1317, 2915, 7627, 497, 7963, 943, 929, 3206, 3321, 8875, 939, 2858, 1720, 3229, 1002, 1965, 2915, 497, 1038, 1062, 1138, 8872, 1082, 1082, 2080, 2855, 2856, 1122, 4166, 2306, 3230, 3949, 2593, 5933, 4714, 7083, 1492, 4502, 2811, 1067, 1198, 5375, 3070, 5538, 1814, 1509, 2433, 1326, 1337, 3062, 3143, 8872, 8872, 8872, 2231, 8871, 1461, 2048, 1469, 2049, 1469, 1469, 1469, 1469, 1469, 1469, 1469, 2848, 2296, 1527, 3248, 1545, 2024, 4620, 1549, 4078, 1595, 1594, 1593, 1604, 1610, 1535, 1458, 8320, 3865, 1708, 7306, 7306, 2061, 2069, 8807, 8272, 1976, 8415, 1778, 6542, 1796, 6542, 8621, 3676, 1503, 2811, 1832, 1836, 1831, 1832, 1836, 3270, 21, 2846, 2847, 1971, 3367, 6087, 570, 2776, 1957, 1973, 1935, 2433, 3398, 1985, 2994, 2995, 4893, 2003, 2279, 3209, 2066, 724, 2080, 2122, 3453, 3496, 5302, 2178, 8355, 2252, 2252, 2304, 2306, 2827, 8791, 5157, 2314, 2353, 2353, 6359, 6359, 2347, 4654, 2345, 2347, 4654, 7776, 8946, 6880, 7938, 2441, 3301, 3289, 7617, 2467, 2466, 8701, 5501, 6679, 5038, 8514, 8393, 6457, 8935, 8890, 5081, 3228, 56, 3211, 3247, 4178, 2773, 8478, 2945, 4393, 8052, 3239, 5823, 3164, 4592, 8501, 8501, 8501, 2448, 1618, 6282, 7659, 5464, 4339, 3288, 2990, 2990, 8568, 5019, 7015, 7508, 3034, 4117, 6027, 3048, 6455, 5499, 6525, 7702, 8790, 3861, 1232, 7255, 3790, 6396, 3098, 3102, 1789, 1796, 3126, 8469, 7824, 3143, 1969, 3246, 1933, 3159, 3248, 3229, 3332, 3301, 3201, 2448, 3321, 3259, 3100, 3248, 2817, 7791, 3351, 3472, 3363, 249, 8976, 3455, 738, 461, 3544, 1890, 461, 8874, 3663, 5936, 3709, 3734, 6236, 5157, 8262, 6367, 8740, 3865, 438, 8751, 37, 6701, 5102, 2017, 3043, 3610, 1593, 4155, 6536, 7958, 4209, 2852, 1469, 4441, 4592, 5240, 2623, 3701, 692, 695, 4562, 8724, 4654, 6729, 7938, 5027, 405, 5438, 4857, 5023, 5089, 5213, 2867, 7525, 7274, 6327, 5610, 6971, 6701, 8654, 5874, 1601, 1466, 6664, 6155, 7983, 8927, 5739, 8462, 6403, 6705, 7659, 8522, 5207, 8214, 8909, 1213, 7127, 8005, 8079, 733, 8982, 7928, 7367, 7367, 8202, 8120, 3186, 8863, 1469, 2699, 7585, 8863, 8355, 8707, 6701, 1002, 8877]
Inclus = set(Inclus)

for i in Inclus : 
	Croisements_orientés.pop(i)
	Coordonnées_croisements.pop(i)


############ DESSIN


TAILLE = 3
Clefs =  list(Croisements_orientés.keys())
dict_ville = { i : Clefs[i] for i in range(len(Clefs))}
dict_ville__ = { dict_ville[i] : i for i in dict_ville} 

Croisements_orientés_émondés = { i : Croisements_orientés[dict_ville[i]] for i in dict_ville }
Coordonnées_croisements_émondés = { i : Coordonnées_croisements[dict_ville[i]] for i in dict_ville}

Noms_c_émondés = list(Croisements_orientés_émondés.values())
Clefs_émondés =  list(Croisements_orientés_émondés.keys())
Code_intersection_émondés = {str(Noms_c_émondés[i]) : Clefs_émondés[i] for i in range(len(Croisements_orientés_émondés))}
#Ici on en a profité pour redéfinir exactement tous nos éléments précédents

''' VIEUX CODE SANS Croisement_orientés_émondés ville = gt.Graph({i:[] for i in range(len(dict_ville))})
pos = ville.new_vertex_property("vector<double>")
couleur = ville.new_vertex_property("string")
taille = ville.new_vertex_property("float")
for i in ville.get_vertices() : 
	pos[i] = (Coordonnées_croisements[dict_ville[i]][0],-Coordonnées_croisements[dict_ville[i]][1])
for i in ville.get_vertices() : 
	taille[i] = 2
	couleur[i] = 'red'


def RechercherIntersectionsRue(l):
	L = [] ; C = []
	for i in Croisements_orientés : 
		if l in Croisements_orientés[i] : 
			L.append(Croisements_orientés[i])
			C.append(dict_ville__[Code_intersection[str(Croisements_orientés[i])]])
	return (L,C) #Ici on renvoie les coordonnées dans la configuration dess croisements émondés

def Distance(A,B):
	return sqrt((A[0]-B[0])**2 - (A[1] - B[1])**2)

def Plus_proche_non_arête(i,C):
	...


def AfficherIntersectionsRues(l):
	for i in dict_ville : 
		if l in str(Croisements_orientés[dict_ville[i]]) :
			couleur[i] = 'blue'
			taille[i] = 5
	(L,C) = RechercherIntersectionsRue(l)
	gt.graph_draw(ville,pos=pos,vertex_size = taille, vertex_fill_color = couleur)




'''

ville = gt.Graph({i:[] for i in Croisements_orientés_émondés},directed=False)
pos = ville.new_vertex_property("vector<double>")
couleur = ville.new_vertex_property("string")
taille = ville.new_vertex_property("float")
for i in ville.get_vertices() : 
	pos[i] = (Coordonnées_croisements_émondés[i][0],-Coordonnées_croisements[dict_ville[i]][1])
for i in ville.get_vertices() : 
	taille[i] = TAILLE
	couleur[i] = 'red'



def RechercherIntersectionsRue(l):
	L = [] ; C = []
	for i in Croisements_orientés_émondés : 
		if l in Croisements_orientés_émondés[i] : 
			L.append(Croisements_orientés_émondés[i])
			C.append(Code_intersection_émondés[str(Noms_c_émondés[i])])
	return (L,C) #Ici on renvoie les coordonnées dans la configuration dess croisements émondés

def Distance(A,B):
	xa,ya = Coordonnées_croisements_émondés[A]
	xb,yb = Coordonnées_croisements_émondés[B]
	lon1,lat1 = math.radians(xa),math.radians(ya)
	lon2,lat2 = math.radians(xb),math.radians(yb)
	d = 2 * 6371 * math.asin(math.sqrt(math.sin((lat2-lat1)/2)**2 + math.cos(lat1)*math.cos(lat2)*math.sin((lon2-lon1)/2)**2  ))
	return d

'''def Tri_ouest_est(C):
	Longitudes = {i: Coordonnées_croisements_émondés[i][0] for i in C}
	Points = {Coordonnées_croisements_émondés[i][0] : i for i in Longitudes}
	L = list(Longitudes.values()) ; L.sort()
	return [Points[i] for i in L]''' 

def ProxLine(C):
	coordonnées = {i : tuple(Coordonnées_croisements_émondés[i]) for i in C}
	points = {tuple(Coordonnées_croisements_émondés[i]) : i for i in coordonnées}
	L = list(coordonnées.values()) ; L.sort()
	points_triés = {L[i] : points[L[i]] for i in range(len(L))}
	Arêtes = []
	for k in range(len(L)-1):
		Arêtes.append((points_triés[L[k]],points_triés[L[k+1]]))
	return Arêtes

def AfficherIntersectionsRue(l):
	for i in Croisements_orientés_émondés : 
		if l in str(Croisements_orientés_émondés[i]) :
			couleur[i] = 'blue'
			taille[i] = 4
	(L,C) = RechercherIntersectionsRue(l)
	A = ProxLine(C)
	for e in A : 
		ville.add_edge(e[0],e[1])
	gt.graph_draw(ville,pos=pos,vertex_size = taille, vertex_fill_color = couleur, edge_pen_width = 3, edge_color = "orange")



Rues = set([Croisements_orientés_émondés[i][0] for i in Croisements_orientés_émondés])

def AfficherTotalement():
	Arêtes = []
	for r in Rues : 
		(L,C) = RechercherIntersectionsRue(r)
		A = ProxLine(C)
		for e in A : 
			Arêtes.append(e)
	Arêtes = set(Arêtes)
	for e in Arêtes : 
		ville.add_edge(e[0],e[1])
	print(gt.is_planar(ville))
	gt.graph_draw(ville,pos=pos,vertex_size = taille, vertex_fill_color = couleur, output="test.pdf")

'''
print(Croisements_orientés_émondés[1824]) 
print(Croisements_orientés_émondés[548])'''
#Le périphérique couillonne tout ! 


#Il faut virer le périph ! 

Virer = RechercherIntersectionsRue("Boulevard Périphérique Intérieur")[1] + RechercherIntersectionsRue("Boulevard Périphérique Extérieur")[1]
for e in Virer : 
	a = Croisements_orientés_émondés[e]
	if "Boulevard Périphérique Intérieur" in a : 
		a.remove("Boulevard Périphérique Intérieur")
	else :
		a.remove("Boulevard Périphérique Extérieur")

Croisements_orientés_émondés[1136].remove('Avenue Jean Jaurès')
Croisements_orientés_émondés[1375].remove('Avenue Victor Hugo')


Noms_c_émondés = list(Croisements_orientés_émondés.values())
Clefs_émondés =  list(Croisements_orientés_émondés.keys())
Code_intersection_émondés = {str(Noms_c_émondés[i]) : Clefs_émondés[i] for i in range(len(Croisements_orientés_émondés))}

Rues = set([Croisements_orientés_émondés[i][0] for i in Croisements_orientés_émondés])

def RechercherIntersectionsRue(l):
	L = [] ; C = []
	for i in Croisements_orientés_émondés : 
		if l in Croisements_orientés_émondés[i] : 
			L.append(Croisements_orientés_émondés[i])
			C.append(Code_intersection_émondés[str(Noms_c_émondés[i])])
	return (L,C) #Ici on renvoie les coordonnées dans la configuration dess croisements émondés

def Distance(A,B):
	xa,ya = Coordonnées_croisements_émondés[A]
	xb,yb = Coordonnées_croisements_émondés[B]
	lon1,lat1 = math.radians(xa),math.radians(ya)
	lon2,lat2 = math.radians(xb),math.radians(yb)
	d = 2 * 6371 * math.asin(math.sqrt(math.sin((lat2-lat1)/2)**2 + math.cos(lat1)*math.cos(lat2)*math.sin((lon2-lon1)/2)**2  ))
	return d

'''def Tri_ouest_est(C):
	Longitudes = {i: Coordonnées_croisements_émondés[i][0] for i in C}
	Points = {Coordonnées_croisements_émondés[i][0] : i for i in Longitudes}
	L = list(Longitudes.values()) ; L.sort()
	return [Points[i] for i in L]''' 

def ProxLine(C):
	coordonnées = {i : tuple(Coordonnées_croisements_émondés[i]) for i in C}
	points = {tuple(Coordonnées_croisements_émondés[i]) : i for i in coordonnées}
	L = list(coordonnées.values()) ; L.sort()
	points_triés = {L[i] : points[L[i]] for i in range(len(L))}
	Arêtes = []
	for k in range(len(L)-1):
		Arêtes.append((points_triés[L[k]],points_triés[L[k+1]]))
	return Arêtes

def AfficherIntersectionsRue(l):
	for i in Croisements_orientés_émondés : 
		if l in str(Croisements_orientés_émondés[i]) :
			couleur[i] = 'blue'
			taille[i] = 4
	(L,C) = RechercherIntersectionsRue(l)
	A = ProxLine(C)
	for e in A : 
		ville.add_edge(e[0],e[1])
	gt.graph_draw(ville,pos=pos,vertex_size = taille, vertex_fill_color = couleur, edge_pen_width = 3, edge_color = "orange")



Rues = set([Croisements_orientés_émondés[i][0] for i in Croisements_orientés_émondés])

def AfficherTotalement():
	Arêtes = []
	for r in Rues : 
		(L,C) = RechercherIntersectionsRue(r)
		A = ProxLine(C)
		for e in A : 
			Arêtes.append(e)
	Arêtes = set(Arêtes)
	for e in Arêtes : 
		ville.add_edge(e[0],e[1])
	print(gt.is_planar(ville))
	gt.graph_draw(ville,pos=pos,vertex_size = taille, vertex_fill_color = couleur)


print(Croisements_orientés_émondés[1375])
print(Croisements_orientés_émondés[4180])
print(Croisements_orientés_émondés[6481])
print(Croisements_orientés_émondés[3137])
print(Croisements_orientés_émondés[451])
print(Croisements_orientés_émondés[1136])

''' Je vais réitérer mais en enlevant toutes les arêtes longues de plus d'un km '''


AfficherTotalement()