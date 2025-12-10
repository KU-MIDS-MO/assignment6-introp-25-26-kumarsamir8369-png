import numpy as np

def estimate_pi(num_samples):
    pts = np.random.rand(num_samples, 2)
    dist = np.sqrt(pts[:,0]**2 + pts[:,1]**2)
    inside = np.sum(dist <= 1)
    return 4 * (inside / num_samples)
