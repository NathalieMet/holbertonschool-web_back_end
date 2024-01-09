#!/usr/bin/env python3
"""Write a function named index_range that takes two integer arguments
page and page_size
The function should return a tuple of size two containing a start index and
an end index corresponding to the range of indexes to return in a list for
those particular pagination parameters.
"""

import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def index_range(self, page, page_size):
        """Write a function named index_range that takes two integer arguments
        page and page_size"""
        start_index = (page - 1) * page_size
        end_index = page * page_size
        return start_index, end_index

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
        """get_page"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        dataset = self.dataset()
        start_index, end_index = self.index_range(page, page_size)

        if start_index >= len(dataset):
            return []

        return dataset[start_index:end_index]
