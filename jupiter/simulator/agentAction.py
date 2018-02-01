from abc import ABCMeta, abstractmethod
from . import bid
# import bid


class AbstractAction(metaclass=ABCMeta):
    """
    自動交渉エージェントが起こすActionの抽象クラス
    各Actionはこのクラスを継承すること
    """
    @abstractmethod
    def __init__(self, agent_id: int):
        """
        :param int agent_id: 行動を起こしたエージェントに割り振られるid
        """
        self.__bid = None
        self.__time_offered = None

    def set_time_offered(self, time: float):
        """
        行動を起こした時間がsetされる

        :param float time: 行動を起こした時間
        """
        self.__time_offered = time

    def get_time_offered(self):
        """
        行動を起こした時間を返す

        :rtype: float
        :return: 行動を起こした時間
        """
        return self.__time_offered


class Accept(AbstractAction):
    """
    エージェントが起こすことのできる行動の1つ
    受容を表す．
    """
    def __init__(self, agent_id: int):
        """
        :param int agent_id: 行動を起こしたエージェントに割り振られたid
        """
        self.__agent_id = agent_id

    def set_bid(self, bid_: bid.Bid):
        """
        受容したbidがsetされる

        :param Bid bid_: 受容したBid
        """
        self.__bid = bid_

    def get_agent_id(self):
        """
        行動を起こしたエージェントのidを返す

        :rtype: int
        :return: 行動を起こしたエージェントのid
        """
        return self.__agent_id

    def get_bid(self):
        """
        受容したBidを返す

        :rtype: Bid
        :return: 受容した提案
        """
        return self.__bid


class Offer(AbstractAction):
    """
    エージェントが起こすことのできる行動の1つ
    提案を表す．
    """
    def __init__(self, agent_id, bid_: bid.Bid):
        """
        :param int agent_id: 行動を起こしたエージェントに割り振られたid
        """
        self.__agent_id = agent_id
        self.__bid = bid_

    def get_agent_id(self):
        """
        行動を起こしたエージェントのidを返す

        :rtype: int
        :return: 行動を起こしたエージェントのid
        """
        return self.__agent_id

    def get_bid(self):
        """
        提案を返す

        :rtype: Bid
        :return: エージェントの提案
        """
        return self.__bid


class EndNegotiation(AbstractAction):
    """
    エージェントが起こすことのできる行動の1つ
    交渉打ち切りを表す．
    """
    def __init__(self, agent_id: int):
        """
        :param int agent_id: 行動を起こしたエージェントに割り振られたid
        """
        self.__agent_id = agent_id

    def get_agent_id(self):
        """
        行動を起こしたエージェントのidを返す

        :rtype: int
        :return: 行動を起こしたエージェントのid
        """
        return self.__agent_id
