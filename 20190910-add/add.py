def get_shape(matrix):
    return [len(r) for r in matrix]

def add(*matrices):
    if any(get_shape(m) != get_shape(matrices[0]) for m in matrices):
        raise ValueError('Matrices are not all the same size.')
    else:
        return [[sum(vals) for vals in zip(*rows)]
                 for rows
                 in zip(*matrices)]
