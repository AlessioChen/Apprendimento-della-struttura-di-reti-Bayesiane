# classe che rappresenta la rete bayesiana

import numpy as np

from Dataset import *


class BayesNet:

    def __init__(self, nodes):
        self.nodes = nodes
        self.n = len(self.nodes)
        self.dag = np.zeros((1, 1))

        for i in range(len(nodes)):
            nodes[i].cpt = np.asfarray(nodes[i].cpt, float)

        self.adjMatrixGen()

    # genera la matrice di adiacenza che rappresenta il grafo
    def adjMatrixGen(self):
        self.dag = np.zeros((self.n, self.n))

        for i in range(self.n):
            for j in range(len(self.nodes[i].parents)):
                for k in range(self.n):
                    if self.nodes[i].parents[j] == self.nodes[k].value:
                        self.dag[k][i] = 1

    def print_graph(self):
        print(self.dag)


# nodes = read_bif('data/asia.bif')
#
# net = BayesNet(nodes)
# # dataset = Dataset(net, 100000)


dataset = [[1, 0, 0], [1, 1, 1], [0, 0, 1], [1, 1, 1], [0, 0, 0], [0, 1, 1], [1, 1, 1], [0, 0, 0], [1, 1, 1], [0, 0, 0]]
k2(dataset, [0, 1, 2], 1, 3)
