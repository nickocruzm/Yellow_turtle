import matplotlib.pyplot as plt
import networkx as nx

G = nx.Graph()

G.add_node(1)

nx.draw(G)
plt.show()