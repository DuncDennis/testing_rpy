from typing import Union

import numpy as np
import networkx as nx
from reservoirpy.mat_gen import Initializer


def _erdos_renyi_network(
    nodes_x: int,
    nodes_y: int,
    connectivity: float = 0.4,
    seed: Union[int, np.random.Generator] = None,
    **kwargs
):
    if nodes_x != nodes_y:
        raise ValueError("Works only for n to n graphs.")

    rng = np.random.default_rng(seed)

    network = nx.fast_gnp_random_graph(nodes_x, p=connectivity, seed=seed)
    network = nx.to_numpy_array(network)

    # vary:
    arg_binary_network = np.argwhere(network)
    rand_shape = network[network != 0.].shape
    network[arg_binary_network[:, 0], arg_binary_network[:, 1]] = rng.random(size=rand_shape) - 0.5

    return network

erdos_renyi_network = Initializer(_erdos_renyi_network)


def _random_sparse_win(
    out_dim: int,
    inp_dim: int,
    seed: Union[int, np.random.Generator] = None,
    **kwargs
):
    # RNG:
    rng = np.random.default_rng(seed)

    # Create input matrix:
    w_in = np.zeros((out_dim, inp_dim))
    for i in range(out_dim):
        random_x_coord = rng.choice(np.arange(inp_dim))
        w_in[i, random_x_coord] = rng.uniform(low=-1, high=+1)

    return w_in

random_sparse_win = Initializer(_random_sparse_win)


def _random_node_bias(
    nodes_x: int,
    other_dim: int, # has to be 1.
    seed: Union[int, np.random.Generator] = None,
    **kwargs
):
    # RNG:
    rng = np.random.default_rng(seed)

    # Create input matrix:
    node_bias = rng.uniform(low=-1.0, high=1.0, size=nodes_x).reshape(nodes_x, 1)

    return node_bias

random_node_bias = Initializer(_random_node_bias)
