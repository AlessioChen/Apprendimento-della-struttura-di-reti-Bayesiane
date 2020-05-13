import numpy as np


# classe che rappresenta la rete bayesiana
class BayesNet:

    def __init__(self, nodes):
        self.nodes = nodes  # vettore dei nodi
        self.n = len(self.nodes)  # numero di nodi
        self.dag = np.zeros((self.n, self.n))  # matrice di adiacenza

        self.dag_gen()

    # genera la matrice di adiacenza che rappresenta il grafo
    def dag_gen(self):
        for i in range(self.n):
            for j in self.nodes[i].parents:  # j sono gli indici dei padri
                self.dag[j][i] = 1

    def print_graph(self):
        print(self.dag)


