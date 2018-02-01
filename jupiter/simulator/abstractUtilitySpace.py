from abc import ABCMeta, abstractmethod
from .bid import Bid
# from bid import Bid


class AbstractUtilitySpace(metaclass=ABCMeta):
    """
    効用情報の抽象クラス

    効用情報のクラスはこのクラスを継承すること
    """

    @abstractmethod
    def __init__(self, file_name):
        """:param str file_name: 交渉ドメインファイルのパス"""
        pass

    @abstractmethod
    def get_reservation_value(self):
        """
        留保価格を返す．

        :rtype: float
        :return: 留保価格
        """
        pass

    @abstractmethod
    def get_discount_factor(self):
        """
        割引効用を返す

        :rtype: float
        :return: 割引効用
        """
        pass

    @abstractmethod
    def get_utility(self, bid_: Bid) -> float:
        """
        効用値を返す

        :param Bid bid_: 効用値を計算するbid
        :rtype: float
        :return: 効用値
        """
        pass

    @abstractmethod
    def get_utility_discounted(self, bid_: Bid, time: float) -> float:
        """
        割引済み効用値を返す

        :param Bid bid_: 効用値を計算するbid
        :param float time: 交渉の経過時間(0<=time<=1)
        :rtype: float
        :return: 割引済み効用値
        """
        pass

    @abstractmethod
    def get_file_name(self) -> str:
        """
        交渉ドメインファイルのパスを返す

        :rtype: str
        :return: 交渉ドメインファイルのパス
        """
        pass
