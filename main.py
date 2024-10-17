from typing import Final

import matplotlib.pyplot as plt  # type: ignore

from src import earthframe
from src import plotting


def _main() -> None:
    x_planet: Final[float] = 10.0
    traveler_speed: Final[float] = 0.5
    t_planet: Final[float] = x_planet / traveler_speed
    t_reunion: Final[float] = 2 * t_planet
    x_max: Final[float] = x_planet * 2.0
    t_max: Final[float] = t_reunion + 4.0

    x_min: Final[float] = -2.0
    margin: Final[float] = 1.5

    axes_earth, _ = plotting.draw_figure(
        x_min,
        x_max,
        t_max,
        "Earth frame",
        "Traveler's frame",
        margin,
        "x",
        "t",
        "x'/x''",
        "t'/t''",
    )

    color_earth: Final[str] = "#0088ff"
    leg_width: Final[int] = 2
    leg_style: Final[str] = "-"
    age_step: Final[int] = 2
    earthframe.draw(
        axes_earth,
        x_max,
        t_max,
        t_reunion,
        x_planet,
        t_planet,
        traveler_speed,
        age_step,
        margin,
        color_earth,
        leg_width,
        leg_style,
    )

    plt.show()


if __name__ == "__main__":
    _main()
