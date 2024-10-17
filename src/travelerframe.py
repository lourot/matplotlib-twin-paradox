from math import asin, ceil, cos, floor
from typing import Any, Final

from matplotlib.axes import Axes  # type: ignore

import numpy as np

from src import maths
from src import plotting


def draw(
    axes: Axes,
    x_min: float,
    x_max: float,
    t_max: float,
    t_reunion: float,
    traveler_end_age: float,
    traveler_speed: float,
    age_step: int,
    margin: float,
    color_traveler_first_leg: Any,
    color_traveler_second_leg: Any,
    color_earth: Any,
    leg_width: int,
    leg_style: str,
) -> None:
    plotting.draw_axes(
        axes, "Traveler's frames", x_min, x_max, t_max, margin, "x'/x''", "t'/t''"
    )

    _draw_traveler_explanation(
        axes,
        x_min,
        x_max,
        t_max,
        traveler_end_age,
        color_traveler_first_leg,
        color_traveler_second_leg,
        leg_width,
        leg_style,
    )


def _draw_traveler_explanation(
    axes: Axes,
    x_min: float,
    x_max: float,
    t_max: float,
    traveler_end_age: float,
    color_traveler_first_leg: Any,
    color_traveler_second_leg: Any,
    leg_width: int,
    leg_style: str,
) -> None:
    first_leg_x: Final[Any] = np.linspace(0, 0)
    first_leg_t: Final[Any] = np.linspace(0, traveler_end_age / 2.0)
    plotting.draw_line(
        axes,
        first_leg_x,
        first_leg_t,
        color_traveler_first_leg,
        leg_width,
        leg_style,
    )
    plotting.draw_marker(
        axes,
        0,
        traveler_end_age / 2.0,
        plotting.darken(color_traveler_first_leg),
    )

    second_leg_x: Final[Any] = np.linspace(0, 0)
    second_leg_t: Final[Any] = np.linspace(traveler_end_age / 2.0, traveler_end_age)
    plotting.draw_line(
        axes,
        second_leg_x,
        second_leg_t,
        color_traveler_second_leg,
        leg_width,
        leg_style,
    )

    plotting.draw_axis(
        axes,
        "x'",
        x_min,
        0,
        x_max - x_min,
        0,
        plotting.darken(color_traveler_first_leg),
    )
    plotting.draw_axis(
        axes,
        "x''",
        x_min,
        traveler_end_age / 2.0,
        x_max - x_min,
        0,
        plotting.darken(color_traveler_second_leg),
    )
    plotting.draw_axis(
        axes,
        "t'/t''",
        0,
        0,
        0,
        t_max,
        plotting.darken(color_traveler_second_leg),
    )


def _draw_earth_first_part_explanation(
    axes: Axes,
    x_max: float,
    margin: float,
    x_planet: float,
    t_planet: float,
    traveler_speed: float,
    age_step: int,
    color_traveler: Any,
    color_earth: Any,
    leg_width: int,
    leg_style: str,
) -> None:
    pass
    # x2_earth, t2_earth = maths.lorentz_transform_prime_to_reference(
    #     x_planet, t_planet, traveler_speed
    # )

    # x_data: Final[Any] = np.linspace(0, x_planet)
    # t_data: Final[Any] = traveler_x_first_leg / traveler_speed
    # plotting.draw_line(
    #     axes,
    #     traveler_x_first_leg,
    #     traveler_t_first_leg,
    #     color_traveler,
    #     leg_width,
    #     leg_style,
    # )
