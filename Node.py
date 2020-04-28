# classe che rappresenta il nodo della rete bayesiana

class Node:
    def __init__(self, name, parents, cpt, value):
        self.name = name  # nome del none
        self.parents = parents  # array con i padri
        self.cpt = cpt  # matrice delle pobablità
        self.value = value

        self.color = 'white'
        self.f = 0
