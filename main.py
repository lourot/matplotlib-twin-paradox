from math import asin, cos, floor
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
        x_max, t_max, "Earth frame", "Traveler frame", margin, "x", "t", "x'", "t'/t''"
    )

    earth_line_x: Final[Any] = np.linspace(0, 0)
    earth_line_t: Final[Any] = np.linspace(0, t_max)
    color_earth: Final[str] = "#0088ff"
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

    color_light: Final[str] = "green"
    _draw_first_leg_explanation(
        axes_earth,
        x_max,
        margin,
        x_planet,
        t_planet,
        traveler_speed,
        color_earth,
        color_light,
        leg_width,
        leg_style,
    )

    _draw_second_leg_explanation(
        axes_earth,
        x_planet,
        t_planet,
        traveler_speed,
        leg_width,
        leg_style,
    )

    plt.show()


def _draw_first_leg_explanation(
    axes: Axes,
    x_max: float,
    margin: float,
    x_planet: float,
    t_planet: float,
    traveler_speed: float,
    color_earth: Any,
    color_light: Any,
    leg_width: int,
    leg_style: str,
) -> None:
    traveler_x_first_leg: Final[Any] = np.linspace(0, x_planet)
    traveler_t_first_leg: Final[Any] = traveler_x_first_leg / traveler_speed
    color_traveler: Final[str] = "orange"
    plotting.draw_line(
        axes,
        traveler_x_first_leg,
        traveler_t_first_leg,
        color_traveler,
        leg_width,
        leg_style,
    )

    plotting.draw_axis(
        axes,
        "x'",
        0,
        0,
        x_max,
        x_max * traveler_speed,
        plotting.darken(color_traveler),
    )
    plotting.draw_axis(
        axes,
        "t'",
        0,
        0,
        x_planet * 1.2,
        t_planet * 1.2,
        plotting.darken(color_traveler),
    )
    _draw_light_ray(
        axes,
        0,
        0,
        x_max * 1.2,
        x_max * 1.2,
        color_light,
    )
    axes.annotate(
        "light",
        xy=(x_planet, x_planet),
        textcoords="offset fontsize",
        xytext=(0, -1),
        color=plotting.darken(color_light),
    )

    _, traveler_age_on_planet = maths.lorentz_transform_reference_to_prime(
        x_planet,
        t_planet,
        traveler_speed,
    )
    age_step: Final[int] = 2
    for age in range(age_step, floor(traveler_age_on_planet), age_step):
        _draw_traveler_age(
            axes,
            margin,
            age,
            traveler_speed,
            plotting.darken(color_traveler),
            color_light,
            annotate_simultaneity=(age == t_planet / 2),
        )
    _draw_traveler_age(
        axes,
        margin,
        traveler_age_on_planet,
        traveler_speed,
        plotting.darken(color_traveler),
        color_light,
        plotting.darken(color_traveler),
        plotting.darken(color_earth),
    )


def _draw_second_leg_explanation(
    axes: Axes,
    x_planet: float,
    t_planet: float,
    traveler_speed: float,
    leg_width: int,
    leg_style: str,
) -> None:
    traveler_x_second_leg: Final[Any] = np.linspace(x_planet, 0)
    traveler_t_second_leg: Final[Any] = (
        t_planet + (x_planet - traveler_x_second_leg) / traveler_speed
    )
    color_traveler: Final[str] = "#aa00aa"
    plotting.draw_line(
        axes,
        traveler_x_second_leg,
        traveler_t_second_leg,
        color_traveler,
        leg_width,
        leg_style,
    )


def _draw_traveler_age(
    axes: Axes,
    margin: float,
    age: float,
    speed: float,
    color,
    color_light,
    marker_traveler_color=None,
    marker_earth_color=None,
    annotate_simultaneity=False,
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
    if annotate_simultaneity:
        sin_angle: Final[float] = speed
        angle_rad: Final[float] = asin(sin_angle)
        angle_deg: Final[float] = angle_rad * 180 / np.pi
        cos_angle: Final[float] = cos(angle_rad)
        margin_text: Final[float] = 4 * margin
        axes.text(
            traveler_age_x + cos_angle * margin_text,
            traveler_age_t + sin_angle * margin_text,
            "simultaneity in traveler's frame",
            color=color,
            rotation=angle_deg,
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

    _draw_light_ray(
        axes,
        traveler_age_x,
        traveler_age_t,
        0,
        traveler_age_t + traveler_age_x,
        color_light,
    )


def _draw_light_ray(
    axes: Axes,
    x_start: float,
    t_start: float,
    x_end: float,
    t_end: float,
    color: Any,
) -> None:
    plotting.draw_line(
        axes,
        [x_start, x_end],
        [t_start, t_end],
        color,
        1,
        ":",
    )


if __name__ == "__main__":
    _main()
