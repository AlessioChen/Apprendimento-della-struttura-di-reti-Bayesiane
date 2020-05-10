from BayesNet import *

sum_dag = np.zeros((8, 8))
for i in range(10000):
    nodes = asia_net()
    net = BayesNet(nodes)
    dataset = Dataset(net, 150)
    app = k2(dataset.dataset, dataset.ordered_array, 2)
    sum_dag = sum_dag + app

print(sum_dag)

# x1 = Node('x1', set(), [], [0, 1], 0)
# x2 = Node('x2', set(), [], [0, 1], 1)
# x3 = Node('x3', set(), [], [0, 1], 2)
#
# dataset = [[1, 0, 0], [1, 1, 1], [0, 0, 1], [1, 1, 1], [0, 0, 0], [0, 1, 1], [1, 1, 1], [0, 0, 0], [1, 1, 1], [0, 0, 0]]
# k2(dataset, [x1, x2, x3], 1)
