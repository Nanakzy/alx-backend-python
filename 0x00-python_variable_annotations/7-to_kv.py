#!/usr/bin/env python3
"""
This module contains a function that returns
a tuple with a string and the square of
an int or float.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple with a string and the square of an int or float.

    Parameters:
    k (str): The string.
    v (Union[int, float]): The int or float to square.

    Returns:
    Tuple[str, float]: The tuple with the string &the square of the int/float.
    """
    return (k, float(v ** 2))
