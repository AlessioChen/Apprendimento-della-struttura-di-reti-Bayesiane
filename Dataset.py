import random

import numpy as np

from Dfs import *


# classe che genera un dataset data la rete e la dimensione
class Dataset:
    def __init__(self, bn_net, dim):
        self.net = bn_net  # rete bayesiana
        self.dim = dim  # numero di righe del dataset
        self.dataset = np.zeros((self.dim, self.net.n))

        # con il DFS mi genera un cammino dalla radice alle foglie
        self.ordered_array = order(self.net.dag, self.net.nodes)

        for i in range(self.dim):  # righe del dataset
            for j in range(self.net.n):  # colonne del dataset
                r1 = random.random()
                r2 = self.get_prob(self.ordered_array[j].value, i)
                if r1 <= r2:
                    self.dataset[i][self.ordered_array[j].value] = 1

    def get_prob(self, i, index):
        # i è l'indice del nodo
        # index riga che sto esaminando
        p_i = self.net.nodes[i].parents
        prob = 0

        if len(p_i) == 0:  # no parents
            prob = self.net.nodes[i].cpt[0]
        else:
            dim = len(p_i)
            s = sorted(p_i)
            k = 0
            for j in range(dim):
                k += 2 ** (dim - j - 1) * self.dataset[index][s[j]]
            prob = self.net.nodes[i].cpt[int(k)]

        return prob
