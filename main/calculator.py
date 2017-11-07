# coding: utf-8
from typing import List
import numpy as np
import copy
import bid

#パレート距離やナッシュ距離を計算する
# JupiterからGUIクラスを通じてこのクラスを使う
class Calculator:
    def __init__(self, issue_size_list: List[int], weight_np_list: List[np.array], discount_list: List[float], reservation_value_list: List[float]):
        self.__size_list = issue_size_list
        self.__evaluations_np_list = weight_np_list
        self.__discout_factor_list = discount_list
        self.__reservation_list = reservation_value_list
        self.__agreement_point_temp = [0]*len(issue_size_list)
        #indexを格納する
        self.agreement_points = []
        self.parato_points = []
        self.nash_points = []
        #効用値を格納する
        self.agreement_points_utility_value = []
        self.parato_points_utility_value = []
        self.nash_points_utility_value = []
        self.__calculate_agreement_points()
        self.__calculate_parato_points()
        self.__calculate_nash_points()

    def __calculate_agreement_points(self):
        self.__calculate_agreement_point(0)

    def __calculate_agreement_point(self, i: int):
        if i != len(self.__size_list):
            for j in range(self.__size_list[i]):
                self.__agreement_point_temp[i] = j
                self.__calculate_agreement_point(i+1)
        else:
            self.agreement_points.append(copy.deepcopy(self.__agreement_point_temp))
            value_list = []
            for player_index in range(len(self.__evaluations_np_list)):
                value = 0
                for evaluations_np, index in zip(self.__evaluations_np_list[player_index], self.__agreement_point_temp):
                    value += evaluations_np[index]
                value_list.append(value)
            self.agreement_points_utility_value.append(copy.deepcopy(value_list))

    def __calculate_parato_points(self):
        self.parato_points = copy.deepcopy(self.agreement_points)
        self.parato_points_utility_value = copy.deepcopy(self.agreement_points_utility_value)
        i = 0
        while i < len(self.parato_points_utility_value):
            j = 0
            while j < len(self.parato_points_utility_value):
                if i == j:
                    pass
                elif True not in set(map(lambda x, y: x >= y, self.parato_points_utility_value[i], self.parato_points_utility_value[j])):
                    self.parato_points.pop(i)
                    self.parato_points_utility_value.pop(i)
                    i -= 1
                    break
                elif True not in set(map(lambda x, y: x <= y, self.parato_points_utility_value[i], self.parato_points_utility_value[j])):
                    self.parato_points.pop(j)
                    self.parato_points_utility_value.pop(j)
                    continue
                j += 1
            i += 1

    # 計算の仕方おかしい
    # それぞれの(utility - reservation_value)の総積が最大となる点
    # 使わない
    def __calculate_nash_points(self):
        value_max = 0
        for utility_list, parato_point in zip(self.parato_points_utility_value, self.parato_points):
            value_temp = 1
            for utility, reservation in zip(utility_list, self.__reservation_list):
                value_temp *= (utility - reservation)
            if value_max < value_temp:
                value_max = value_temp
                self.nash_points = [parato_point]
                self.nash_points_utility_value = [utility_list]
            elif value_max == value_temp:
                self.nash_points.append(parato_point)
                self.nash_points_utility_value.append(utility_list)
        #print(self.nash_points_utility_value)
        #for point, value in zip(self.parato_points, self.parato_points_utility_value):
        #    if min_gap > max(value) - min(value):
        #        min_gap = max(value) - min(value)
        #        self.nash_points = []
        #        self.nash_points.append(point)
        #        self.nash_points_utility_value = []
        #        self.nash_points_utility_value.append(value)
        #    elif min_gap == max(value) - min(value):
        #        min_gap = max(value) - min(value)
        #        self.nash_points.append(point)
        #        self.nash_points_utility_value.append(value)

    def get_agreement_points(self):
        return (self.agreement_points, self.agreement_points_utility_value)

    def get_parato_points(self):
        return (self.parato_points, self.parato_points_utility_value)

    def get_utilities(self, index_list_list: [[[int], float]]):
        value_list_list = []
        for index_time_list in index_list_list:
            index_list = index_time_list[0]
            value_list = []
            for player_index in range(len(self.__evaluations_np_list)):
                value = 0
                for evaluations_np, index in zip(self.__evaluations_np_list[player_index], index_list):
                    value += evaluations_np[index]
                value *= pow(self.__discout_factor_list[player_index], index_time_list[1])
                value_list.append(value)
            value_list_list.append(copy.deepcopy(value_list))
        return value_list_list

    def get_utility(self, index_list: [int], time=0.0, is_discounted=True):
        #print(index_time_list)
        value_list = []
        for player_index in range(len(self.__evaluations_np_list)):
            value = 0
            for evaluations_np, index in zip(self.__evaluations_np_list[player_index], index_list):
                value += evaluations_np[index]
            if is_discounted:
                value *= pow(self.__discout_factor_list[player_index], time)
            value_list.append(value)
        return value_list

    def get_discount_reservation_value_list(self, time):
        ret_list = []
        for reservation, discount in zip(self.__reservation_list, self.__discout_factor_list):
            ret_list.append(value * pow(discount, time))
        return ret_list

    def test(self):
        bid_ = bid.Bid(len(self.__size_list))
        print("parato distance:", self.get_parato_distance(bid_.get_indexes()))
        print("nash distance:", self.get_nash_distance(bid_.get_indexes()))

    def get_parato_distance(self, index_list: List[int], time:float) -> float:
        point_np = np.array(self.get_utility(index_list, time), dtype=np.float32)
        parato_points_np = np.array(self.parato_points_utility_value, dtype=np.float32)
        min_distance = 9999
        point = []
        for i in range(len(self.parato_points)):
            if min_distance > np.linalg.norm(point_np - parato_points_np[i]):
                min_distance = np.linalg.norm(point_np - parato_points_np[i])
                point = self.parato_points_utility_value[i]
        return min_distance

    def get_nash_distance(self, index_list: List[int]) -> float:
        point_np = np.array(self.get_utility(index_list, is_discounted=False), dtype=np.float32)
        nash_points_np = np.array(self.nash_points_utility_value, dtype=np.float32)
        return np.linalg.norm(point_np - nash_points_np[0])
