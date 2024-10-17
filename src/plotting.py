import colorsys
from typing import Final

import matplotlib.pyplot as plt  # type: ignore
from matplotlib.axes import Axes  # type: ignore
from matplotlib.colors import to_rgb  # type: ignore
import numpy as np


def draw_figure(
    xmax: float,
    ymax: float,
    title1: str,
    title2: str,
    margin: float,
    xname1: str,
    yname1: str,
    xname2: str,
    yname2: str,
) -> tuple[Axes, Axes]:
    _fig, (axes1, axes2) = plt.subplots(
        1, 2, sharey=True, figsize=(15, 12), layout="constrained", facecolor="lightgray"
    )

    _draw_axes(axes1, title1, xmax, ymax, margin, xname1, yname1)
    _draw_axes(axes2, title2, xmax, ymax, margin, xname2, yname2)

    return axes1, axes2


def draw_line(axes, data_x, data_y, color, width, style) -> None:
    axes.plot(
        data_x,
        data_y,
        # label="Earth",
        color=color,
        linewidth=width,
        linestyle=style,
    )


def draw_marker(axes, x, y, color, label: str | None = None, margin=0.0) -> None:
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


def draw_axis(axes, label, x_start, y_start, x_end, y_end, color) -> None:
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


def darken(color: str):
    # See https://stackoverflow.com/questions/37765197/darken-or-lighten-a-color-in-matplotlib
    h, l, s = colorsys.rgb_to_hls(*to_rgb(color))
    scale_l: Final[float] = 0.6
    return colorsys.hls_to_rgb(h, min(1, l * scale_l), s=s)


def _draw_axes(
    axes, title, xmax, ymax, margin, xname="x", yname="t", xunit="ly", yunit="y"
) -> None:
    axes.set_title(title)
    label_color: Final[str] = "black"
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
