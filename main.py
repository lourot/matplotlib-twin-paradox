from typing import Any, Final

import matplotlib.pyplot as plt
import numpy as np


def _main() -> None:
    fig, (axes_earth, axes_traveler) = plt.subplots(1, 2, figsize=(8, 8))
    _plot(axes_earth, "Earth")
    _plot(axes_traveler, "Traveler", 1, ":")
    plt.show()


def _plot(axes, title, linewidth=2, linestyle="-") -> None:
    earth_x: Final[Any] = np.linspace(0, 0)
    earth_y: Final[Any] = np.linspace(0, 4)
    traveler_x_first_leg: Final[Any] = np.linspace(0, 1)
    traveler_y_first_leg: Final[Any] = 2 * traveler_x_first_leg
    traveler_x_second_leg: Final[Any] = np.linspace(1, 0)
    traveler_y_second_leg: Final[Any] = 2 + 2 * (1 - traveler_x_second_leg)
    markers_x: Final[Any] = [
        1,
    ]
    markers_y: Final[Any] = [
        2,
    ]

    axes.set_title(title)
    label_color: Final[str] = "green"
    label_fontsize: Final[int] = 14
    axes.set_xlabel("x", color=label_color, fontsize=label_fontsize)
    axes.set_ylabel("t", color=label_color, fontsize=label_fontsize)
    axes.plot(
        earth_x,
        earth_y,
        label="Earth",
        color="blue",
        linewidth=linewidth,
        linestyle=linestyle,
    )
    axes.plot(
        traveler_x_first_leg,
        traveler_y_first_leg,
        label="First leg",
        color="orange",
        linewidth=linewidth,
        linestyle=linestyle,
    )
    axes.plot(
        traveler_x_second_leg,
        traveler_y_second_leg,
        label="Second leg",
        color="orange",
        linewidth=linewidth,
        linestyle=linestyle,
    )
    axes.plot(markers_x, markers_y, "s", label="Other planet", color="red")  # s=square

    axes.grid()
    # axes.legend()


if __name__ == "__main__":
    _main()
