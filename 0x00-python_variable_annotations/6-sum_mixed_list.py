#!/usr/bin/env python3
"""
Return as a float
"""
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    summation of a mixed list
    """

    return float(sum(mxd_lst))
