#!/usr/bin/env python3
"""
Return as a float
"""
from typing import Union


def sum_mixed_list(mxd_lst: list[Union[int, str]]) -> float:
    """
    summation of a mixed list
    """

    return float(sum(mxd_lst))
