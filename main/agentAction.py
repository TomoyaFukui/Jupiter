# coding: utf-8
from abc import ABCMeta, abstractmethod
from enum import Enum, unique
import time
import copy
import bid

class AbstractAction(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, agent_id: int):
        self.__bid = None
        self.__time_offered = None

    def set_time_offered(self, time: float):
        self.__time_offered = time
        return self

    def get_time_offered(self):
        return self.__time_offered

class Accept(AbstractAction):
    def __init__(self, agent_id: int):
        self.__agent_id = agent_id

    def set_bid(self, bid_: bid.Bid):
        self.__bid = bid_

    def get_agent_id(self):
        return self.__agent_id

    def get_bid(self):
        return self.__bid

class Offer(AbstractAction):
    def __init__(self, agent_id, bid_: bid.Bid):
        self.__agent_id = agent_id
        self.__bid = bid_

    def get_agent_id(self):
        return self.__agent_id

    def get_bid(self):
        return self.__bid

class EndNegotiation(AbstractAction):
    def __init__(self, agent_id: int):
        self.__agent_id = agent_id

    def get_agent_id(self):
        return self.__agent_id

if __name__ == "__main__":
    pass
