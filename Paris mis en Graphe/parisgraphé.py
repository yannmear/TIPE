import pandas as pd
from graph_tool.all import *

files = ["croisementR.json"]
rd = [pd.read_json(i) for i in files]

coord = rd[0]["pos"].to_dict()
text = rd[0]["rues"].to_dict()




connexité_rues = {} # dictionnaire dont l'appel d'un nom de rue renvoie le nom des rues adjacentes


for i in text :
	if text[i][0] in connexité_rues : 
		connexité_rues[text[i][0]].append(text[i][1])
		if text[i][1] not in connexité_rues : 
			connexité_rues[text[i][1]] = []
	else : 
		connexité_rues[text[i][0]] = [text[i][1]]
		if text[i][1] not in connexité_rues : 
			connexité_rues[text[i][1]] = []


nom_rue= [i for i in connexité_rues.keys()] # ensemble des noms de rues
code_rue = {nom_rue[i]:i for i in range(len(nom_rue))} # dictionnaire des codes arbitrairement attriubés à chaque nom de rue

connexité_rues_codes = {code_rue[i]:[code_rue[j] for j in connexité_rues[i]] for i in nom_rue}


g = Graph(connexité_rues_codes,directed = True)
'''g = Graph()''' ; pos = g.new_vertex_property('vector<double>')
for i in coord : 
	pos[i]=(coord[i][0],coord[i][1])

pb = 0
for i in range(len(nom_rue)):
	if code_rue[nom_rue[i]] == 5756:
		pb = nom_rue[i]

print(pb)
graph_draw(g,pos=pos)

'''Jusqu'à présent j'ai des artéfacts sur mon graphe car : il y a des rues qui ne sont que des sorties et qui n'ont donc pas de coordonnées'''