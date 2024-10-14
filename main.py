import matplotlib.pyplot as plt
import numpy as np


def _main():
    traveler_x_first_leg = np.linspace(0, 1)
    traveler_y_first_leg = 2 * traveler_x_first_leg
    traveler_x_second_leg = np.linspace(1, 0)
    traveler_y_second_leg = 2 + 2 * (1 - traveler_x_second_leg)

    fig, ax = plt.subplots(figsize=(4, 8))
    ax.set_title("Time diagram - Earth")
    ax.set_xlabel("x")
    ax.set_ylabel("t")
    ax.plot(traveler_x_first_leg, traveler_y_first_leg, label="First leg")
    ax.plot(traveler_x_second_leg, traveler_y_second_leg, label="Second leg")
    ax.legend()
    plt.show()


if __name__ == "__main__":
    _main()
