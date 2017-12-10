import random
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '..')
import abstractAgent
import agentAction
import abstractUtilitySpace
import negotiationRule
import bid

class BoulwareAgent(abstractAgent.AbstractAgent):
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
        return (1.0 - pow(self.__rule.get_time_now(), 10))

    def receiveAction(self, agentAction_: agentAction.AbstractAction):
        if isinstance(agentAction_, agentAction.Offer):
            self.__is_first_turn = False
            self.__opponent_action = agentAction_
            self.__opponent_bid = agentAction_.get_bid()

    def sendAction(self):
        if self.__opponent_action is not None and \
            self.get_conssetion_value() < self.__utility_space.get_utility(self.__opponent_bid) \
                and self.__is_first_turn == False:
            #self.get_conssetion_value() < self.__utility_space.get_utility_discounted(self.__opponent_bid, self.__opponent_action.get_time_offered()) \
            return agentAction.Accept(self.__agent_id)

        bid_offer = bid.Bid(len(self.__issue_size_list))
        for i, size in enumerate(self.__issue_size_list):
            bid_offer.set_issue_by_index(i, self.__random.randint(0, size-1))
        #while self.__utility_space.get_utility_discounted(bid_offer, self.__rule.get_time_now()) < self.get_conssetion_value():
        while self.__utility_space.get_utility(bid_offer) < self.get_conssetion_value():
            for i, size in enumerate(self.__issue_size_list):
                bid_offer.set_issue_by_index(i, self.__random.randint(0, size-1))
        return agentAction.Offer(self.__agent_id, bid_offer)

    def receive_start_negotiation(self):
        self.__is_first_turn = True
        self.__opponent_action = None
        self.__opponent_bid = None
        
    def get_name(self):
        return 'BoulwareAgent'
