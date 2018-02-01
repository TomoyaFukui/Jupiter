import random
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '..')
import abstractAgent
import agentAction
import abstractUtilitySpace
import negotiationRule
import bid

class LinearAgent0(abstractAgent.AbstractAgent):
    def __init__(self, utility_space: abstractUtilitySpace.AbstractUtilitySpace,
                    negotiation_rule: negotiationRule.NegotiationRule, agent_id: int, agent_num:int):
        self.__utility_space = utility_space
        self.__rule = negotiation_rule
        self.__agent_id = agent_id
        self.__random = random
        self.__random.seed(0)
        self.__issue_size_list = self.__utility_space.get_issue_size_list()
        self.__is_first_turn = True
        self.__opponent_action = None
        self.__opponent_bid = None

    def get_conssetion_value(self):
        return (1.0 - self.__rule.get_time_now())

    def receive_action(self, agentAction_: agentAction.AbstractAction):
        if isinstance(agentAction_, agentAction.Offer):
            self.__is_first_turn = False
            self.__opponent_action = agentAction_
            self.__opponent_bid = agentAction_.get_bid()

    def send_action(self):
        if self.__opponent_action is not None and \
            self.get_conssetion_value() < self.__utility_space.get_utility(self.__opponent_bid) \
                and self.__is_first_turn == False:
            return agentAction.Accept(self.__agent_id)

        bid_offer = self.__utility_space.get_bid_by_random_number()
        while self.__utility_space.get_utility(bid_offer) < self.get_conssetion_value():
            bid_offer = self.__utility_space.get_bid_by_random_number()
        return agentAction.Offer(self.__agent_id, bid_offer)

    def receive_start_negotiation(self):
        self.__is_first_turn = True
        self.__opponent_action = None
        self.__opponent_bid = None

    def get_name(self):
        return 'LinearAgent'
