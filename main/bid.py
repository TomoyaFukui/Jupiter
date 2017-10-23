# coding: utf-8
import copy
from typing import List

class Bid:
    def __init__(self, issue_size):
        self.__length = issue_size
        if isinstance(issue_size, int):
            self.__indexes = [0] * self.__length
        elif isinstance(issue_size, list):
            self.__indexes = issue_size
        else:
            self.__indexes = []

    def set_issue_by_list(self, index_list: List[int]):
        #for i, index in enumerate(index_list):
        #   self.__indexes[i] = index_list
        self.__indexes = index_list

    def set_issue_by_index(self, issue_index: int, item_index: int):
        self.__indexes[issue_index] = item_index

    def get_indexes(self):
        return copy.deepcopy(self.__indexes)
