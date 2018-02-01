from py4j.java_gateway import JavaGateway, GatewayParameters
from . import abstractAgent
from . import agentAction
from . import abstractUtilitySpace
from . import negotiationRule
from . import bid
# import abstractAgent
# import agentAction
# import abstractUtilitySpace
# import negotiationRule
# import bid


class JavaAgent(abstractAgent.AbstractAgent):
    """
    Genius実装のJava言語エージェントと通信を行う．
    """
    def __init__(self, setting_file_name:str, utility_space: abstractUtilitySpace.AbstractUtilitySpace,
                    negotiation_rule: negotiationRule.NegotiationRule, agent_id: int, agent_num: int, port:int):
        """
        :param str setting_file_name: 効用ドメインファイルのパス
        :param AbstractUtilitySpace utility_space: 効用空間の情報が取得できる
        :param NegotiationRule negotiation_rule: 交渉の時間やタイプ，現在の正規化時間が取得できる
        :param int agent_id: 自分のエージェントに割り振られたid
        :param int agent_num: 交渉参加エージェントの数
        :param int port: 通信を行うポート番号
        """
        self.__utility_space = utility_space
        self.__rule = negotiation_rule
        self.__agent_id = agent_id
        self.__issue_size_list = self.__utility_space.get_issue_size_list()
        self.__opponent_bid = bid.Bid(len(self.__issue_size_list))

        # JVMへ接続
        self.gateway = JavaGateway(gateway_parameters=GatewayParameters(port=port))
        self.__setting_file_name = setting_file_name
        # Geniusのagentのinit
        self.__agent = self.gateway.entry_point
        self.__agent_num = agent_num
        self.__random_seed = 0
        self.receive_start_negotiation()

    def receive_action(self, agent_action: agentAction.AbstractAction):
        """
        他エージェントが行動を起こした場合に，その行動が通知される

        :param AbstractAction agent_action: 他のエージェントが起こした行動
        """
        bid_str = ""
        if isinstance(agent_action, agentAction.Offer):
            for i, index in enumerate(agent_action.get_bid().get_indexes()):
                bid_str = bid_str + self.__utility_space.get_name(i, index+1) + ","
            bid_str = bid_str[:-1]
        self.gateway.receiveAction(str(agent_action.get_agent_id()), agent_action.__class__.__name__, bid_str)

    def send_action(self):
        """
        自分のターンが回ってきた際に呼び出され，どの行動を起こすか返す

        :rtype: AbstractAction
        :return: Accept,Offer,EndNegotiationのいずれかを返す
        """
        message = self.gateway.entry_point.sendAction()
        massage_list = message.split(",")
        if massage_list[1].find("Offer") > -1:
            index_list = []
            for i, item in enumerate(massage_list[2:]):
                item = item[item.find("=")+1:]
                index_list.append(self.__utility_space.get_index(i, item)-1)
            return agentAction.Offer(self.__agent_id, bid.Bid(index_list))
        elif massage_list[1].find("Accept") > -1:
            return agentAction.Accept(self.__agent_id)
        elif massage_list[1].find("EndNegotiation") > -1:
            return agentAction.EndNegotiation(self.__agent_id)

    def get_name(self):
        """
        自分のエージェントの名前を返す．クラス名と同じにすることを推奨

        :rtype: str
        :return: エージェントの名前．クラス名と同じにすることを推奨
        """
        return self.gateway.entry_point.getName()

    def receive_start_negotiation(self):
        """提案応答ゲームを行う際に，提案応答ゲームが開始される際に呼び出される"""
        if self.__rule.get_type() == negotiationRule.TypeOfNegotiation.Turn:
            self.__agent.setAgent(self.__setting_file_name,
                                self.__utility_space.get_file_name(),
                                0, self.__rule.get_time_max(),
                                self.__random_seed, str(self.__agent_id), self.__agent_num)
        elif self.__rule.get_type() == negotiationRule.TypeOfNegotiation.Time:
            self.__agent.setAgent(self.__setting_file_name,
                                self.__utility_space.get_file_name(),
                                1, self.__rule.get_time_max(),
                                self.__random_seed, str(self.__agent_id), self.__agent_num)
