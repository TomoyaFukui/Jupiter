from jupiter.simulator import abstractAgent
from jupiter.simulator import agentAction
from jupiter.simulator import abstractUtilitySpace
from jupiter.simulator import negotiationRule


class IntervalAgent(abstractAgent.AbstractAgent):
    def __init__(self,
                 utility_space: abstractUtilitySpace.AbstractUtilitySpace,
                 negotiation_rule: negotiationRule.NegotiationRule,
                 agent_id: int, agent_num: int):
        self.__utility_space = utility_space
        self.__rule = negotiation_rule
        self.__agent_id = agent_id
        self.__opponent_bid = None
        self.lower_max = 0.94
        self.upper_max = 1
        self.lower_min = 0.1
        self.upper_min = 0.4
        self.lower_curvature = 0.5
        self.upper_curvature = 0.9

    # Set time based upper and lower thresholds.
    def set_thresholds(self):
        time = self.__rule.get_time_now()
        self.lower_threshold = float(((1-time) * (1-time) * self.lower_max) + (2 * (1-time) * time * self.lower_curvature) + (time * time * self.lower_min))
        self.upper_threshold = float(((1-time) * (1-time) * self.upper_max) + (2 * (1-time) * time * self.upper_curvature) + (time * time * self.upper_min))

    def receive_action(self, agentAction_: agentAction.AbstractAction):
        if isinstance(agentAction_, agentAction.Offer):
            self.__opponent_bid = agentAction_.get_bid()

    def send_action(self):
        self.set_thresholds()

        if self.__opponent_bid is not None and self.upper_threshold <= self.__utility_space.get_utility(self.__opponent_bid):
            return agentAction.Accept(self.__agent_id)
        else:
            bid_offer = self.__utility_space.get_bid_between_concession_values(self.upper_threshold, self.lower_threshold)
            return agentAction.Offer(self.__agent_id, bid_offer)

    def receive_start_negotiation(self):
        self.__opponent_bid = None

    def receive_end_negotiation(self):
        pass

    def get_name(self):
        return 'IntervalAgent'
