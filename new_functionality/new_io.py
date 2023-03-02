import numpy as np
from sklearn.preprocessing import StandardScaler
from reservoirpy import Node

def _inp_scaler_initialize(inp_node: "Node", x=None, **kwargs):
    """InputScaler initialize function.

    Sets the input and output dimension of the node, and fits the StandardScaler to the data.
    Uses **kwargs as a y argument must also be parsable.
    """
    inp_node.set_input_dim(x.shape[1])
    inp_node.set_output_dim(x.shape[1])
    scaler = StandardScaler()
    inp_node.set_param("scaler", scaler)

def _inp_scaler_forward(inp_node: "InputScaler", x):
    return inp_node.scaler.transform(x)

def _inp_scaler_backward(inp_node: "InputScaler", X: np.ndarray, *args, **kwargs):
    for seq in X:
        inp_node.scaler.fit(seq)

class InputScaler(Node):
    def __init__(self, name=None, **kwargs):
        super(InputScaler, self).__init__(
            forward=_inp_scaler_forward,
            initializer=_inp_scaler_initialize,
            backward=_inp_scaler_backward,
            params={"scaler": None},
            name=name,
            **kwargs,
        )
