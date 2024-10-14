from typing import Any, Final

import matplotlib.pyplot as plt
import numpy as np


def _main() -> None:
    _fig, (axes_earth, axes_traveler) = plt.subplots(
        1, 2, sharey=True, figsize=(5, 8), layout="tight", facecolor="lightgray"
    )
    _plot(axes_earth, "Earth")
    _plot(axes_traveler, "Traveler", "x'", "t'", linewidth=1, linestyle=":")
    plt.show()


def _plot(
    axes, title, xname="x", yname="t", xunit="ly", yunit="y", linewidth=2, linestyle="-"
) -> None:
    x_max: Final[float] = 10.0
    speed: Final[float] = 0.5
    t_max: Final[float] = 2 * x_max / speed

    earth_x: Final[Any] = np.linspace(0, 0)
    earth_t: Final[Any] = np.linspace(0, t_max)
    traveler_x_first_leg: Final[Any] = np.linspace(0, x_max)
    traveler_t_first_leg: Final[Any] = traveler_x_first_leg / speed
    traveler_x_second_leg: Final[Any] = np.linspace(x_max, 0)
    traveler_t_second_leg: Final[Any] = (
        t_max / 2 + (x_max - traveler_x_second_leg) / speed
    )
    markers_x: Final[Any] = [
        x_max,
    ]
    markers_t: Final[Any] = [
        t_max / 2,
    ]

    axes.set_title(title)
    label_color: Final[str] = "green"
    label_fontsize: Final[int] = 14
    xlabel: Final[str] = f"{xname} [{xunit}]"
    ylabel: Final[str] = f"{yname} [{yunit}]"
    axes.set_xlabel(xlabel, color=label_color, fontsize=label_fontsize)
    axes.set_ylabel(ylabel, color=label_color, fontsize=label_fontsize)

    axes.plot(
        earth_x,
        earth_t,
        label="Earth",
        color="blue",
        linewidth=linewidth,
        linestyle=linestyle,
    )
    axes.plot(
        traveler_x_first_leg,
        traveler_t_first_leg,
        label="First leg",
        color="orange",
        linewidth=linewidth,
        linestyle=linestyle,
    )
    axes.plot(
        traveler_x_second_leg,
        traveler_t_second_leg,
        label="Second leg",
        color="orange",
        linewidth=linewidth,
        linestyle=linestyle,
    )

    planet_label: Final[str] = "Planet"
    planet_color: Final[str] = "red"
    arrow_head_size: Final[int] = 7
    axes.plot(
        markers_x, markers_t, "s", label=planet_label, color=planet_color
    )  # s=square
    axes.annotate(
        planet_label,
        xy=(markers_x[0] - 0.15, markers_t[0] + 0.5),
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

    axes.set_xlim(0, x_max)
    axes.set_ylim(0, t_max)
    tick_granularity: Final[float] = 2.0
    axes.set_xticks(np.arange(0, x_max + tick_granularity, tick_granularity))
    axes.set_yticks(np.arange(0, t_max + tick_granularity, tick_granularity))
    # axes.minorticks_on()
    axes.set_aspect("equal")  # aspect ratio of 1:1

    axes.grid()
    # axes.legend()


if __name__ == "__main__":
    _main()
