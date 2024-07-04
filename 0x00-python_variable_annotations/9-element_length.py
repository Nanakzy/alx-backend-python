#!/usr/bin/env python3
"""
This module contains a function that returns the
length of elements in an iterable.
"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples with elements and their lengths.

    Parameters:
    lst (Iterable[Sequence]): The iterable of sequences.

    Returns:
    List[Tuple[Sequence, int]]: A list of tuples with
    sequences and their lengths.
    """
    return [(i, len(i)) for i in lst]
