#!/usr/bin/env python3
"""
Simple helper function
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    returns tuple
    :param page:
    :param page_size:
    :return:
    """
    start = (page - 1) * page_size
    endi = start + page_size
    return start, endi
