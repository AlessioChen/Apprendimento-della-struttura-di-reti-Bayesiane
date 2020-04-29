import numpy as np

#classe che genera un dataset data la rete e la dimensione
class Dataset:
    def __init__(self, bn_net, dim):
        self.net = bn_net
        self.dim = dim
        self.dataset = np.zeros((self.dim,self.dim))


