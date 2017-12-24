#import py4j.java_gateway
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/agents')
from py4j.java_gateway import JavaGateway, GatewayParameters
import random
import abstractAgent
import agentAction
import abstractUtilitySpace
import negotiationRule
import bid

class JavaAgent(abstractAgent.AbstractAgent):
    def __init__(self, setting_file_name:str, utility_space: abstractUtilitySpace.AbstractUtilitySpace,
                    negotiation_rule: negotiationRule.NegotiationRule, agent_id: int, agent_num: int, port:int):
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
        bid_str = ""
        if isinstance(agent_action, agentAction.Offer):
            for i, index in enumerate(agent_action.get_bid().get_indexes()):
                bid_str = bid_str + self.__utility_space.get_name(i, index+1) + ","
            bid_str = bid_str[:-1]
        self.gateway.receiveAction(str(agent_action.get_agent_id()), agent_action.__class__.__name__, bid_str)

    def send_action(self):
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
        return self.gateway.entry_point.getName()

    def receive_start_negotiation(self):
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


#class JavaAgent():
#
#    JAR_PATH = "./jar/testentrypoint.jar"
#    ENTRY_POINT_CLASS = "TestEntryPoint"
#
#    def __init__(self):
#        self._gateway = None
#        self._process = None
#        cmd = ["java", "-jar", self.JAR_PATH, self.ENTRY_POINT_CLASS]
#        if platform.system() == "Windows":
#            cmd[0] = "javaw"
#        self._process = subprocess.Popen(cmd)
#        print "JVM started: " + str(self._process.pid)
#        atexit.register(self.kill)
#        time.sleep(1)  # waiting for JVM start up
#        self._gateway = JavaGateway()
#
#    def getString(self):
#        return self._gateway.entry_point.getString()
#
#    def kill(self):
#        if self._gateway != None:
#            self._gateway.shutdown()
#            self._gateway = None
#        if self._process != None:
#            self._process.kill()
#            print "JVM killed: " + str(self._process.pid)
#            self._process = None
#
#
#def main():
#    jcon = JavaConnection()
#    print jcon.getString()
#    jcon.kill()
#
#if __name__ == "__main__":
#    main()
