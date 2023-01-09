import matplotlib.pyplot as plt
import networkx as nx

G = nx.Graph()
S = nx.star_graph(20)
G.add_node(1)

nx.draw(S)
plt.show()