import random

from Functions import *


# classe che genera un dataset data la rete e la dimensione
class Dataset:
    def __init__(self, bn_net, dim):
        self.net = bn_net
        self.dim = dim
        self.dataset = np.zeros((self.dim, self.net.n))
        # con il DFS mi genera un cammino dalla radice alle foglie
        self.ordedered_array = order(self.net.dag, self.net.nodes)

        for i in range(self.dim):  # righe del dataset
            for j in range(self.net.n):  # colonne del dataset
                r1 = float(random.random())
                r2 = float(self.get_prob(i, self.ordedered_array[j].value))
                if r1 <= r2:
                    self.dataset[i][self.ordedered_array[j].value] = 1

        mat = np.asmatrix(self.dataset)
        names = ''
        for i in range(len(self.net.nodes)):
            names = names + ' ' + self.net.nodes[i].name

        np.savetxt('out.txt', mat, header=names, fmt='%s')

    def get_prob(self, i, k):
        # k è i'indice del nodo che sto esaminando ordinato in base al DFS
        # i è l'indice del nodo padre
        prob = 0

        if len(self.net.nodes[k].parents) == 0:  # prior p(a)
            prob = self.net.nodes[k].cpt[0]
        else:
            prob = self.net.nodes[k].cpt[1]

        if len(self.net.nodes[k].parents) == 1:  # nodo con un padre
            if self.dataset[i][self.net.nodes[k].parents[0]] == 1:
                prob = self.net.nodes[k].cpt[0][0]
            else:
                prob = self.net.nodes[k].cpt[1][0]

        if len(self.net.nodes[k].parents) == 2:  # nodo con due padri
            if self.dataset[i][self.net.nodes[k].parents[0]] == 1:
                if self.dataset[i][self.net.nodes[k].parents[1]] == 1:
                    prob = self.net.nodes[k].cpt[0][0]
                else:
                    prob = self.net.nodes[k].cpt[2][0]

            else:
                if self.dataset[i][self.net.nodes[k].parents[1]] == 0:
                    prob = self.net.nodes[k].cpt[3][0]
                else:
                    prob = self.net.nodes[k].cpt[1][0]

        return prob
