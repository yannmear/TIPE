import pandas as pd
from graph_tool.all import *
from tqdm import tqdm
from numpy import array

def Intersection(A,B):
	I = []
	for i in A : 
		for j in B : 
			if i == j : 
				I.append(i)
	return I 

files = ["croisement3.json"]
rd = [pd.read_json(i) for i in files]

coord_brut = rd[0]["pos"].to_dict()
text = rd[0]["rues"].to_dict()

### Étape 1 : Même jeu de coordonnées pour l'intersection A-B et l'intersection B-A

connexité_rues = {} # dictionnaire dont l'appel d'un nom de rue renvoie le nom des rues adjacentes
for i in text :
	if text[i][0] in connexité_rues : 
		connexité_rues[text[i][0]].append(text[i][1])
	else : 
		connexité_rues[text[i][0]] = [text[i][1]]

print(connexité_rues["Rue Delambre"])
print(connexité_rues["Boulevard du Montparnasse"])

def privé(L,G):
	H = []
	for l in L : 
		if l not in G : 
			H.append(l)
	return H

impasses = []
for r in connexité_rues : 
	for j in connexité_rues[r] :
		if j not in connexité_rues :
			impasses.append(j)
impasses = array(impasses)

for r in tqdm(connexité_rues) : 
	for j in range(len(connexité_rues[r])) :
		l = [] 
		if connexité_rues[r][j] in impasses : 
			l.append(j)
	for j in l : 
		connexité_rues[r].append(j)


l = [] 
for i in connexité_rues :
	if connexité_rues[i] == [] :
		l.append(i)

connexité_rues2 = {}
for j in connexité_rues : 
	if j not in l :
		connexité_rues2[j] = connexité_rues[j]

connexité_rues = connexité_rues2

rue_coord = {i : (text[i],coord_brut[i]) for i in range(len(text))}


def Rechercher(st1,st2=""):
	numéros = []
	for j in rue_coord : 
		if (st2 in rue_coord[j][0][1] or st2 in rue_coord[j][0][0]) and (st1 in rue_coord[j][0][1] or st1 in rue_coord[j][0][0]) : 
			numéros.append(j)
	return (numéros,[rue_coord[i] for i in numéros])


def ÉmondageGénéral(XY):
	XY_ = dict(XY) ; l = len(XY_)
	Final = {}
	j = 0
	while XY_ != {} :
		el = XY_[j]
		L = Rechercher(el[0][0],el[0][1])
		x,y = 0,0
		for s in L[0] : 
			s_ = XY_.pop(s)
			x += s_[1][0]
			y += s_[1][1]
			x /= len(L[0])
			y /= len(L[0])
		Final[el[0][0] + ' - ' + el[0][1]] = (x,y)
		j = list(XY_)[-1]
		print(len(XY_))
	return Final

