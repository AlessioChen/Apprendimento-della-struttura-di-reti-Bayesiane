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


nodes = asia_net()
net = BayesNet(nodes)
dataset = Dataset(net, 150)

for j in range(len(nodes)):
    nodes[j].parents = set()

# x1 = Node('x1', set(), [], [0, 1], 0)
# x2 = Node('x2', set(), [], [0, 1], 1)
# x3 = Node('x3', set(), [], [0, 1], 2)
#
# dataset = [[1, 0, 0], [1, 1, 1], [0, 0, 1], [1, 1, 1], [0, 0, 0], [0, 1, 1], [1, 1, 1], [0, 0, 0], [1, 1, 1], [0, 0, 0]]
# k2(dataset, [x1, x2, x3], 1)
for i in range(1000):
    nodes = asia_net()
    net = BayesNet(nodes)
    dataset = Dataset(net, 150)
    k2(dataset.dataset, dataset.ordered_array, 2)
