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


# Ln gamma function ln((x-1)!) ->  ln(0) + ln(1) + ... + ln(x-1)
def ln_gamma(x):
    return sum(np.log(range(1, int(x))))


def find(arr, target):
    array = np.array([], dtype='int64')
    for i in range(np.size(arr)):
        if arr[i] == target:
            array = np.append(array, i)
    return array


def score(dataset, var, var_parents):
    score = 0
    n = np.size(dataset[0])
    dim_var = 2
    range_var = [0, 1]
    r_i = dim_var
    data_o = dataset
    used = np.zeros(n, dtype='int64')

    d = 1
    # Get first unproccesed sample
    while d <= n:
        freq = np.zeros(int(dim_var), dtype='int64')
        while d <= n and used[d - 1] == 1:
            d += 1
        if d > n:
            break
        for i in range(int(dim_var)):
            if range_var[i] == data_o[d - 1, var]:
                break
        freq[i] = 1
        used[d - 1] = 1
        parent = dataset[d - 1, var_parents]
        d += 1
        # count frequencies of state while keeping rack of used samples
        for j in range(d - 1, n):
            if used[j] == 0:
                if (parent == data_o[j, var_parents]).all():
                    i = 0
                    while range_var[i] != data_o[j, var]:
                        i += 1
                    freq[i] += 1
                    used[j] = 1
        sum_m = np.sum(freq)
        r_i = int(r_i)

        # finally sum over frequencies to get log likelihood bayesian score
        # with uniform priors

        for j in range(1, r_i + 1):
            if freq[j - 1] != 0:
                score += ln_gamma(freq[j - 1] + 1)
        score += ln_gamma(r_i) - ln_gamma(sum_m + r_i)

    return score


# upper_boud è in numero max di padri che può x un nodo
def k2():
    dataset = np.array(
        [[1, 0, 0], [1, 1, 1], [0, 0, 1], [1, 1, 1], [0, 0, 0], [0, 1, 1], [1, 1, 1], [0, 0, 0], [1, 1, 1], [0, 0, 0]])
    order = [0, 1, 2]
    dim = 3  # numero di variabili
    u = 2  # numero max di padri per un nodo
    dag = np.zeros((dim, dim))

    k2_score = np.zeros((1, dim))

    for i in range(1, dim):

        parent = np.zeros((dim, 1))
        ok = 1
        p_old = -1e10
        while ok == 1 and np.sum(parent) < u:
            local_max = -10e10
            local_node = 0
            # iterate through possible parent connections to determine best action
            for j in range(i - 1, -1, -1):
                if parent[order[j]] == 0:
                    parent[order[j]] = 1

                    # score this node
                    local_score = score(dataset, order[i], find(parent[:, 0], 1))

                    # determine local max
                    if local_score > local_max:
                        local_max = local_score
                        local_node = order[j]
                    # mark parent processed
                    parent[order[j]] = 0
            # assign the highest parent
            p_new = local_max
            if p_new > p_old:
                p_old = p_new
                parent[local_node] = 1
            else:
                ok = 0
            k2_score[0, order[i]] = p_old
            dag[:, order[i]] = parent.reshape(dim)

    print(dag, k2_score)
    return dag, k2_score
