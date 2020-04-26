class BayesNet():
    def __init__(self, E=None, value_dict=None, file=None):
        """
               Initialize the BayesNet class.
               Arguments
               ---------
               *V* : a list of strings - vertices in topsort order
               *E* : a dict, where key = vertex, val = list of its children
               *F* : a dict,
                   where key = rv,
                   val = another dict with
                       keys =
                           'parents',
                           'values',
                           'cpt'
               *V* : a dict
        """
        if file is not None:
            import read as reader
            bn = reader.read_bn(file)
            self.V = bn.V
            self.E = bn.E
            self.F = bn.F
        else:
            if E is not None:
                self.set_structure(E, value_dict)
            else:
                self.V = []
                self.E = {}
                self.F = {}
