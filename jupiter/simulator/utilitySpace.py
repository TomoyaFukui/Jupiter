# import sys
# import os
import numpy as np
import numpy.random as rand
import random
import copy
from . import abstractUtilitySpace
from . import readUtilityFile
from . import bid
from .cython import make_bid
# import abstractUtilitySpace
# import readUtilityFile
# import bid
# sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/cython')
# from cython import make_bid


class UtilitySpace(abstractUtilitySpace.AbstractUtilitySpace):
    """
    線形効用空間のクラス
    """
    def __init__(self, file_name: str):
        '''
        :param str file_name: 効用ドメインファイルのパス
        '''

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
        """
        交渉ドメインファイルのパスを返す

        :rtype: str
        :return: 交渉ドメインファイルのパス
        """
        return self.__file_name

    def get_index(self, issue_number, item_name):
        '''
        指定された論点における，itemのindexを返す．

        :param int issue_number: 調べたい論点のindex
        :param str item_name: indexを知りたいitem
        :rtype: int
        :return: 指定された論点における，itemのindex
        '''
        return self.__name2index_list[issue_number][item_name]

    def get_name(self, issue_number, item_index):
        '''
        指定された論点におけるindexのitemを返す.

        :param int issue_number: 調べたい論点のindex
        :param int item_index: itemを知りたいindex
        :rtype: str
        :return: 指定された論点における，indexのitem
        '''
        return self.__index2name_list[issue_number][item_index]

    def get_reservation_value(self):
        """
        留保価格を返す．

        :rtype: float
        :return: 留保価格
        """
        return self.__reservation_value

    def get_discount_reservation_value(self, time):
        """
        割引効用込みの留保価格を返す．

        :param float time: 交渉の正規化された経過時間
        :rtype: float
        :return: 割引済みの留保価格
        """
        return self.__reservation_value * pow(self.__discout_factor, time)

    def get_discount_factor(self):
        """
        割引効用を返す

        :rtype: float
        :return: 割引効用
        """
        return self.__discout_factor

    def get_weight_np_list(self):
        """
        効用値を返す

        :rtype: np.array
        :return: 効用値
        """
        return copy.deepcopy(self.__evaluations_np_list)

    def get_issue_size_list(self):
        """
        各論点の大きさのリストを返す

        :rtype: List[int]
        :return: 各論点の大きさのリスト
        """
        return copy.deepcopy(self.__issue_size_list)

    def get_utility(self, bid_: bid.Bid) -> float:
        """
        効用値を返す

        :param Bid bid_: 効用値を計算するbid
        :rtype: float
        :return: 効用値
        """
        value = 0.0
        for i, index in enumerate(bid_.get_indexes()):
            value += self.__evaluations_np_list[i][index]
        return float(value)

    def get_bid_above_concession_value(self, concession_value, make_num=1000):
        '''
        乱数によりBid生成する

        :rtype: Bid
        :return: 乱数により生成されたBid
        '''
        # cython_code.
        random_number_list = []
        for size in self.__issue_size_list:
            random_number_list.append(rand.randint(0, size, make_num).tolist())
        bid_index_list = make_bid.get_bid_above_concession_value(self.__evaluations_np_list, random_number_list, concession_value)
        return bid.Bid(bid_index_list)

    def get_utility_discounted(self, bid_: bid.Bid, time: float) -> float:
        """
        割引済みの効用値を返す

        :param Bid bid_: 効用値を計算したいBid
        :param float time: 正規化された交渉の経過時間
        :rtype: float
        :return: 割引済みの効用値
        """
        value = self.get_utility(bid_)
        value *= pow(self.__discout_factor, time)
        return value

    def get_bid_by_random_number(self) -> bid.Bid:
        '''
        乱数によりBid生成する

        :rtype: Bid
        :return: 乱数により生成されたBid
        '''
        bid_ret = bid.Bid(len(self.__issue_size_list))
        for i, size in enumerate(self.__issue_size_list):
            bid_ret.set_issue_by_index(i, self.__random.randint(0, size-1))
        return bid_ret

    def is_valid_bid(self, bid_: bid.Bid) -> bool:
        '''
        Bidに正しい値が格納されているか調べる．

        :param bid_ Bid: Bidが正しい値が格納されているか調べる．
        :rtype: bool
        :return: Bidに正しい値が格納されているかどうか
        '''
        for index, size in zip(bid_.get_indexes(), self.__issue_size_list):
            if index < 0 or size <= index:
                return False
        return True

    def __print_all(self):
        print('reservation_value:' + (str)(self.__reservation_value))
        print('discount_factor:' + (str)(self.__discout_factor))
        print('issue_size:' + (str)(self.__issue_size_list))
        print('evaluation', self.__evaluations_np_list)


# if __name__ == '__main__':
#     #utility_space = UtilitySpace('Domain2/Domain2_util1.xml')
#     utility_space = UtilitySpace('Jobs/Jobs_util1.xml')
#     utility_space.print_all()
