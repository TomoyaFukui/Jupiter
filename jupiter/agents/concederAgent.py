from jupiter.simulator import abstractAgent
from jupiter.simulator import agentAction
from jupiter.simulator import abstractUtilitySpace
from jupiter.simulator import negotiationRule


class ConcederAgent(abstractAgent.AbstractAgent):
    def __init__(self, utility_space: abstractUtilitySpace.AbstractUtilitySpace,
                    negotiation_rule: negotiationRule.NegotiationRule, agent_id: int, agent_num:int):
        self.__utility_space = utility_space
        self.__rule = negotiation_rule
        self.__agent_id = agent_id
        self.__opponent_bid = None

    def get_conssetion_value(self):
        return (1.0 - pow(self.__rule.get_time_now(), 0.5))

    def receive_action(self, agentAction_: agentAction.AbstractAction):
        if isinstance(agentAction_, agentAction.Offer):
            self.__opponent_bid = agentAction_.get_bid()

    def send_action(self):
        if self.__opponent_bid is not None and \
           self.get_conssetion_value() < self.__utility_space.get_utility(self.__opponent_bid):
            return agentAction.Accept(self.__agent_id)

        bid_offer = self.__utility_space.get_bid_above_concession_value(self.get_conssetion_value())
        return agentAction.Offer(self.__agent_id, bid_offer)

    def receive_start_negotiation(self):
        self.__opponent_bid = None

    def receive_end_negotiation(self):
        pass

    def get_name(self):
        return 'ConsederAgent'
