import numpy as np

def random_unit_vectors(num_vectors, dim):
    M = np.random.randn(num_vectors, dim)
    lengths = np.linalg.norm(M, axis=1, keepdims=True)
    lengths[lengths == 0] = 1
    return M / lengths


