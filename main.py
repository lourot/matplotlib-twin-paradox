from math import floor
from typing import Any, Final

from matplotlib.axes import Axes  # type: ignore
import matplotlib.pyplot as plt  # type: ignore
import numpy as np

from src import maths
from src import plotting


def _main() -> None:
    x_planet: Final[float] = 10.0
    traveler_speed: Final[float] = 0.5
    t_planet = x_planet / traveler_speed
    x_max: Final[float] = x_planet * 2.0
    t_max: Final[float] = 2 * t_planet

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

    color_earth: Final[str] = "blue"
    color_traveler: Final[str] = "orange"
    leg_width: Final[int] = 2
    leg_style: Final[str] = "-"
    plotting.draw_line(
        axes_earth,
        earth_line_x,
        earth_line_t,
        color_earth,
        leg_width,
        leg_style,
    )
    plotting.draw_line(
        axes_earth,
        traveler_x_first_leg,
        traveler_t_first_leg,
        color_traveler,
        leg_width,
        leg_style,
    )
    plotting.draw_line(
        axes_earth,
        traveler_x_second_leg,
        traveler_t_second_leg,
        color_traveler,
        leg_width,
        leg_style,
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
        t_planet * 1.2,
        plotting.darken(color_traveler),
    )

    _, traveler_age_on_planet = maths.lorentz_transform_reference_to_prime(
        x_planet,
        t_planet,
        traveler_speed,
    )
    age_step: Final[int] = 2
    for age in range(age_step, floor(traveler_age_on_planet), age_step):
        _draw_traveler_age(
            axes_earth,
            age,
            traveler_speed,
            plotting.darken(color_traveler),
        )
    _draw_traveler_age(
        axes_earth,
        traveler_age_on_planet,
        traveler_speed,
        plotting.darken(color_traveler),
        plotting.darken(color_traveler),
        plotting.darken(color_earth),
    )

    plt.show()


def _draw_traveler_age(
    axes: Axes,
    age: float,
    speed: float,
    color,
    marker_traveler_color=None,
    marker_earth_color=None,
) -> None:
    traveler_age_x, traveler_age_t = maths.lorentz_transform_prime_to_reference(
        0,
        age,
        speed,
    )
    simultaneous_x_on_earth: Final[float] = 0.0
    simultaneous_t_on_earth: Final[float] = traveler_age_t - traveler_age_x * speed
    plotting.draw_line(
        axes,
        [traveler_age_x, simultaneous_x_on_earth],
        [traveler_age_t, simultaneous_t_on_earth],
        color,
        1,
        ":",
    )
    axes.annotate(
        str(round(age, 1)),
        xy=(traveler_age_x, traveler_age_t),
        textcoords="offset fontsize",
        xytext=(0.6, -0.4),
        color=color,
    )

    if marker_traveler_color is not None:
        plotting.draw_marker(
            axes,
            traveler_age_x,
            traveler_age_t,
            marker_traveler_color,
        )
    if marker_earth_color is not None:
        plotting.draw_marker(
            axes,
            simultaneous_x_on_earth,
            simultaneous_t_on_earth,
            marker_earth_color,
        )


if __name__ == "__main__":
    _main()
