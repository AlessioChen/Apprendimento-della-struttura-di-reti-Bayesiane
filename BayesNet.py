# classe che rappresenta la rete bayesiana

import numpy as np
import Read
import Node

class BayesNet:

    def __init__(self, nodes):
        self.nodes = nodes
        self.n = len(self.nodes)
        self.adjMatrix = []

        for i in range (len(nodes)):
            nodes[i].cpt = np.asfarray(nodes[i].cpt,float)
            nodes[i].print_node()
        self.adjMatrixGen()




    #genera la matrice di adiacenza che rappresenta il grafo
    def adjMatrixGen(self):
        self.adjMatrix = np.zeros((self.n, self.n))

        for i in range(self.n):
            for j in range(len(self.nodes[i].parents)):
                for k in range (self.n):
                    if self.nodes[i].parents[j] == self.nodes[k].value:
                        self.adjMatrix[k][i] = 1


    def print_graph(self):
        print(self.adjMatrix)


nodes = Read.read_bif('data/asia.bif')
net = BayesNet(nodes)
net.print_graph()

