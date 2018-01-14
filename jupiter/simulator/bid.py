import copy
from typing import List


class Bid:
    """
    自動交渉エージェント間で交換されるBid
    Offer，Acceptクラスを作成する際に用いる
    """
    def __init__(self, issue_size):
        """
        :param List issue_size1: 提案したい内容のindexのリスト
        :param int issue_size2: 交渉ドメインの各論点の数
        """
        if isinstance(issue_size, int):
            self.__indexes = [0] * issue_size
        elif isinstance(issue_size, list):
            self.__indexes = issue_size
        else:
            self.__indexes = []

    def set_issue_by_list(self, index_list: List[int]):
        """
        listオブジェクトにより提案Bidをsetする

        :param list issue_size: 提案したい内容のindexのリスト
        """
        self.__indexes = index_list

    def set_issue_by_index(self, issue_index: int, item_index: int):
        """
        論点のindexを指定して，その論点に指定したindexをsetする

        :param int issue_index: setしたい論点のindex
        :param int item_index: setしたいitemのindex
        """
        self.__indexes[issue_index] = item_index

    def get_indexes(self):
        """
        行動を起こした時間を返す

        :rtype: float
        :return: 行動を起こした時間
        """
        return copy.deepcopy(self.__indexes)
