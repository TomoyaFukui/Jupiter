# coding: utf-8
from abc import ABCMeta, abstractmethod
import abstractUtilitySpace
import negotiationRule
import agentAction

# 抽象クラス
class AbstractAgent(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, utility_space: abstractUtilitySpace.AbstractUtilitySpace,
                negotiation_rule: negotiationRule.NegotiationRule, agent_id:int, agent_num:int):
        pass
    @abstractmethod
    def receive_action(self, agent_action: agentAction.AbstractAction):
        pass
    @abstractmethod
    def send_action(self) -> agentAction.AbstractAction:
        pass
    @abstractmethod
    def get_name(self) -> str:
        pass

    def receive_start_negotiation(self):
        pass

    def receive_end_negotiation(self):
        pass


if __name__ == "__main__":
    pass
