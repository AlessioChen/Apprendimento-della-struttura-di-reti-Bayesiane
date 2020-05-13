import random

import numpy as np

from Order_functions import *


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
        # riga che sto esaminando
        p_i = self.net.nodes[i].parents
        prob = 0

        if len(p_i) == 0:  # no parents
            prob = self.net.nodes[i].cpt[0]

        if len(p_i) == 1:  # 1 parents
            for j in p_i:
                if self.dataset[index][j] == 1:
                    prob = self.net.nodes[i].cpt[0]
                else:
                    prob = self.net.nodes[i].cpt[1]

        if len(p_i) == 2:  # 2 parents
            s = list(p_i)
            a = self.dataset[index][s[0]]
            b = self.dataset[index][s[1]]
            if a == 1 and b == 1:
                prob = self.net.nodes[i].cpt[0]
            if a == 0 and b == 1:
                prob = self.net.nodes[i].cpt[1]

            if a == 1 and b == 0:
                prob = self.net.nodes[i].cpt[2]
            if a == 0 and b == 0:
                prob = self.net.nodes[i].cpt[3]

        return prob

