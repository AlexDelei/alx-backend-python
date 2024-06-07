#!/usr/bin/env python3
"""
Any type elements
"""
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Input elements are not known

    return Any type or none
    """
    if lst:
        return lst[0]
    else:
        return None
