from typing import Any, Final

import matplotlib.pyplot as plt  # type: ignore
import numpy as np

from src import maths
from src import plotting


def _main() -> None:
    x_planet: Final[float] = 10.0
    traveler_speed: Final[float] = 0.5
    x_max: Final[float] = x_planet * 2.0
    t_max: Final[float] = 2 * x_planet / traveler_speed

    margin: Final[float] = 0.5

    axes_earth, _ = plotting.draw_figure(
        x_max, t_max, "Earth", "Traveler", margin, "x", "t", "x'", "t'"
    )

    earth_line_x: Final[Any] = np.linspace(0, 0)
    earth_line_t: Final[Any] = np.linspace(0, t_max)
    traveler_x_first_leg: Final[Any] = np.linspace(0, x_planet)
    traveler_t_first_leg: Final[Any] = traveler_x_first_leg / traveler_speed
    traveler_x_second_leg: Final[Any] = np.linspace(x_planet, 0)
    traveler_t_second_leg: Final[Any] = (
        t_max / 2 + (x_planet - traveler_x_second_leg) / traveler_speed
    )

    color_traveler: Final[str] = "orange"
    plotting.draw_line(axes_earth, earth_line_x, earth_line_t, "blue")
    plotting.draw_line(
        axes_earth, traveler_x_first_leg, traveler_t_first_leg, color_traveler
    )
    plotting.draw_line(
        axes_earth, traveler_x_second_leg, traveler_t_second_leg, color_traveler
    )

    plotting.draw_marker(
        axes_earth,
        x_planet,
        x_planet / traveler_speed,
        plotting.darken(color_traveler),
    )

    plotting.draw_axis(
        axes_earth,
        "x'",
        0,
        0,
        x_max,
        x_max * traveler_speed,
        plotting.darken(color_traveler),
    )
    plotting.draw_axis(
        axes_earth,
        "t'",
        0,
        0,
        x_planet * 1.2,
        x_planet / traveler_speed * 1.2,
        plotting.darken(color_traveler),
    )

    ten_year_traveler_bday_x, ten_year_traveler_bday_t = (
        maths.lorentz_transform_prime_to_reference(0, 10, traveler_speed)
    )
    plotting.draw_marker(
        axes_earth,
        ten_year_traveler_bday_x,
        ten_year_traveler_bday_t,
        "red",
    )

    plt.show()


if __name__ == "__main__":
    _main()
