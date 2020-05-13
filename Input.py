from Node import *


def asia_net():
    nodes = [0, 0, 0, 0, 0, 0, 0, 0]

    nodes[0] = Node('asia', set(), [0.01], [0, 1], 0)
    nodes[1] = Node('tub', set([0]), [0.05, 0.01], [0, 1], 1)
    nodes[2] = Node('smoke', set(), [0.5], [0, 1], 2)
    nodes[3] = Node('lung', set([2]), [0.1, 0.01], [0, 1], 3)
    nodes[4] = Node('bronc', set([2]), [0.6, 0.3], [0, 1], 4)
    nodes[5] = Node('either', set([1, 3]), [1.0, 1.0, 1.0, 0.0], [0, 1], 5)
    nodes[6] = Node('xray', set([5]), [0.98, 0.05], [0, 1], 6)
    nodes[7] = Node('dysp', set([4, 5]), [0.9, 0.7, 0.8, 0.1], [0, 1], 7)

    return nodes


def cancer_net():
    nodes = [0, 0, 0, 0, 0]
    nodes[0] = Node('pollution', [], [0.9], [0, 1], 0)
    nodes[1] = Node('Smoker', [], [0.3], [0, 1], 1)
    nodes[2] = Node('Cancer', [0, 1], [0.03, 0.05, 0.001, 0.02], [0, 1], 2)
    nodes[3] = Node('Xray', [2], [0.9, 0.2], [0, 1], 3)
    nodes[4] = Node('Dyspnoa', [2], [0.65, 0.3], [0, 1], 4)
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
