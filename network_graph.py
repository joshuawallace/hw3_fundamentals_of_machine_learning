# Created by JJW Apr 8 2016
# This plots a network map of the data
# for COS 424 Assignment 3

# big thanks to https://networkx.github.io/documentation/networkx-1.10/reference/classes.graph.html#networkx.Graph
# and http://stackoverflow.com/questions/21978487/improving-python-networkx-graph-layout


import networkx as nx
import matplotlib.pyplot as plt
import random as rand
rand.seed(2343)

import general_functions as general_f

# Number of transactions to graph
num = 10000

# Read in the data
data = general_f.data_readin()

# Pull out "num" number of transactions
senders_sample, receivers_sample = zip(*rand.sample(list(zip(data.sender_ids, data.receiver_ids)), num))

# Make a graph and add the transactions to it
G = nx.Graph()
temp = [(senders_sample[i], receivers_sample[i])
        for i in range(num)]
G.add_edges_from(temp)
print len(G)
pos = nx.spring_layout(G, scale=2)
nx.draw(G, pos, font_size=8, node_size=0, width=0.001)

# Figure set up
fig = plt.gcf()
fig.set_size_inches(6, 2.7)

# Save figure
fig.savefig("fig1.pdf")
