import copy

import numpy as np

from Node import Node


# lettura da file della rete
def read_bif(path):
    nodes = []
    with open(path, 'r') as f:
        i = 0
        c = 0

        while True:
            line = f.readline()
            if 'variable' in line:
                name = line.split()[1]

                new_line = f.readline()
                domain_values = new_line.replace(',', ' ').split()[6:-1]  # list of vals
                node = Node(name, [], [], domain_values, i)
                i = i + 1

                nodes.append(node)
            elif 'probability' in line:
                line = line.replace(',', ' ')
                child = line.split()[2]
                parents = line.split()[4:-2]

                if len(parents) == 0:  # prior
                    new_line = f.readline().replace(';', ' ').replace(',', ' ').split()
                    prob_values = new_line[1:]

                    nodes[c].cpt = prob_values
                else:  # not a prior
                    while True:
                        new_line = f.readline()

                        if '}' in new_line:
                            break
                        new_line = new_line.replace(',', ' ').replace(';', ' ').replace('(', ' ').replace(')',
                                                                                                          ' ').split()

                        prob_values = new_line[(len(parents)):]
                        a = np.asfarray(prob_values, float)
                        nodes[c].cpt.append(a)

                    for j in range(len(parents)):
                        for k in range(len(nodes)):
                            if nodes[k].name == parents[j]:
                                nodes[c].parents.append(k)

                c = c + 1
            if line == '':
                break

    return nodes

def dfs_visit(nodes, adjacency_matrix, u):
    global time
    time += 1
    u.color = 'Grey'
    for i in range(len(adjacency_matrix)):
        if adjacency_matrix[u.value, i] == 1 and nodes[i].color == 'White':
            nodes[i].parents = u.value
            dfs_visit(nodes, adjacency_matrix, nodes[i])
    u.color = 'Black'
    time += 1
    u.f = time
    return u.f

def dfs(nodes, adjacency_matrix):
    for i in nodes:
        i.color = 'White'
        i.parents = None
    global time
    time = 0
    for i in nodes:
        if i.color == 'White':
            dfs_visit(nodes, adjacency_matrix, i)

def order(adjacency_matrix, nodes):
    # deep copy, serve per il dataset
    nodes1 = copy.deepcopy(nodes)
    dfs(nodes1, adjacency_matrix)
    nodes1.sort(key=lambda x: x.f, reverse=True)
    nodes_ordered = []
    for i in range(len(nodes)):
        nodes_ordered.append(nodes1[i])
    return nodes_ordered
