# coding: utf-8
from typing import List
import summrizationOfUtilitySpace
import negotiationRule
import display
import copy
import time
import agentAction
import comunicateJavaAgent
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/agents')
from linearAgent import*
from boulwareAgent import*
from concederAgent import*

class Jupiter:
    def __init__(self, negotiation_type, negotiation_time: int, setting_file_name, *file_names):
        if negotiation_type == negotiationRule.TypeOfNegotiation.Turn:
            self.__rule = negotiationRule.NegotiationRuleTurn(negotiation_time)
        elif negotiation_type == negotiationRule.TypeOfNegotiation.Time:
            self.__rule = negotiationRule.NegotiationRuleTime(negotiation_time)
        else:
            raise ValueError('negotiation type error in Jupiter init')
        self.__utilities = summrizationOfUtilitySpace.SummrizationOfUtilitySpace(file_names)
        self.__setting_file_name = setting_file_name
        self.__file_names = file_names
        self.__agent_list = []

        self.__display = display.Display(self.__utilities.get_utility_space(0).get_issue_size_list(),
                                            self.__utilities.get_weight_np_list(),
                                            self.__utilities.get_discount_factor_list(),
                                            self.__utilities.get_reservation_value_list())
        self.__action_list_list = []
        self.__get_agreement_list = []

    def set_agent(self, agent_name):
        instance = globals()[agent_name]
        self.__agent_list.append(instance(
                            self.__utilities.get_utility_space(len(self.__agent_list)),
                            self.__rule,
                            len(self.__agent_list), len(self.__file_names)))
        self.__display.set_agent_name(self.__agent_list[-1].get_name())

    def set_java_agent(self):
        self.__agent_list.append(comunicateJavaAgent.JavaAgent(
                                self.__setting_file_name,
                                self.__utilities.get_utility_space(len(self.__agent_list)),
                                self.__rule,
                                len(self.__agent_list), len(self.__file_names)))
        self.__display.set_agent_name(self.__agent_list[-1].get_name())

    def do_negotiation(self, is_printing: bool, print_times=10) -> bool:
        if self.__rule.get_type() == negotiationRule.TypeOfNegotiation.Turn:
            self.__rule._NegotiationRuleTurn__start_negotiation()
        elif self.__rule.get_type() == negotiationRule.TypeOfNegotiation.Time:
            self.__rule._NegotiationRuleTime__start_negotiation()
        else:
            print('unexpected invalid NegotiationRuleType')
            return False

        if is_printing:
            self.__display.plot_initialize()

        action_list = []
        self.__accept_num = 1
        can_proceed = True
        while can_proceed:
            for i in range(len(self.__agent_list)):
                #agentにアクションを起こさせて、時間内かつアクションが有効か検証する
                action = self.__agent_list[i].sendAction()
                if self.__rule.get_time_now() > 1.0:
                    return self.__end_negotiation(action_list, [False])
                elif not self.__is_valid_action(action, len(action_list)):
                    print('unexpected invalid action caused')
                    return False
                elif isinstance(action, agentAction.Accept):
                    action.set_bid(action_list[-1].get_bid())
                action.set_time_offered(self.__rule.get_time_now())
                action_list.append(action)
                if is_printing:
                    print(self.__rule.get_time_now() , self.__agent_list[action.get_agent_id()].get_name(),
                        action_list[-1].__class__.__name__, action_list[-1].get_bid().get_indexes())
                #各agentにアクションを知らせる
                for j in range(len(self.__agent_list)):
                    if i == j:
                        continue
                    self.__agent_list[j].receiveAction(action_list[-1])
                #ネゴシエーションの終了判定
                if self.__is_finished_negotiation(action):
                    if is_printing:
                        self.__display.update_end(action_list, [True, action])
                        print("parato distance:",self.__display.get_parato_distance(action))
                    return self.__end_negotiation(action_list, [True, action])
                elif self.__rule.get_type() == negotiationRule.TypeOfNegotiation.Time and \
                    not self.__rule._NegotiationRuleTime__proceed_negotiation():
                    return self.__end_negotiation(action_list, [False])
            if is_printing and len(action_list) % print_times == 0:
                self.__display.update(action_list)
            if self.__rule.get_type() == negotiationRule.TypeOfNegotiation.Turn:
                can_proceed = self.__rule._NegotiationRuleTurn__proceed_negotiation()
        return self.__end_negotiation(action_list, [False])

    def __is_valid_action(self, action: agentAction.AbstractAction, action_len: int) -> bool:
        if isinstance(action, agentAction.Accept) and action_len == 0:
            raise ValueError('first accept error in agent_id:',action.get_agent_id())
        elif isinstance(action, agentAction.Offer) and not self.__utilities.is_valid_bid(action.get_bid()):
            raise ValueError('bid index error in agent_id:',action.get_agent_id())
        return True

    def __is_finished_negotiation(self, action: agentAction.AbstractAction) -> bool:
        if isinstance(action, agentAction.EndNegotiation):
            return True
        elif isinstance(action, agentAction.Accept):
            self.__accept_num += 1
            if self.__accept_num == len(self.__agent_list):
                return True
        else:
            self.__accept_num = 1
        return False

    def __end_negotiation(self, actions, agreement) -> bool:
        self.__action_list_list.append(actions)
        self.__get_agreement_list.append(agreement)
        return True

    def display_points_end(self):
        if len(self.__agent_list) == 3:
            self.__display.display_plot3_update_end(self.__action_list_list[-1], self.__get_agreement_list[-1])
        elif len(self.__agent_list) == 2:
            self.__display.display_plot2_update_end(self.__action_list_list[-1], self.__get_agreement_list[-1])

    def display(self):
        self.__display.show()

    def set_save_pictures_Flag(self):
        self.__display.set_save_flag()


if __name__ == '__main__':
    #jupiter = Jupiter(negotiationRule.TypeOfNegotiation.Turn, 1000, 'domain/Jobs/Jobs.xml',
    #    'domain/Jobs/Jobs_util1.xml', 'domain/Jobs/Jobs_util2.xml')
    #jupiter = Jupiter(negotiationRule.TypeOfNegotiation.Turn, 100, 'domain/Domain2/Domain2.xml',
    #    'domain/Domain2/Domain2_util1.xml', 'domain/Domain2/Domain2_util2.xml')
    jupiter = Jupiter(negotiationRule.TypeOfNegotiation.Turn, 100, 'domain/Domain2/Domain2.xml',
        'domain/Domain2/Domain2_util1.xml', 'domain/Domain2/Domain2_util2.xml', 'domain/Domain2/Domain2_util3.xml')
    jupiter.set_agent('LinearAgent')
    #jupiter.set_agent('LinearAgent')
    jupiter.set_agent('ConcederAgent')
    jupiter.set_agent('BoulwareAgent')
    #jupiter.set_java_agent()

    #jupiter.test()
    #jupiter.set_save_pictures_Flag()
    jupiter.do_negotiation(is_printing=True, print_times=1)
    #jupiter.display()
    #jupiter.do_negotiation(is_printing=True, print_times=1)
    #jupiter.display()

    #jupiter.display_points_end()
    #jupiter.display_points()
    #jupiter.display_agreement_points()
