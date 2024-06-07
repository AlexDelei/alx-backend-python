#!/usr/bin/env python3
"""
Annotate the function below
"""
from typing import List, Iterable, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    An iterable sequence with a tuple in it
    """
    return [(i, len(i)) for i in lst]
