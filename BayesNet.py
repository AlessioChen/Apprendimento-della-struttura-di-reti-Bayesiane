# classe che rappresenta la rete bayesiana

from Dataset import *


class BayesNet:

    def __init__(self, nodes):
        self.nodes = nodes
        self.n = len(self.nodes)
        self.dag = np.zeros((1, 1))

        for i in range(len(nodes)):
            nodes[i].cpt = np.asfarray(nodes[i].cpt, float)

        self.dag_gen()

    # genera la matrice di adiacenza che rappresenta il grafo
    def dag_gen(self):
        self.dag = np.zeros((self.n, self.n))

        for i in range(self.n):
            for j in self.nodes[i].parents:  # j sono gli indici dei padri
                self.dag[j][i] = 1

    def print_graph(self):
        print(self.dag)


