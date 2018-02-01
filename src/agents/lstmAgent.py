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
import seq2seq

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
        self.__log_index = 0

        self.__predictor = seq2seq.SEQ2SEQ()
        self.__predictor.init_model(30, sum(self.__issue_size_list), len(self.__issue_size_list))
        self.__predictor.create_model()
        self.__predictor.load()

        self.__time_list = []

    def append_log(self):
        out_li = [0] * (1 + self.__agent_num + sum(self.__issue_size_list))
        out_li[0] = self.__action_history0.get_time_offered()
        out_li[1 + self.__action_history0.get_agent_id()] = 1
        index_sum = 1
        for index, length in zip(self.__action_history0.get_bid().get_indexes(), self.__issue_size_list):
            out_li[self.__agent_num + index_sum + index] = 1
            index_sum += length
        self.__log_dict["data"].append(out_li)
        #print("in:", in_li)
        #print("out:", out_li)
        #print("save:", out_li)

    def is_valid_index_list(self, index_list:list):
        for index, size in zip(index_list, self.__issue_size_list):
            if index < 0 or size <= index:
                return False
        return True

    def get_conssetion_value(self):
        # return (1.0 - pow(self.__rule.get_time_now(), 10) - 0.1)
        if self.__time_list == []:
            self.__time_list.append(self.__rule.get_time_now())
        else:
            self.__time_list.append(self.__rule.get_time_now() - sum(self.__time_list))
#
        if len(self.__log_dict["data"]) < 30:
            return (1.0 - pow(self.__rule.get_time_now(), 10) - 0.1)

        data = self.__log_dict["data"][-30:]
        data = np.array([i[3:] for i in data], np.int8).reshape(1, 30, sum(self.__issue_size_list))
        predict = self.__predictor.predict(data, self.__issue_size_list, 300)[0]

        utility_list = [self.__utility_space.get_utility(bid.Bid(index_list)) *
                            pow(self.__utility_space.get_discount_factor(), self.__time_list[-1]*i%2)
                            for i, index_list in enumerate(predict)
                            if i % self.__agent_num != 0 and self.is_valid_index_list(index_list)]
        #print(sum(self.__time_list))
        return max(utility_list)

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
            self.append_log()

    def sendAction(self):
        conssetion_value = self.get_conssetion_value()
        if self.__action_history0 is not None and \
            conssetion_value < self.__utility_space.get_utility(self.__action_history0.get_bid()) \
                and self.__is_first_turn == False:
            accept = agentAction.Accept(self.__agent_id)
            accept.set_bid(self.__action_history0.get_bid())
            accept.set_time_offered(self.__rule.get_time_now())
            self.receiveAction(accept)
            return accept

        bid_offer = bid.Bid(len(self.__issue_size_list))
        for i, size in enumerate(self.__issue_size_list):
            bid_offer.set_issue_by_index(i, self.__random.randint(0, size-1))
        while self.__utility_space.get_utility(bid_offer) < conssetion_value:
            for i, size in enumerate(self.__issue_size_list):
                bid_offer.set_issue_by_index(i, self.__random.randint(0, size-1))
        offer = agentAction.Offer(self.__agent_id, bid_offer)
        offer.set_time_offered(self.__rule.get_time_now())
        self.receiveAction(offer)
        return offer

    def receive_end_negotiation(self):
        #JSON データの書き込み
        self.game_num = 1
        f = open('bids' + str(self.game_num) + ".json", 'w')
        json.dump(self.__log_dict, f, indent=4)
        pass

    def get_name(self):
        return 'LSTMAgent'
