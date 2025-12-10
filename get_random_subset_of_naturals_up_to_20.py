import numpy as np

def get_random_subset_of_naturals_up_to_20():
    bits = np.random.randint(0, 2, size=20)
    nums = np.arange(1, 21)
    return nums[bits == 1]




