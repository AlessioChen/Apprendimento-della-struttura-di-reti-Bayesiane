def read_bn(path):
    """
    Wrapper function for reading BayesNet objects
    from various file types.
    Arguments
    ---------
    *path* : a string
        The path (relative or absolute) - MUST
        include extension -> that's how we know
        which file reader to call.
    Returns
    -------
    *bn* : a BayesNet object
    Effects
    -------
    None
    Notes
    -----
    """
    if '.bif' in path:
        return read_bif(path)
    elif '.bn' in path:
        return read_json(path)
    elif '.mat' in path:
        return read_mat(path)
    else:
        print("Path Extension not recognized")


def read_bif(path):
    """
    This function reads a .bif file into a
    BayesNet object. It's probably not the
    fastest or prettiest but it gets the job
    done.
    Arguments
    ---------
    *V* : a list of strings
    *E* : a dict, where key = vertex, val = list of its children
    *F* : a dict, where key = rv, val = another dict with
                keys = 'parents', 'values', cpt'
    """
    _parents = {}  # key = vertex, value = list of vertices in the scope (includind itself)
    _cpt = {}  # key = vertex, value = list (then numpy array)
    _vals = {}  # key=vertex, val=list of its possible values

    with open(path, 'r') as f:
        while True:
            line = f.readline()
            if 'variable' in line:
                new_vertex = line.split()[1]

                _parents[new_vertex] = []
                _cpt[new_vertex] = []
                _vals[new_vertex] = []

                new_line = f.readline()
                new_vals = new_line.replace(',', ' ').split()[6:-1]  # list of vals
                _vals[new_vertex] = new_vals
            elif 'probability' in line:
                line = line.replace(',', ' ')
                child_rv = line.split()[2]
                parent_rvs = line.split()[4:-2]

                if len(parent_rvs) == 0:  # prior
                    new_line = f.readline().replace(';', ' ').replace(',', ' ').split()
                    prob_values = new_line[1:]
                    _cpt[child_rv].append(map(float, prob_values))
                    # _cpt[child_rv] = map(float,prob_values)
                else:  # not a prior
                    _parents[child_rv].extend(list(parent_rvs))
                    while True:
                        new_line = f.readline()
                        if '}' in new_line:
                            break
                        new_line = new_line.replace(',', ' ').replace(';', ' ').replace('(', ' ').replace(')',
                                                                                                          ' ').split()
                        prob_values = new_line[-(len(_vals[new_vertex])):]
                        prob_values = map(float, prob_values)
                        _cpt[child_rv].append(prob_values)
            if line == '':
                break

    # CREATE FACTORS
    _F = {}
    _E = {}
    for rv in _vals.keys():
        _E[rv] = [c for c in _vals.keys() if rv in _parents[c]]
        f = {
            'parents': _parents[rv],
            'values': _vals[rv],
            'cpt': [item for sublist in _cpt[rv] for item in sublist]
        }
        _F[rv] = f






read_bif("data/asia.bif")
