import matplotlib.pyplot as plt
import numpy as np


def _main():
    x = np.linspace(0, 1)
    y = 2 * x

    fig, ax = plt.subplots()
    ax.set_title("Time diagram - Earth")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.plot(x, y)
    plt.show()


if __name__ == "__main__":
    _main()
