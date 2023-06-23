import graph_tool.all as gt

# Créer un graphe
g = gt.Graph()

# Ajouter des arêtes au graphe
v1 = g.add_vertex()
v2 = g.add_vertex()
v3 = g.add_vertex()
e1 = g.add_edge(v1, v2)
e2 = g.add_edge(v2, v3)
e3 = g.add_edge(v3, v1)

# Créer une EdgePropertyMap pour stocker les couleurs des arêtes
edge_colors = g.new_edge_property("string")

# Définir les couleurs des arêtes
for e in g.get_all_edges(v1):
	

# Accéder aux couleurs des arêtes
print(edge_colors[e1])  # [1.0, 0.0, 0.0]

# Appliquer les couleurs aux arêtes lors du rendu
gt.graph_draw(g, edge_color=edge_colors)

# Sauvegarder le graphe avec les couleurs des arêtes
gt.graph_draw(g, edge_color=edge_colors, output="graph.png")
