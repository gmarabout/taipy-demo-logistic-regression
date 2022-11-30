import numpy as np

# Set seed for random number generator
rg = np.random.default_rng(seed=0)

# Create an array with 500 rows and 3 columns.
# This will serve as initial data node
initial_dataset = rg.normal(size=(500, 3))


def make_X(dataset):
    # Remove the first column which can be considered as noise
    X1 = np.delete(dataset, 0, axis=1)

    # Now create two more columns correlated with X1
    X2 = X1 + 0.1 * np.random.normal(size=(500, 2))
    X = np.concatenate((X1, X2), axis=1)

    return X


def make_Y(dataset):
    P = 1 / (1 + np.e ** (-np.matmul(dataset, [1, 1, 1])))
    Y = P > 0.5
    return Y
