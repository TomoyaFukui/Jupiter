# coding: utf-8
from typing import List
import utilitySpace
import bid


class SummrizationOfUtilitySpace:
    def __init__(self, file_name_list: List[str]):
        self.__utility_num = len(file_name_list)
        self.__utility_space_list = []
        for i, file_name in enumerate(file_name_list):
            self.__utility_space_list.append(utilitySpace.UtilitySpace(file_name))

        #self.__calculate_distance = calculateDistance.CaluculateDistance(
        #                                self.__utility_space_list[0].get_issue_size_list(),
        #                                weight_np_list)

    def __print_all(self):
        for utility_space in self.__utility_space_list:
            utility_space.print_all()

    def is_valid_bid(self, bid_: bid.Bid) -> bool:
        return self.__utility_space_list[0].is_valid_bid(bid_)

    def get_utility_space(self, index: int):
        return self.__utility_space_list[index]

    def get_utility_num(self):
        return self.__utility_num

    def get_weight_np_list(self):
        weight_np_list = []
        for i in range(self.__utility_num):
            weight_np_list.append(self.__utility_space_list[i].get_weight_np_list())
        return weight_np_list

    def get_discount_factor_list(self):
        discount_list = []
        for utility in self.__utility_space_list:
            discount_list.append(utility.get_discount_factor())
        return discount_list

    def get_reservation_value_list(self):
        reservation_value_list = []
        for utility in self.__utility_space_list:
            reservation_value_list.append(utility.get_reservation_value())
        return reservation_value_list

if __name__ == '__main__':
    #utilities = SummrizationOfUtilitySpace('Domain2/Domain2_util1.xml',
    #                                        'Domain2/Domain2_util2.xml')
    utilities = SummrizationOfUtilitySpace('Jobs/Jobs_util1.xml',
                                            'Jobs/Jobs_util2.xml')
