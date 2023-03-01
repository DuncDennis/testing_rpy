import matplotlib.pyplot as plt

def show_pred(y_pred, y_pred_true, dim=0, title=None):
    """Simple function to show pred vs. true pred. """
    plt.figure(figsize=(10, 3))
    if title is not None:
        plt.title(title)
    plt.xlabel("$t$")
    plt.plot(y_pred[:, dim], label="Pred", color="blue")
    plt.plot(y_pred_true[:, dim], label="True", color="red")
    plt.legend()
    plt.show()
