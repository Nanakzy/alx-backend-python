#!/usr/bin/env python3
"""
This module contains a function that returns the sum of a list of floats.
"""


from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Sums a list of floats.

    Parameters:
    input_list (List[float]): The list of floats to sum.

    Returns:
    float: The sum of the list of floats.
    """
    return sum(input_list)
