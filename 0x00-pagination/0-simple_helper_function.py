#!/usr/bin/env python3
""" Simple helper function """
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """
       Returns a tuple of size two containing a start and
       end index corresponding to the range of indexes to return
       for those particluar pagination parameters.
    """
    # Computing start index of a dataset at a given page
    start_index = (page - 1) * (page_size)
    # Computing end index of a dataset at a given page
    end_index = start_index + (page_size)

    start_end_indexs = [start_index, end_index]

    return tuple(start_end_indexs)
