import random

from Functions import *


# classe che genera un dataset data la rete e la dimensione
class Dataset:
    def __init__(self, bn_net, dim):
        self.net = bn_net
        self.dim = dim
        self.dataset = np.zeros((self.dim, self.net.n))
        # con il DFS mi genera un cammino dalla radice alle foglie
        self.ordered_array = order(self.net.dag, self.net.nodes)

        for i in range(self.dim):  # righe del dataset
            for j in range(self.net.n):  # colonne del dataset
                r1 = random.random()
                r2 = self.get_prob(self.ordered_array[j].value, i)
                if r1 <= r2:
                    self.dataset[i][self.ordered_array[j].value] = 1

    #     mat = np.asmatrix(self.dataset)
    #     names = ''
    #     for i in range(len(self.net.nodes)):
    #         names = names + ' ' + self.net.nodes[i].name
    #
    # # np.savetxt('out.txt', mat, header=names, fmt='%s')

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


def get_order(self):
    order = np.zeros(len(self.ordered_array), dtype='int64')
    for i in range(len(self.ordered_array)):
        order[i] = int(self.ordered_array[i].value)

    return order
