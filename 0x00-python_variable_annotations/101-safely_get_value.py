#!/usr/bin/env python3
"""
This module contains a function that safely gets a value
from a dictionary.
"""

from typing import Mapping, Any, TypeVar, Union

T = TypeVar('T')


def safely_get_value(dct: Mapping[Any, Any], key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """
    Safely gets a value from a dictionary.

    Parameters:
    dct (Mapping[Any, Any]): The dictionary.
    key (Any): The key to look up.
    default (Union[T, None]): The default value if the key is not found.

    Returns:
    Union[Any, T]: The value associated with the key if found,
    else the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
