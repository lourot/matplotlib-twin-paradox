from math import ceil
from typing import Final

import matplotlib.pyplot as plt  # type: ignore

from src import earthframe
from src import travelerframe
from src import plotting


def _main() -> None:
    x_planet: Final[float] = 10.0
    traveler_speed: Final[float] = 0.5
    t_planet: Final[float] = x_planet / traveler_speed
    t_reunion: Final[float] = 2 * t_planet
    t_max: Final[float] = t_reunion + 4.0

    margin: Final[float] = 1.5

    axes_earth, axes_traveler = plotting.draw_figure()

    color_earth: Final[str] = "#0088ff"
    color_traveler_first_leg: Final[str] = "orange"
    color_traveler_second_leg: Final[str] = "#aa00aa"
    leg_width: Final[int] = 2
    leg_style: Final[str] = "-"
    age_step: Final[int] = 2

    traveler_end_age, d_earth_from_planet = earthframe.draw(
        axes_earth,
        -2.0,
        x_planet * 2.0,
        t_max,
        t_reunion,
        x_planet,
        t_planet,
        traveler_speed,
        age_step,
        margin,
        color_traveler_first_leg,
        color_traveler_second_leg,
        color_earth,
        leg_width,
        leg_style,
    )

    travelerframe.draw(
        axes_traveler,
        x_planet * -1.0,
        2.0,
        ceil(traveler_end_age / 2.0 + 1.0) * 2,
        traveler_end_age,
        t_reunion,
        x_planet,
        traveler_speed,
        d_earth_from_planet,
        age_step,
        margin,
        color_traveler_first_leg,
        color_traveler_second_leg,
        color_earth,
        leg_width,
        leg_style,
    )

    plt.show()


if __name__ == "__main__":
    _main()
