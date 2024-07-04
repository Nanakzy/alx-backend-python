#!/usr/bin/env python3
"""
This module contains a function that zooms into an array.
"""

from typing import List, Tuple

def zoom_array(lst: Tuple[int, ...], factor: int = 2) -> List[int]:
    """
    Zooms into an array.

    Parameters:
    lst (Tuple[int, ...]): The tuple to zoom into.
    factor (int): The zoom factor.

    Returns:
    List[int]: The zoomed-in list.
    """
    zoomed_in: List[int] = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in

array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
