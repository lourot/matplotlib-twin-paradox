from math import sqrt
from typing import Tuple


def lorentz_transform_prime_to_reference(
    x2: float, t2: float, v: float
) -> Tuple[float, float]:
    """
    Transforms (x', t') back to (x, t) in the reference frame, doing a Lorentz transformation.

    Units:
    * x, x': light-T (T being a time unit, like seconds or years)
    * t, t': T
    * v: no unit, fraction of the speed of light
    """
    gamma = 1 / sqrt(1 - v**2)
    t1 = gamma * (t2 + v * x2)
    x1 = gamma * (x2 + v * t2)
    return x1, t1
