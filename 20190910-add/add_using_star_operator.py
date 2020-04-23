def add(*matrices):
    return [[sum(vals) for vals in zip(*rows)]
             for rows
             in zip(*matrices)]
