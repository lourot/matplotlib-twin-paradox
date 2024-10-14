from typing import Any, Final

import matplotlib.pyplot as plt
import numpy as np


def _main() -> None:
    fig, (axes_earth, axes_traveler) = plt.subplots(1, 2, sharey=True, figsize=(8, 8))
    _plot(axes_earth, "Earth")
    _plot(axes_traveler, "Traveler", "x'", "t'", 1, ":")
    plt.show()


def _plot(axes, title, xlabel="x", ylabel="t", linewidth=2, linestyle="-") -> None:
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
    axes.set_xlabel(xlabel, color=label_color, fontsize=label_fontsize)
    axes.set_ylabel(ylabel, color=label_color, fontsize=label_fontsize)

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

    planet_label: Final[str] = "Planet"
    planet_color: Final[str] = "red"
    arrow_head_size: Final[int] = 7
    axes.plot(
        markers_x, markers_y, "s", label=planet_label, color=planet_color
    )  # s=square
    axes.annotate(
        planet_label,
        xy=(markers_x[0] - 0.01, markers_y[0] + 0.05),
        textcoords="offset fontsize",
        xytext=(-4, 5.2),
        color=planet_color,
        arrowprops=dict(
            # arrowstyle="fancy",
            # relpos=(10, -10),
            color=planet_color,
            width=1,
            headwidth=arrow_head_size,
            headlength=arrow_head_size,
            # shrink=0.5,
        ),
    )

    axes.set_xlim(0, 1)
    axes.set_ylim(0, 4)

    axes.grid()
    # axes.legend()


if __name__ == "__main__":
    _main()
