import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError('List must contain nine numbers.')
    else:
        matrix = np.array(list).reshape(3, 3)
    #mean, variance, standard deviation, max, min, and sum of the rows, columns, and elements in a 3 x 3 matrix.
    mean_calc = [(matrix.mean(axis=0).tolist()), (matrix.mean(axis=1).tolist()), (matrix.flatten().mean())]
    var_calc = [(matrix.var(axis=0).tolist()), (matrix.var(axis=1).tolist()), (matrix.flatten().var())]
    std_calc = [(matrix.std(axis=0).tolist()), (matrix.std(axis=1).tolist()), (matrix.flatten().std())]
    max_calc = [(matrix.max(axis=0).tolist()), (matrix.max(axis=1).tolist()), (matrix.flatten().max())]
    min_calc = [(matrix.min(axis=0).tolist()), (matrix.min(axis=1).tolist()), (matrix.flatten().min())]
    sum_calc = [(matrix.sum(axis=0).tolist()), (matrix.sum(axis=1).tolist()), (matrix.flatten().sum())]
    calculations = {
        "mean": mean_calc,
        "variance": var_calc,
        "standard deviation": std_calc,
        "max": max_calc,
        "min": min_calc,
        "sum": sum_calc,
    }
    return calculations