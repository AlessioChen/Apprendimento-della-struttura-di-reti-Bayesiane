import copy


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
