# First networkx library is imported 
# along with matplotlib
import networkx as nx
import matplotlib.pyplot as plt
#import matplotlib.animation.FuncAnimation
import random
import time


# Defining a Class
class GraphVisualization:
   
    def __init__(self):
          
        # visual is a list which stores all 
        # the set of edges that constitutes a
        # graph
        self.visual = []
          
    # addEdge function inputs the vertices of an
    # edge and appends it to the visual list
    def addEdge(self, a, b):
        temp = [a, b]
        self.visual.append(temp)

    # In visualize function G is an object of
    # class Graph given by networkx G.add_edges_from(visual)
    # creates a graph with a given list
    # nx.draw_networkx(G) - plots the graph
    # plt.show() - displays the graph
    def visualize(self):
        G = nx.Graph()
        G.add_edges_from(self.visual)
        nx.draw_networkx(G)
		#ani = FuncAnimation(fig=G, func=animate, frames=range(len(alphabet)), interval=500, repeat=True)
        plt.show()
  
# Driver code

G = GraphVisualization()
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXZ"

for k in range(0,len(alphabet)):
	
	first_random = random.choice(alphabet)
	alphabet.replace(first_random,'')	
	second_random = random.choice(alphabet)
	G.addEdge(first_random,second_random)

G.visualize()	
