from jupiter.simulator import abstractAgent
from jupiter.simulator import agentAction
from jupiter.simulator import abstractUtilitySpace
from jupiter.simulator import negotiationRule


class SampleAgent(abstractAgent.AbstractAgent):
    def __init__(self,
                 utility_space: abstractUtilitySpace.AbstractUtilitySpace,
                 negotiation_rule: negotiationRule.NegotiationRule,
                 agent_id: int, agent_num: int):
        self.__utility_space = utility_space
        self.__rule = negotiation_rule
        self.__agent_id = agent_id
        self.__opponent_bid = None

    def receive_action(self, agentAction_: agentAction.AbstractAction):
        if isinstance(agentAction_, agentAction.Offer):
            self.__opponent_bid = agentAction_.get_bid()

    def send_action(self):
        def get_conssetion_value():
            return (1.0 - self.__rule.get_time_now())

        if self.__opponent_bid is not None and \
           get_conssetion_value() < \
           self.__utility_space.get_utility(self.__opponent_bid):
            return agentAction.Accept(self.__agent_id)

        bid_offer = self.__utility_space.get_bid_above_concession_value(
            get_conssetion_value())
        return agentAction.Offer(self.__agent_id, bid_offer)

    def receive_start_negotiation(self):
        self.__opponent_bid = None

    def receive_end_negotiation(self):
        pass

    def get_name(self):
        return 'LinearAgent'
