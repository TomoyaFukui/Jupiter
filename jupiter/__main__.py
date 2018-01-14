# from jupiter import Jupiter
from jupiter.jupiter import Jupiter
from jupiter.negotiationRule import TypeOfNegotiation
import time
import itertools

time_list = []

def calc():
    name_list = ["LinearAgent", "BoulwareAgent", "ConcederAgent"]
    a = list(itertools.permutations(name_list, 3))
    for b in a:
        temp(b, 10)

def temp(name_list, roop_num=1):
    simu = Jupiter(TypeOfNegotiation.Turn, 180, 'Atlas3/triangularFight.xml',
       'Atlas3/triangularFight_util1.xml', 'Atlas3/triangularFight_util2.xml', 'Atlas3/triangularFight_util3.xml')
    # simu = Jupiter(negotiationRule.TypeOfNegotiation.Time, 10, 'domain/Terra/NewDomain.xml',
    #     'domain/Terra/NewDomain_util1.xml', 'domain/Terra/NewDomain_util2.xml', 'domain/Terra/NewDomain_util3.xml')
    # simu = Jupiter(negotiationRule.TypeOfNegotiation.Turn, 180, 'domain/myAgent/KDomain.xml',
    #     'domain/myAgent/KDomain_util1.xml', 'domain/myAgent/KDomain_util2.xml', 'domain/myAgent/KDomain_util3.xml')
    # simu = Jupiter(negotiationRule.TypeOfNegotiation.Turn, 180, 'domain/Terra/NewDomain.xml',
    #     'domain/Terra/NewDomain_util1.xml', 'domain/Terra/NewDomain_util2.xml', 'domain/Terra/NewDomain_util3.xml')
    for name in name_list:
        simu.set_agent(name)
        # simu.set_java_agent(name)
    for i in range(0, roop_num):
        start = time.time()
        simu.do_negotiation(is_printing=False, print_times=1)
        time_list.append(time.time() - start)

