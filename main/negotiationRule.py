# coding: utf-8
from enum import Enum, unique
from abc import ABCMeta, abstractmethod
import time

@unique
class TypeOfNegotiation(Enum):
    Turn = 1
    Time = 2

class NegotiationRule(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, time_max_ms: int):
        pass

    def __start_negotiation(self):
        pass

    def __proceed_negotiation(self):
        pass

    @abstractmethod
    def get_type(self):
        return self.__type

    @abstractmethod
    def get_time_now(self):
        return float(self.__time_now) / self.__max_time


class NegotiationRuleTurn(NegotiationRule):
    def __init__(self, time_max_turn: int):
        self.__type = TypeOfNegotiation.Turn
        self.__max_time = time_max_turn
        self.__time_now = 0
        pass

    def __start_negotiation(self):
        self.__time_now = 1

    def __proceed_negotiation(self):
        self.__time_now += 1
        if self.__time_now <= self.__max_time:
            return True
        else:
             return False

    def get_time_max(self):
        return self.__max_time

    def get_time_now(self):
        return float(self.__time_now - 1) / self.__max_time

    def get_type(self):
        return self.__type

class NegotiationRuleTime(NegotiationRule):
    def __init__(self, time_max_s: time.time()):
        self.__type = TypeOfNegotiation.Time
        self.__max_time = time_max_s
        self.__time_now = 0
        pass

    def __start_negotiation(self):
        self.__time_begining = time.time()

    def __proceed_negotiation(self):
        self.__time_now = time.time() - self.__time_begining
        if self.__time_now <= self.__max_time:
            return True
        else:
             return False

    def get_time_max(self):
        return self.__max_time

    def get_time_now(self):
        self.__time_now = time.time() - self.__time_begining
        return float(self.__time_now) / self.__max_time
        #return self.__time_now

    def get_type(self):
        return self.__type
