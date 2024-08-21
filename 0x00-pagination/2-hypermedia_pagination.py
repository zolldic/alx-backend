#!/usr/bin/env python3
""" 2. Hypermedia pagination"""
import csv
import math
from typing import List, Dict


def index_range(page: int, page_size: int) -> tuple:
    """
        return a tuple of size two containing
            a start index and an end index corresponding
            to the range of indexes to return in a list for
            those particular pagination parameters.
    """
    return (((page - 1) * page_size), (page * page_size))


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
        """Retrieves a specific page of data from the dataset.
        """
        _data: List[List] = self.dataset()
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        start, end = index_range(page, page_size)
        return _data[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """method that returns a dictionary
            containing the following key-value pairs
        """
        _data: List[List] = self.get_page(page, page_size)
        _dataset: List[List] = self.dataset()
        total = math.ceil(len(_dataset) / page_size)

        return {
                "page_size": len(_data),
                "page": page,
                "data": _data,
                "next_page": None if page > total else page + 1,
                "prev_page": None if page < 1 else page - 1,
                "total_pages": total
                }
