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
    x_planet: float,
    t_planet: float,
    traveler_speed: float,
    age_step: int,
    margin: float,
    color_traveler_first_leg: Any,
    color_traveler_second_leg: Any,
    color_earth: Any,
    leg_width: int,
    leg_style: str,
) -> tuple[float, float]:
    plotting.draw_axes(axes, "Earth frame", x_min, x_max, t_max, margin, "x", "t")

    _draw_earth_explanation(
        axes,
        x_max,
        t_max,
        t_reunion,
        x_planet,
        traveler_speed,
        color_earth,
        leg_width,
        leg_style,
    )

    traveler_age_on_planet, d_earth_from_planet = _draw_first_leg_explanation(
        axes,
        x_max,
        margin,
        x_planet,
        t_planet,
        traveler_speed,
        age_step,
        color_traveler_first_leg,
        color_earth,
        leg_width,
        leg_style,
    )

    _draw_second_leg_explanation(
        axes,
        margin,
        x_planet,
        t_planet,
        traveler_speed,
        age_step,
        color_traveler_second_leg,
        color_earth,
        leg_width,
        leg_style,
    )

    return 2.0 * traveler_age_on_planet, d_earth_from_planet


def _draw_earth_explanation(
    axes: Axes,
    x_max: float,
    t_max: float,
    t_reunion: float,
    x_planet: float,
    traveler_speed: float,
    color: Any,
    leg_width: int,
    leg_style: str,
) -> None:
    earth_line_x: Final[Any] = np.linspace(0, 0)
    earth_line_t: Final[Any] = np.linspace(0, t_reunion)
    plotting.draw_line(
        axes,
        earth_line_x,
        earth_line_t,
        color,
        leg_width,
        leg_style,
    )

    plotting.draw_axis(
        axes,
        "x",
        0,
        0,
        x_max,
        0,
        plotting.darken(color),
    )
    axes.annotate(
        f"d={x_planet} ly; v={traveler_speed}",
        xy=(x_planet, 0),
        textcoords="offset fontsize",
        xytext=(0, 0.5),
        color=plotting.darken(color),
    )

    plotting.draw_axis(
        axes,
        "t",
        0,
        0,
        0,
        t_max,
        plotting.darken(color),
    )


