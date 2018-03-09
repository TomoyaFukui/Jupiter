from jupiter.simulator.jupiter import Jupiter
# from jupiter.simulator.jupiter import test
from jupiter.simulator import negotiationRule

# from jupiter import run
import site

from jupiter.agents import linearAgent
from jupiter.agents import concederAgent
import sys
import os
import site
import importlib

if __name__ == '__main__':
    # sys.path.append(os.path.join(site.getsitepackages()[-1], "jupiter-negotiation/agents"))
    # path = os.path.join(site.getsitepackages()[-1], "jupiter-negotiation/")
    path = site.getsitepackages()[-1]
    # path += "/Library/Python/3.6/site-packages/jupiter-negotiation/domain"
    path += "/jupiter-negotiation/domain"
    print(path)


    # jupiter = Jupiter(negotiationRule.TypeOfNegotiation.Turn, 100, path + '/Atlas3/triangularFight.xml',
    #      path +  '/Atlas3/triangularFight_util2.xml',
    #      path +  '/Atlas3/triangularFight_util1.xml')
    jupiter = Jupiter(negotiationRule.TypeOfNegotiation.Turn, 100, path + '/Jobs/Jobs.xml',
         path +  '/Jobs/Jobs_Util1.xml',
         path +  '/Jobs/Jobs_Util2.xml')
    jupiter.set_agent(linearAgent, 'LinearAgent')
    jupiter.set_agent(concederAgent, 'ConcederAgent')

    # jupiter.set_notebook_flag()
    jupiter.do_negotiation(is_printing=True, print_times=1)
    jupiter.display.show()
