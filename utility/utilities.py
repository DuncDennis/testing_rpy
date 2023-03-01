import contextlib #  for temp_seed
import numpy as np

@contextlib.contextmanager
def temp_seed(seed: int | None = None):
    """
    from https://stackoverflow.com/questions/49555991/can-i-create-a-local-numpy-random-seed
    Use like:
    with temp_seed(5):
        <do_smth_that_uses_np.random>
    """
    if seed is None:
        try:
            yield
        finally:
            pass
    else:
        state = np.random.get_state()
        np.random.seed(seed)
        try:
            yield
        finally:
            np.random.set_state(state)
