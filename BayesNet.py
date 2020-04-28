# classe che rappresenta la rete bayesiana

import numpy as np
import Read


class BayesNet:

    def __init__(self, nodes):
        self.nodes = nodes
        self.n = len(self.nodes)
        self.adjMatrix = []

    #genera la matrice di adiacenza che rappresenta il grafo
    def adjMatrixGen(self):
        self.adjMatrix = np.zeros((self.n, self.n))

        for i in range(self.n):
            for j in range(len(self.nodes[i].pi)):




