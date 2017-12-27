import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/agents')
import numpy as np
import random
import copy
import abstractUtilitySpace
import readUtilityFile
import bid
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/cython')
import make_bid
import numpy.random as rand

class UtilitySpace(abstractUtilitySpace.AbstractUtilitySpace):
    def __init__(self, file_name: str):
        self.__set_utility_space(file_name)
        pass

    def __set_utility_space(self, file_name: str):
        self.__file_name = file_name
        all_records = readUtilityFile.ReadXML().create_utility(file_name)
        self.__discout_factor = (float)(all_records[0]['discount_factor'])
        self.__reservation_value = (float)(all_records[1]['reservation'])

        issue_size = all_records[2]

        self.__name2index_list = []
        self.__index2name_list = []
        for i in range(issue_size):
            name = all_records[i+3+issue_size]["name"]
            name2index = {v:int(k) for k, v in all_records[i+3+issue_size][name].items()}
            self.__name2index_list.append(name2index)
            index2name = {int(k):v for k, v in all_records[i+3+issue_size][name].items()}
            self.__index2name_list.append(index2name)

        self.__weight_list = []
        for i in range(issue_size):
            for j in range(issue_size - i):
                j_changed = i + j + 3
                if i+1 == int(all_records[j_changed]["index"]):
                    self.__weight_list.append(float((all_records[j_changed])["weight"]))
                    break
        self.__issue_list = []
        self.__issue_size_list = []
        for i in range(issue_size):
            for j in range(issue_size - i):
                j_changed = i + j + 3 + issue_size
                if i+1 == int(all_records[j_changed]["index"]):
                    self.__issue_list.append(all_records[j_changed])
                    self.__issue_size_list.append(len((all_records[j_changed])["issue"]))
                    break
        self.__evaluations_np_list = self.__calc_weight()
        self.__random = random
        self.__random.seed(0)


    def __calc_weight(self):
        evaluations = []
        evaluations_np_list = []
        for i, issue_dict in enumerate(self.__issue_list):
            for j in range(self.__issue_size_list[i]):
                #print(issue_dict["issue"][str(j+1)])
                evaluations.append(float(issue_dict["issue"][str(j+1)]))
            #evaluations_list.append(evaluations)
            evaluations_np_list.append(np.array(evaluations, np.float64))
            evaluations_np_list[i] = evaluations_np_list[i] / np.max(evaluations_np_list[i])
            evaluations_np_list[i] *= self.__weight_list[i]
            evaluations = []

        #evaluations_np_list.append(np.array(evaluations_list[i], np.float64))
        #for i in range(len(self.__issue_size_list)):
            #evaluations_np[i] = evaluations_np[i] / np.max(evaluations_np[i])
        return evaluations_np_list

    def get_file_name(self):
        return self.__file_name

    def get_index(self, issue_number, item_name):
        return self.__name2index_list[issue_number][item_name]

    def get_name(self, issue_number, item_index):
        return self.__index2name_list[issue_number][item_index]

    def get_reservation_value(self):
        return self.__reservation_value

    def get_discount_reservation_value(self, time):
        return self.__reservation_value * pow(self.__discout_factor, time)

    def get_discount_factor(self):
        return self.__discout_factor

    def get_weight_np_list(self):
        return copy.deepcopy(self.__evaluations_np_list)

    def get_issue_size_list(self):
        return copy.deepcopy(self.__issue_size_list)

    def get_utility(self, bid_: bid.Bid) -> float:
        value = 0.0
        for i, index in enumerate(bid_.get_indexes()):
            value += self.__evaluations_np_list[i][index]
        return float(value)

    def get_bid_above_concession_value(self, concession_value, make_num=1000):
        # cython_code.
        random_number_list = []
        for size in self.__issue_size_list:
            random_number_list.append(rand.randint(0, size, make_num).tolist())
        bid_index_list = make_bid.get_bid_above_concession_value(self.__evaluations_np_list, random_number_list, concession_value)
        return bid.Bid(bid_index_list)

    def get_utility_discounted(self, bid_: bid.Bid, time: float) -> float:
        value = self.get_utility(bid_)
        value *= pow(self.__discout_factor, time)
        return value

    def get_bid_by_random_number(self) -> bid.Bid:
        bid_ret = bid.Bid(len(self.__issue_size_list))
        for i, size in enumerate(self.__issue_size_list):
            bid_ret.set_issue_by_index(i, self.__random.randint(0, size-1))
        return bid_ret

    def is_valid_bid(self, bid_: bid.Bid) -> bool:
        for index, size in zip(bid_.get_indexes(), self.__issue_size_list):
            if index < 0 or size <= index:
                return False
        return True

    def print_all(self):
        print('reservation_value:' + (str)(self.__reservation_value))
        print('discount_factor:' + (str)(self.__discout_factor))
        print('issue_size:' + (str)(self.__issue_size_list))
        print('evaluation', self.__evaluations_np_list)


if __name__ == '__main__':
    #utility_space = UtilitySpace('Domain2/Domain2_util1.xml')
    utility_space = UtilitySpace('Jobs/Jobs_util1.xml')
    utility_space.print_all()
