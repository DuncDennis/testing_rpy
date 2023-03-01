import numpy as np

def loop(model,
         use_for_pred: np.ndarray,
         sync_steps: int = 0,
         pred_steps: int | None = None,
         reset_reservoir_bool: bool = True):
    """Simple Reimplimentation of predict function for reservoirpy."""
    sync = use_for_pred[:sync_steps]
    true_data = use_for_pred[sync_steps:]
    if reset_reservoir_bool:
        model.reset()  # not sure what this does.

    # sync the reservoir:
    warmup_y = model.run(sync, reset=False)

    # Take as many pred_steps as there are true_data steps if None:
    if pred_steps is None:
        pred_steps = true_data.shape[0]

    # Array to save pred_data to:
    inp_dim = use_for_pred.shape[1]
    pred_data = np.zeros((pred_steps, inp_dim))

    # save data:
    pred_data[0, :] = warmup_y[-1]
    x = warmup_y[-1, :].reshape(1, -1)
    for i in range(1, pred_steps):
        x = model(x)
        pred_data[i, :] = x

    return pred_data, true_data