if __name__ == '__main__':
    start = time.time()
    # calc()
    # name_list = ["LinearAgent", "BoulwareAgent", "ConcederAgent"]
    # name_list = [25538, 25539]

    # name_list = ["LinearAgent", "BoulwareAgent", "ConcederAgent"]
    # temp(name_list)
    # simu = Jupiter(negotiationRule.TypeOfNegotiation.Time, 10, 'domain/Jobs/Jobs.xml',
    #    'domain/Jobs/Jobs_util1.xml', 'domain/Jobs/Jobs_util2.xml')
    # simu = Jupiter(TypeOfNegotiation.Turn, 100, 'domain/Atlas3/triangularFight.xml',
    #     'domain/Atlas3/triangularFight_util1.xml', 'domain/Atlas3/triangularFight_util2.xml', 'domain/Atlas3/triangularFight_util3.xml')
    # simu = Jupiter(TypeOfNegotiation.Turn, 100, 'domain/Atlas3/triangularFight.xml',
    #     'domain/Atlas3/triangularFight_util1.xml', 'domain/Atlas3/triangularFight_util2.xml')
    # simu = Jupiter(negotiationRule.TypeOfNegotiation.Turn, 100, 'domain/Farma/DomainTwF.xml',
    #     'domain/Farma/DomainTwF_util1.xml', 'domain/Farma/DomainTwF_util2.xml')
    # simu = Jupiter(negotiationRule.TypeOfNegotiation.Turn, 100, 'domain/parsAgent2/PEnergy.xml',
    #     'domain/parsAgent2/PEnergy_util1.xml', 'domain/parsAgent2/PEnergy_util2.xml')
    # simu = Jupiter(negotiationRule.TypeOfNegotiation.Turn, 100, 'domain/myAgent/KDomain.xml',
    #     'domain/myAgent/KDomain_util1.xml', 'domain/myAgent/KDomain_util2.xml')
    # simu = Jupiter(negotiationRule.TypeOfNegotiation.Turn, 100, 'domain/Terra/NewDomain.xml',
    #     'domain/Terra/NewDomain_util1.xml', 'domain/Terra/NewDomain_util2.xml', 'domain/Terra/NewDomain_util3.xml')
    simu = Jupiter(TypeOfNegotiation.Turn, 100, 'domain/Terra/NewDomain.xml',
        'domain/Terra/NewDomain_util1.xml', 'domain/Terra/NewDomain_util2.xml', 'domain/Terra/NewDomain_util3.xml')

    #simu = Jupiter(negotiationRule.TypeOfNegotiation.Turn, 100, 'domain/Domain2/Domain2.xml',
    #    'domain/Domain2/Domain2_util1.xml', 'domain/Domain2/Domain2_util2.xml', 'domain/Domain2/Domain2_util3.xml')
    # simu = Jupiter(negotiationRule.TypeOfNegotiation.Turn, 180, 'domain/Atlas3/triangularFight.xml',
    #    'domain/Atlas3/triangularFight_util1.xml', 'domain/Atlas3/triangularFight_util2.xml', 'domain/Atlas3/triangularFight_util3.xml')
    # simu = Jupiter(negotiationRule.TypeOfNegotiation.Turn, 180, 'domain/Atlas3/triangularFight.xml',
    #    'domain/Atlas3/triangularFight_util1.xml', 'domain/Atlas3/triangularFight_util2.xml')
    # simu = Jupiter(negotiationRule.TypeOfNegotiation.Turn, 1000, 'domain/myAgent/KDomain.xml',
    #    'domain/myAgent/KDomain_util1.xml', 'domain/myAgent/KDomain_util2.xml', 'domain/myAgent/KDomain_util3.xml')
    # simu = Jupiter(negotiationRule.TypeOfNegotiation.Turn, 180, 'domain/Atlas3/triangularFight.xml',
    #    'domain/Atlas3/triangularFight_util1.xml', 'domain/Atlas3/triangularFight_util2.xml')
    # simu = Jupiter(negotiationRule.TypeOfNegotiation.Turn, 180, 'domain/Terra/NewDomain.xml',
    #    'domain/Terra/NewDomain_util1.xml', 'domain/Terra/NewDomain_util2.xml')
    # simu.set_agent('LinearAgent')
    # simu.set_agent('LinearAgent0')
    # simu.set_agent('LinearAgent')
    # simu.set_agent('ConcederAgent')
    # simu.set_agent('BoulwareAgent')
    #simu.set_agent('LSTMAgent')
    # simu.set_agent('ImprovementAgent')
    # simu.set_java_agent(25535) #LinearAgent
    # simu.set_java_agent(25536) #ConcederAgent
    # simu.set_java_agent(25537) #BoulwareAgent
    # simu.set_java_agent(25538) #YXAgent
    # simu.set_java_agent(25539) #ParsCat
    # simu.set_java_agent(25540) #ParsCat
    # simu.set_java_agent(25541) #ParsCat

    simu.set_improvement_agent()
    simu.set_java_agent(25535)
    simu.set_java_agent(25536)
    #simu.test()
    # simu.set_save_pictures_Flag()
    #simu.set_notebook_flag()
    for i in range(0, 1000):
        simu.do_negotiation(is_printing=False, print_times=100)
    # simu.set_agent('ImprovementAgent')
    # simu.set_agent('LinearAgent')
    # simu.set_agent('ImprovementAgent')
    # for i in range(0, 1000):
    #     simu.do_negotiation(is_printing=False, print_times=100)
        # if i % 1000 == 0:
        #     simu.do_negotiation(is_printing=True, print_times=1)
        # else:
        # simu.do_negotiation(is_printing=False, print_times=1)
    simu.save_history_as_json()
    # for i in range(0, 3):
    #     simu.do_negotiation(is_printing=True, print_times=1)
    # a = list(itertools.permutations(name_list, 3))
    # for b in a:
    #     temp(b)

    # simu.do_negotiation(is_printing=False, print_times=1)
    # simu.display.show()

    # elapsed_time = time.time() - start
    # print(len(time_list))
    # print ("elapsed_time:{0}".format(sum(time_list)) + "[sec]", len(time_list))
    # for time in time_list:
    #     print(time)

    # jupiter.display_log('log/bids20171211-07:20:38.json', 1000)
    # jupiter.display_log('log/bids20171211-09:55:05.json', 500)
    # jupiter.display_log('log/bids20171218-01:46:21.json', 1000) %pars2 triangular
