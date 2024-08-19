#!/usr/bin/env python3
import csv
from typing import List, Tuple


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

    def index_range(self, page: int, page_size: int) -> Tuple[int, int]:
        """
        returns a tuple of size two
        """
        return ((page - 1) * page_size, page * page_size)

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Return a specific page of the dataset based on page
        number and page size.
        """
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0

        start_index, end_index = self.index_range(page, page_size)
        if end_index > len(self.dataset()):
            return []
        return self.dataset()[start_index:end_index]
