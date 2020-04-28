from Node import Node
import numpy as np

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
                        a = np.asfarray(prob_values,float)
                        nodes[c].cpt.append(a)

                    for j in range(len(parents)):
                        for k in range(len(nodes)):
                            if nodes[k].name == parents[j]:
                                nodes[c].parents.append(k)

                c = c + 1
            if line == '':
                break
            print()

    return nodes


read_bif('data/asia.bif')