def _draw_first_leg_explanation(
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
) -> tuple[float, float]:
    traveler_x_first_leg: Final[Any] = np.linspace(0, x_planet)
    traveler_t_first_leg: Final[Any] = traveler_x_first_leg / traveler_speed
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
    length_step: Final[int] = 2
    for i in range(length_step, floor(x_max), length_step):
        x_length_mark, t_length_mark = maths.lorentz_transform_prime_to_reference(
            i,
            0,
            traveler_speed,
        )
        if x_length_mark > x_max:
            break
        plotting.draw_marker(
            axes,
            x_length_mark,
            t_length_mark,
            plotting.darken(color_traveler),
            margin=margin,
            shape="|",
        )
        axes.annotate(
            str(i),
            xy=(x_length_mark, t_length_mark),
            textcoords="offset fontsize",
            xytext=(0.6, -0.8),
            color=plotting.darken(color_traveler),
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

    color_light: Final[str] = "green"
    _, traveler_age_on_planet = maths.lorentz_transform_reference_to_prime(
        x_planet,
        t_planet,
        traveler_speed,
    )
    for age in range(0, floor(traveler_age_on_planet / 2), age_step):
        _draw_light_ray(
            axes,
            0,
            age,
            x_planet * 1.2,
            age + x_planet * 1.2,
            color_light,
        )
    axes.annotate(
        "light",
        xy=(x_planet, x_planet),
        textcoords="offset fontsize",
        xytext=(0, -1),
        color=plotting.darken(color_light),
    )

    for age in range(age_step, floor(traveler_age_on_planet), age_step):
        _draw_traveler_age(
            axes,
            True,
            x_planet,
            t_planet,
            margin,
            age,
            traveler_speed,
            plotting.darken(color_traveler),
            color_light=color_light if age < traveler_age_on_planet / 2 else None,
            annotate_simultaneity=(age == t_planet / 2),
        )
    t_end_first_leg_on_earth, simultaneity_angle_deg = _draw_traveler_age(
        axes,
        True,
        x_planet,
        t_planet,
        margin,
        traveler_age_on_planet,
        traveler_speed,
        plotting.darken(color_traveler),
        None,
        plotting.darken(color_traveler),
        plotting.darken(color_earth),
    )

    x1_earth_from_planet, _ = maths.lorentz_transform_reference_to_prime(
        0,
        t_end_first_leg_on_earth,
        traveler_speed,
    )
    d_earth_from_planet = -x1_earth_from_planet
    earth_speed_from_traveler = d_earth_from_planet / traveler_age_on_planet
    axes.annotate(
        f"d={round(d_earth_from_planet, 1)} ly; v={round(earth_speed_from_traveler, 2)}",
        xy=(0, t_end_first_leg_on_earth),
        textcoords="offset fontsize",
        xytext=(1, 1),
        color=plotting.darken(color_traveler),
        rotation=simultaneity_angle_deg + plotting.ROTATION_CORRECTION,
    )

    return traveler_age_on_planet, d_earth_from_planet


def _draw_second_leg_explanation(
    axes: Axes,
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
    traveler_x_second_leg: Final[Any] = np.linspace(x_planet, 0)
    traveler_t_second_leg: Final[Any] = (
        t_planet + (x_planet - traveler_x_second_leg) / traveler_speed
    )
    plotting.draw_line(
        axes,
        traveler_x_second_leg,
        traveler_t_second_leg,
        color_traveler,
        leg_width,
        leg_style,
    )

    x2_axis_x_offset_after_planet: Final[float] = x_planet
    x2_axis_t_offset_after_planet: Final[float] = x_planet * -traveler_speed
    plotting.draw_axis(
        axes,
        "x''",
        x_planet - x2_axis_x_offset_after_planet,
        t_planet - x2_axis_t_offset_after_planet,
        2 * x2_axis_x_offset_after_planet,
        2 * x2_axis_t_offset_after_planet,
        plotting.darken(color_traveler),
    )
    plotting.draw_axis(
        axes,
        "t''",
        x_planet,
        t_planet,
        x_planet * -1.2,
        t_planet * 1.2,
        plotting.darken(color_traveler),
    )

    plotting.draw_marker(
        axes,
        x_planet - x2_axis_x_offset_after_planet,
        t_planet - x2_axis_t_offset_after_planet,
        plotting.darken(color_earth),
    )

    _, traveler_age_on_planet = maths.lorentz_transform_reference_to_prime(
        x_planet,
        t_planet,
        traveler_speed,
    )
    for age in range(
        ceil(traveler_age_on_planet), ceil(traveler_age_on_planet * 2), age_step
    ):
        _draw_traveler_age(
            axes,
            False,
            x_planet,
            t_planet,
            margin,
            age,
            traveler_speed,
            plotting.darken(color_traveler),
        )


def _draw_traveler_age(
    axes: Axes,
    first_leg: bool,
    x_planet: float,
    t_planet: float,
    margin: float,
    age: float,
    speed: float,
    color,
    color_light=None,
    marker_traveler_color=None,
    marker_earth_color=None,
    annotate_simultaneity=False,
) -> tuple[float, float]:
    if first_leg:
        traveler_age_x, traveler_age_t = maths.lorentz_transform_prime_to_reference(
            0,
            age,
            speed,
        )
    else:
        _, traveler_age_on_planet = maths.lorentz_transform_reference_to_prime(
            x_planet,
            t_planet,
            speed,
        )
        traveler_age_x_from_planet, traveler_age_t_from_planet = (
            maths.lorentz_transform_prime_to_reference(
                0,
                age - traveler_age_on_planet,
                -speed,
            )
        )
        traveler_age_x = x_planet + traveler_age_x_from_planet
        traveler_age_t = t_planet + traveler_age_t_from_planet

    simultaneous_x_on_earth: Final[float] = 0.0
    simultaneous_t_on_earth: Final[float] = traveler_age_t + traveler_age_x * speed * (
        -1 if first_leg else 1
    )

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
    sin_angle: Final[float] = speed
    angle_rad: Final[float] = asin(sin_angle)
    angle_deg: Final[float] = angle_rad * 180 / np.pi
    cos_angle: Final[float] = cos(angle_rad)
    if annotate_simultaneity:
        margin_text: Final[float] = margin
        axes.text(
            traveler_age_x + cos_angle * margin_text,
            traveler_age_t + sin_angle * margin_text,
            "traveler's simultaneity",
            color=color,
            rotation=angle_deg + plotting.ROTATION_CORRECTION,
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

    if color_light is not None:
        _draw_light_ray(
            axes,
            traveler_age_x,
            traveler_age_t,
            0,
            traveler_age_t + traveler_age_x,
            color_light,
        )

    return simultaneous_t_on_earth, angle_deg


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
