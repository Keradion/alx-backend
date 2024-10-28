#!/usr/bin/env python3
""" Implement simple pagination """
import math
import csv
from typing import List, Tuple


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


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset
    
    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Use index_range to find the correct indexes to paginate
        the dataset correctly and return the appropriate page
        of the dataset .
        """
        # Assert to verify page and page_size are int's and > 0
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        # Validating page and page_size according to the size of the dataset
        # Calling index_range function to get start and end indexes
        indexs = (index_range(page, page_size))
        start_index = indexs[0]
        end_index = indexs[1]
        # Performing Pagination returning a result
        dataset = self.dataset()
        return dataset[start_index:end_index]
