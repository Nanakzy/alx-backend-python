#!/usr/bin/env python3
"""
This module contains a function that returns the first
element of a sequence if it exists, else None.
"""

from typing import Sequence, Any, Optional


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """
    Returns the first element of a sequence if it exists, else None.

    Parameters:
    lst (Sequence[Any]): The sequence.

    Returns:
    Optional[Any]: The first element if it exists, else None.
    """
    if lst:
        return lst[0]
    else:
        return None
