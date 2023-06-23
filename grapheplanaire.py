import graph_tool.all as gt
import numpy as np
import time as t
t0 = t.time()

points = np.random.random((400, 2)) * 4


g, pos = gt.triangulation(points, type="delaunay")


weight = g.new_edge_property("double")
for e in g.edges():
	weight[e] = np.sqrt(sum((np.array(pos[e.source()]) -
                         np.array(pos[e.target()]))**2))

print(t.time()-t0)

gt.graph_draw(g, pos=pos, vertex_fill_color="red",
              edge_pen_width=0.3)
