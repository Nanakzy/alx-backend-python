#!/usr/bin/env python3
"""
This module contains a function that returns a multiplier function.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by the given multiplier.

    Parameters:
    multiplier (float): The multiplier.

    Returns:
    Callable[[float], float]: A function that multiplies a float
    by the multiplier.
    """
    def multiply_by(n: float) -> float:
        """
        Multiplies a float by the multiplier.

        Parameters:
        n (float): The float to multiply.

        Returns:
        float: The result of the multiplication.
        """
        return n * multiplier
    return multiply_by
