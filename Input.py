from Node import *


def asia_net():
    nodes = [0, 0, 0, 0, 0, 0, 0, 0]

    nodes[0] = Node('asia', set(), [0.01], [0, 1], 0)
    nodes[1] = Node('tub', set([0]), [0.01, 0.05], [0, 1], 1)
    nodes[2] = Node('smoke', set(), [0.5], [0, 1], 2)
    nodes[3] = Node('lung', set([2]), [0.01, 0.1], [0, 1], 3)
    nodes[4] = Node('bronc', set([2]), [0.3, 0.6], [0, 1], 4)
    nodes[5] = Node('either', set([1, 3]), [0.0, 1.0, 1.0, 1.0], [0, 1], 5)
    nodes[6] = Node('xray', set([5]), [0.05, 0.98], [0, 1], 6)
    nodes[7] = Node('dysp', set([4, 5]), [0.1, 0.7, 0.8, 0.9], [0, 1], 7)

    return nodes


def cancer_net():
    nodes = [0, 0, 0, 0, 0]
    nodes[0] = Node('pollution', [], [0.9], [0, 1], 0)
    nodes[1] = Node('Smoker', [], [0.3], [0, 1], 1)
    nodes[2] = Node('Cancer', [0, 1], [0.001, 0.03, 0.02, 0.05], [0, 1], 2)
    nodes[3] = Node('Xray', [2], [0.2, 0.9], [0, 1], 3)
    nodes[4] = Node('Dyspnoa', [2], [0.3, 0.65], [0, 1], 4)
    return nodes

