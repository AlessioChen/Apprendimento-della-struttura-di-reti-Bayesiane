# classe che rappresenta il nodo della rete bayesiana

class Node:
    def __init__(self, name, parents, cpt, domain_values, value ):
        self.name = name  # nome del none
        self.parents = parents  # array con i padri
        self.cpt = cpt  # matrice delle pobablità
        self.domaian_values = domain_values #valori del dominio
        self.value = value

        self.color = 'white'
        self.f = 0

    def print_node(self):
        print(name)
        print(parents)
        print(cpt)
        print(doman_values)