import matplotlib.pyplot as plt
import numpy as np


def _main():
    fig, (axes_earth, axes_traveler) = plt.subplots(1, 2, figsize=(8, 8))
    _plot(axes_earth, "Earth")
    _plot(axes_traveler, "Traveler")
    plt.show()


def _plot(axes, title):
    traveler_x_first_leg = np.linspace(0, 1)
    traveler_y_first_leg = 2 * traveler_x_first_leg
    traveler_x_second_leg = np.linspace(1, 0)
    traveler_y_second_leg = 2 + 2 * (1 - traveler_x_second_leg)

    axes.set_title(title)
    axes.set_xlabel("x")
    axes.set_ylabel("t")
    axes.plot(traveler_x_first_leg, traveler_y_first_leg, label="First leg")
    axes.plot(traveler_x_second_leg, traveler_y_second_leg, label="Second leg")
    axes.legend()


if __name__ == "__main__":
    _main()
