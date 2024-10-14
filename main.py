import colorsys
from typing import Any, Final

import matplotlib.pyplot as plt
from matplotlib.colors import to_rgb
import numpy as np


def _main() -> None:
    _fig, (axes_earth, axes_traveler) = plt.subplots(
        1, 2, sharey=True, figsize=(10, 8), layout="constrained", facecolor="lightgray"
    )

    x_planet: Final[float] = 10.0
    traveler_speed: Final[float] = 0.5
    x_max: Final[float] = x_planet * 2.0
    t_max: Final[float] = 2 * x_planet / traveler_speed

    margin: Final[float] = 0.5

    _draw_axes(axes_earth, "Earth", x_max, t_max, margin)
    _draw_axes(axes_traveler, "Traveler", x_max, t_max, margin, "x'", "t'")

    earth_line_x: Final[Any] = np.linspace(0, 0)
    earth_line_t: Final[Any] = np.linspace(0, t_max)
    traveler_x_first_leg: Final[Any] = np.linspace(0, x_planet)
    traveler_t_first_leg: Final[Any] = traveler_x_first_leg / traveler_speed
    traveler_x_second_leg: Final[Any] = np.linspace(x_planet, 0)
    traveler_t_second_leg: Final[Any] = (
        t_max / 2 + (x_planet - traveler_x_second_leg) / traveler_speed
    )

    color_traveler: Final[str] = "orange"
    _draw_line(axes_earth, earth_line_x, earth_line_t, "blue")
    _draw_line(axes_earth, traveler_x_first_leg, traveler_t_first_leg, color_traveler)
    _draw_line(axes_earth, traveler_x_second_leg, traveler_t_second_leg, color_traveler)

    _draw_marker(
        axes_earth, x_planet, x_planet / traveler_speed, _darken(color_traveler)
    )

    _draw_axis(
        axes_earth, "x'", 0, 0, x_max, x_max * traveler_speed, _darken(color_traveler)
    )
    _draw_axis(
        axes_earth,
        "t'",
        0,
        0,
        x_planet * 1.2,
        x_planet / traveler_speed * 1.2,
        _darken(color_traveler),
    )

    plt.show()


def _draw_axes(
    axes, title, xmax, ymax, margin, xname="x", yname="t", xunit="ly", yunit="y"
) -> None:
    axes.set_title(title)
    label_color: Final[str] = "green"
    label_fontsize: Final[int] = 14
    xlabel: Final[str] = f"{xname} [{xunit}]"
    ylabel: Final[str] = f"{yname} [{yunit}]"
    axes.set_xlabel(xlabel, color=label_color, fontsize=label_fontsize)
    axes.set_ylabel(ylabel, color=label_color, fontsize=label_fontsize)

    axes.set_xlim(-margin, xmax + margin)
    axes.set_ylim(-margin, ymax + margin)
    tick_granularity: Final[float] = 2.0
    minor_tick_granularity: Final[float] = 1.0
    axes.set_xticks(np.arange(0, xmax + tick_granularity, tick_granularity))
    axes.set_yticks(np.arange(0, ymax + tick_granularity, tick_granularity))
    axes.set_xticks(
        np.arange(0, xmax + minor_tick_granularity, minor_tick_granularity), minor=True
    )
    axes.set_yticks(
        np.arange(0, ymax + minor_tick_granularity, minor_tick_granularity), minor=True
    )
    axes.set_aspect("equal")  # aspect ratio of 1:1

    axes.grid()
    # axes.legend()


def _draw_line(axes, data_x, data_y, color) -> None:
    legwidth: Final[int] = 2
    legstyle: Final[str] = "-"
    axes.plot(
        data_x,
        data_y,
        # label="Earth",
        color=color,
        linewidth=legwidth,
        linestyle=legstyle,
    )


def _draw_marker(axes, x, y, color, label: str | None = None, margin=0.0) -> None:
    arrow_head_size: Final[int] = 7
    axes.plot([x], [y], "s", label=label, color=color)  # s=square

    if label is not None:
        axes.annotate(
            label,
            xy=(x, y + margin),
            textcoords="offset fontsize",
            xytext=(-4, 5.2),
            color=color,
            arrowprops=dict(
                # arrowstyle="fancy",
                # relpos=(10, -10),
                color=color,
                width=1,
                headwidth=arrow_head_size,
                headlength=arrow_head_size,
                # shrink=0.5,
            ),
        )


def _draw_axis(axes, label, x_start, y_start, x_end, y_end, color) -> None:
    # See https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.arrow.html
    axes.arrow(
        x_start,
        y_start,
        x_end,
        y_end,
        length_includes_head=True,
        head_width=0.5,
        color=color,
        linestyle=":",
    )

    axes.annotate(
        label,
        xy=(x_end, y_end),
        textcoords="offset fontsize",
        xytext=(-0.5, 0.5),
        color=color,
    )


def _darken(color: str):
    # See https://stackoverflow.com/questions/37765197/darken-or-lighten-a-color-in-matplotlib
    h, l, s = colorsys.rgb_to_hls(*to_rgb(color))
    scale_l: Final[float] = 0.8
    return colorsys.hls_to_rgb(h, min(1, l * scale_l), s=s)


if __name__ == "__main__":
    _main()
