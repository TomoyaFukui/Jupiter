from abc import ABCMeta, abstractmethod
import enum
from bid import Bid

# 抽象クラス
class AbstractUtilitySpace(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, file_name):
        pass

    @abstractmethod
    def get_reservation_value(self):
        pass

    @abstractmethod
    def get_discount_factor(self):
        pass

    @abstractmethod
    def get_utility(self, bid_: Bid) -> float:
        pass

    @abstractmethod
    def get_utility_discounted(self, bid_: Bid, time: float) -> float:
        pass

    @abstractmethod
    def get_file_name(self) -> str:
        pass


if __name__ == "__main__":
    pass
    #assert issubclass(Cat().__class__, Agent)
    #ssert isinstance(Cat(), Agent)
