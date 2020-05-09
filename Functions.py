import copy
import itertools
import math

import numpy as np

from Node import Node


# lettura da file della rete
def asia_net():
    nodes = [0, 0, 0, 0, 0, 0, 0, 0]

    nodes[0] = Node('asia', [], [0.01], [0, 1], 0)
    nodes[1] = Node('tub', [0], [0.05, 0.01], [0, 1], 1)
    nodes[2] = Node('smoke', [], [0.5], [0, 1], 2)
    nodes[3] = Node('lung', [2], [0.1, 0.01], [0, 1], 3)
    nodes[4] = Node('bronc', [2], [0.6, 0.3], [0, 1], 4)
    nodes[5] = Node('either', [1, 3], [1.0, 1.0, 1.0, 0.0], [0, 1], 5)
    nodes[6] = Node('xray', [5], [0.98, 0.05], [0, 1], 6)
    nodes[7] = Node('dysp', [4, 5], [0.9, 0.7, 0.8, 0.1], [0, 1], 7)

    return nodes


# funzione che legge il grado da file
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


def cartesian_product(n, f_i):
    # n è il numero di padri
    count = 0
    x = [0, 1]
    if n == 1:
        for iter in itertools.product(x):
            f_i[count] = iter
            count += 1
    if n == 2:
        for iter in itertools.product(x, x):
            f_i[count] = iter
            count += 1

    return f_i


def count_case(dataset, f_i, p_i, i, j, k):
    # i indice della variabile
    # j configurazione dei padri
    # k valore che può assumere la variabile i
    # f_i insieme delle configurazione dei padri di i

    a_ijk = 0
    a = f_i[j]
    if len(p_i) == 0:  # 0 padri
        for m in range(len(dataset)):
            if dataset[m][i] == k:
                a_ijk = a_ijk + 1
    else:
        for m in range(len(dataset)):
            if dataset[m][i] == k:
                for index in range(len(p_i)):
                    if dataset[m][p_i[index]] == a[index]:
                        a_ijk = a_ijk + 1
    return a_ijk


def score(dataset, node_i, p_i):
    # r_i = #dei valori che può assumere la variabile x_i
    r_i = len(node_i.domain_values)
    i = node_i.value
    n_ij = 0
    p1 = 1
    p2 = 1
    # TODO considerare il caso q_i= 0
    q_i = 2 ** len(p_i)

    # genera il prodotto cartesiano
    f_i = np.zeros((q_i, (len(p_i))))
    f_i = cartesian_product(len(p_i), f_i)

    for j in range(len(p_i) + 1):
        for k in range(r_i):
            a_ijk = count_case(dataset, f_i, p_i, i, j, node_i.domain_values[k])
            n_ij = n_ij + a_ijk
            p2 = p2 * math.factorial(a_ijk)
        n1 = math.factorial(r_i - 1)
        d1 = math.factorial(n_ij + r_i - 1)
        quoziente = n1 / d1
        p1 = p1 * quoziente
    score = p1 * p2

    print(score)
    print()
    return score


def k2(dataset, node_order, upper_bound):
    n = len(node_order)
    pred = []
    for i in range(n):
        p_new = -10e10
        p_old = score(dataset, node_order[i], node_order[i].parents)
        ok = True
        while ok == True and len(node_order[i].parents) < upper_bound:
            for x in range(n):
                if x in pred and x not in node_order[i].parents:
                    temp = node_order[i].parents
                    temp.append((int(x)))
                    local_score = score(dataset, node_order[i], temp)
                    if local_score > p_new:
                        z = x
                        p_new = local_score
            # p_new forse da ricalcolare?
            if p_new > p_old:
                p_old = p_new
                node_order[i].parents = np.append(node_order[i].parents, int(z))
            else:
                ok = False
            pred = np.append(pred, int(i))

    for j in range(len(node_order)):
        print(node_order[j].parents)
