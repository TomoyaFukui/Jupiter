import random
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '..')
import abstractAgent
import agentAction
import abstractUtilitySpace
import negotiationRule
import bid
#import tensorflow as tf
#import keras
import numpy as np
import json
import copy

class LSTMAgent(abstractAgent.AbstractAgent):
    def __init__(self, utility_space: abstractUtilitySpace.AbstractUtilitySpace,
                    negotiation_rule: negotiationRule.NegotiationRule, agent_id: int, agent_num:int):
        self.__utility_space = utility_space
        self.__rule = negotiation_rule
        self.__agent_id = agent_id
        self.__random = random
        self.__random.seed(0)
        self.__issue_size_list = self.__utility_space.get_issue_size_list()
        self.__is_first_turn = True

        self.__action_history0 = None
        self.__action_history1 = None

        self.__agent_num = agent_num
        self.__log_dict = {}
        self.__log_dict["data"] = []
        #self.__log_dict["in"] = []
        #self.__log_dict["out"] = []
        self.__log_index = 0

    def save_log(self):
        #in_li = [0] * (1 + self.__agent_num + sum(self.__issue_size_list))
        #in_li[0] = self.__action_history1.get_time_offered()
        #in_li[1 + self.__action_history1.get_agent_id()] = 1
        #index_sum = 1
        #for index, length in zip(self.__action_history1.get_bid().get_indexes(), self.__issue_size_list):
        #    in_li[self.__agent_num + index_sum + index] = 1
        #    index_sum += length

        out_li = [0] * (1 + self.__agent_num + sum(self.__issue_size_list))
        out_li[0] = self.__action_history0.get_time_offered()
        out_li[1 + self.__action_history0.get_agent_id()] = 1
        index_sum = 1
        for index, length in zip(self.__action_history0.get_bid().get_indexes(), self.__issue_size_list):
            out_li[self.__agent_num + index_sum + index] = 1
            index_sum += length
        self.__log_dict["data"].append(out_li)
        #self.__log_dict["in"].append(in_li)
        #print("in:", in_li)
        #print("out:", out_li)
        #print("save:", out_li)


    def get_conssetion_value(self):
        return (1.0 - pow(self.__rule.get_time_now(), 10))

    def receiveAction(self, agentAction_: agentAction.AbstractAction):
        if isinstance(agentAction_, agentAction.Offer):
            self.__is_first_turn = False
            self.__action_history1 = self.__action_history0
            self.__action_history0 = agentAction_
        if (isinstance(agentAction_, agentAction.Offer) or \
           isinstance(agentAction_, agentAction.Accept)) and \
           self.__action_history0 is not None:
           #self.__action_history0 is not None and \
           #self.__action_history1 is not None:
            self.save_log()

    def sendAction(self):
        if self.__action_history0 is not None and \
            self.get_conssetion_value() < self.__utility_space.get_utility(self.__action_history0.get_bid()) \
                and self.__is_first_turn == False:
            #self.get_conssetion_value() < self.__utility_space.get_utility_discounted(self.__opponent_bid, self.__opponent_action.get_time_offered()) \
            accept = agentAction.Accept(self.__agent_id)
            accept.set_bid(self.__action_history0.get_bid())
            accept.set_time_offered(self.__rule.get_time_now())
            self.receiveAction(accept)
            return accept

        bid_offer = bid.Bid(len(self.__issue_size_list))
        for i, size in enumerate(self.__issue_size_list):
            bid_offer.set_issue_by_index(i, self.__random.randint(0, size-1))
        while self.__utility_space.get_utility(bid_offer) < self.get_conssetion_value():
            for i, size in enumerate(self.__issue_size_list):
                bid_offer.set_issue_by_index(i, self.__random.randint(0, size-1))
        offer = agentAction.Offer(self.__agent_id, bid_offer)
        offer.set_time_offered(self.__rule.get_time_now())
        self.receiveAction(offer)
        return offer

    def receive_end_negotiation(self):
        #JSON データの書き込み
        f = open('bids.json', 'w')
        json.dump(self.__log_dict, f, indent=4)
        pass

    def get_name(self):
        return 'LSTMAgent'
