# coding: utf-8
import numpy as np
#import matplotlib as plt
from typing import List
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import copy
import time
import calculator
import agentAction
import bid
import matplotrecorder

class Display:
    def __init__(self, issue_size_list, weight_np_list, discount_list, reservation_value_list):
        self.__calculate = calculator.Calculator(issue_size_list, weight_np_list, discount_list, reservation_value_list)
        self.__agent_num = len(weight_np_list)
        self.__agent_name_list = []
        self.__save_flag = False

    def plot_initialize(self):
        if self.__agent_num == 2:
            self.__initialize_plot2()
        elif self.__agent_num == 3:
            self.__initialize_plot3()

    def __initialize_plot2(self):
        self.__fig = plt.figure()
        self.__ax = self.__fig.add_subplot(1,1,1)
        self.__ax.grid(True)
        self.__ax.set_title('utility')
        self.__ax.set_xlabel(self.__agent_name_list[0]+': utility')
        self.__ax.set_ylabel(self.__agent_name_list[1]+': utility')
        self.__ax.set_xlim(0,1)
        self.__ax.set_ylim(0,1)
        agreement_points = self.__calculate.get_agreement_points()[1]
        x = [i[0] for i in agreement_points]
        y = [i[1] for i in agreement_points]
        self.__line0, = self.__ax.plot(x, y, 'ks', label='candidate')

        parato_points = self.__calculate.get_parato_points()[1]
        x1 = [i[0] for i in parato_points]
        y1 = [i[1] for i in parato_points]
        self.__line1, = self.__ax.plot(x1, y1, 'rs', label='parato')

        self.__line2, = self.__ax.plot([2], [2], 'b.', label=self.__agent_name_list[0])
        self.__line3, = self.__ax.plot([2], [2], 'g.', label=self.__agent_name_list[1])
        self.__line4, = self.__ax.plot([2], [2], 'y.', ms=10, label='agreement')

    def __initialize_plot3(self):
        self.__fig = plt.figure(figsize=(12,8))
        self.__fig.subplots_adjust(left=0.05, bottom=0.1, right=0.95, top=0.90, wspace=0.2, hspace=0.6)
        self.__ax_list = []
        self.__ax_list.append(plt.subplot2grid((2,2),(0,0)))
        self.__ax_list.append(plt.subplot2grid((2,2),(1,0)))
        self.__ax_list.append(plt.subplot2grid((2,2),(0,1)))
        agreement_points = self.__calculate.get_agreement_points()[1]
        parato_points = self.__calculate.get_parato_points()[1]
        self.__line_list = [[], [], [], []]
        size = 10
        for i, ax in enumerate(self.__ax_list):
            ax.grid(True)
            #ax.set_title('id:'+str(i%3)+'- id:'+str((i+1)%3))
            #ax.set_xlabel('id:'+str((i)%3))
            #ax.set_ylabel('id:'+str((i+1)%3))
            ax.set_title(self.__agent_name_list[i%3]+' - '+self.__agent_name_list[(i+1)%3])
            ax.set_xlabel(self.__agent_name_list[i%3])
            ax.set_ylabel(self.__agent_name_list[(i+1)%3])
            ax.set_xlim(0,1)
            ax.set_ylim(0,1)

            x = [j[i%3] for j in agreement_points]
            y = [j[(i+1)%3] for j in agreement_points]
            self.__line_list[i].append(ax.plot(x, y, 'ks', label='candidate')[0])

            x = [j[i%3] for j in parato_points]
            y = [j[(i+1)%3] for j in parato_points]
            self.__line_list[i].append(ax.plot(x, y, 'cs', label='parato')[0])
            self.__line_list[i].append(ax.plot([2], [2], 'r.', ms=size, label=self.__agent_name_list[0])[0])
            self.__line_list[i].append(ax.plot([2], [2], 'g.', ms=size, label=self.__agent_name_list[1])[0])
            self.__line_list[i].append(ax.plot([2], [2], 'b.', ms=size, label=self.__agent_name_list[2])[0])
            self.__line_list[i].append(ax.plot([2], [2], 'y.', ms=size, label='agreement')[0])

        self.__ax_list.append(plt.subplot2grid((2,2),(1,1)))
        self.__ax_list[3].set_title('empty')
        self.__ax_list[3].set_xlim(0,1)
        self.__ax_list[3].set_ylim(0,1)
        self.__line_list[3].append(self.__ax_list[3].plot([2], [2], 'ks', label='candidate')[0])
        self.__line_list[3].append(self.__ax_list[3].plot([2], [2], 'cs', label='parato')[0])
        self.__line_list[3].append(self.__ax_list[3].plot([2], [2], 'r.', ms=size, label=self.__agent_name_list[0])[0])
        self.__line_list[3].append(self.__ax_list[3].plot([2], [2], 'g.', ms=size, label=self.__agent_name_list[1])[0])
        self.__line_list[3].append(self.__ax_list[3].plot([2], [2], 'b.', ms=size, label=self.__agent_name_list[2])[0])
        self.__line_list[3].append(self.__ax_list[3].plot([2], [2], 'y.', ms=size, label='agreement')[0])

    def __display_plot3_update(self, action_list):
        self.__ax_list[3].legend(loc='upper right')
        for i in range(self.__agent_num):
            bid_list = [[x.get_bid().get_indexes(), x.get_time_offered()] for x in action_list
                            if (isinstance(x, agentAction.Offer) or isinstance(x, agentAction.Accept))
                            and x.get_agent_id() == i]
            value_list = self.__calculate.get_utilities(bid_list)
            util_list = [[i[0] for i in value_list], [i[1] for i in value_list], [i[2] for i in value_list]]

            for j, lines in enumerate(self.__line_list):
                if j == 3:
                    continue
                lines[i+2].set_data(util_list[j%3], util_list[(j+1)%3])
        plt.pause(.1)
        if self.__save_flag:
            matplotrecorder.save_frame()

    def __display_plot3_update_end(self, action_list, get_agreement: [bool, agentAction.AbstractAction]):
        self.__display_plot3_update(action_list)
        if get_agreement[0] == True and isinstance(get_agreement[1], agentAction.EndNegotiation):
            agreement = self.__calculate.get_discount_reservation_value_list(get_agreement[1].get_time_offered())
            for i, lines in enumerate(self.__line_list):
                if i == 3:
                    continue
                lines[5].set_data(agreement[i%3], agreement[(i+1)%3])
        elif get_agreement[0] == True:
            agreement = get_agreement[1].get_bid().get_indexes()
            agreement = self.__calculate.get_utility(agreement, get_agreement[1].get_time_offered())
            for i, lines in enumerate(self.__line_list):
                if i == 3:
                    continue
                lines[5].set_data(agreement[i%3], agreement[(i+1)%3])
        self.__ax_list[3].legend(loc='upper right')
        plt.pause(.001)
        if self.__save_flag:
            matplotrecorder.save_frame()
            matplotrecorder.save_movie("movies/animation.gif", 0.1)

    def __display_plot2_update(self, action_list):
        for i in range(self.__agent_num):
            bid_list = [[x.get_bid().get_indexes(), x.get_time_offered()] for x in action_list
                            if (isinstance(x, agentAction.Offer) or isinstance(x, agentAction.Accept))
                            and x.get_agent_id() == i]
            value_list = self.__calculate.get_utilities(bid_list)
            x = [i[0] for i in value_list]
            y = [i[1] for i in value_list]
            if i == 0:
                self.__line2.set_data(x, y)
            elif i == 1:
                self.__line3.set_data(x, y)

        self.__ax.legend(loc='upper right')
        plt.pause(.001)
        if self.__save_flag:
            matplotrecorder.save_frame()

    def __display_plot2_update_end(self, action_list, get_agreement: [bool, agentAction.AbstractAction]):
        self.__display_plot2_update(action_list)
        if get_agreement[0] == True and isinstance(get_agreement[1], agentAction.EndNegotiation):
            agreement = self.__calculate.get_discount_reservation_value_list(get_agreement[1].get_time_offered())
            self.__line4.set_data(agreement[0], agreement[1])
        elif get_agreement[0] == True:
            agreement = get_agreement[1].get_bid().get_indexes()
            agreement = self.__calculate.get_utility(agreement, get_agreement[1].get_time_offered())
            self.__line4.set_data(agreement[0], agreement[1])

        self.__ax.legend(loc='upper right')
        plt.pause(.001)
        if self.__save_flag:
            matplotrecorder.save_frame()
            matplotrecorder.save_movie("movies/animation.gif", 0.1)

    def show(self):
        plt.show()

    def update(self, action_list):
        if self.__agent_num == 2:
            self.__display_plot2_update(action_list)
        elif self.__agent_num == 3:
            self.__display_plot3_update(action_list)

    def update_end(self, action_list, get_agreement):
        if self.__agent_num == 2:
            self.__display_plot2_update_end(action_list, get_agreement)
        elif self.__agent_num == 3:
            self.__display_plot3_update_end(action_list, get_agreement)

    def set_agent_name(self, name):
        self.__agent_name_list.append(name)

    def get_parato_distance(self, action):
        return self.__calculate.get_parato_distance(action.get_bid().get_indexes(), action.get_time_offered())

    def set_save_flag(self):
        self.__save_flag = True

    # def display_agreement_points(self):
    #     fig = plt.figure()
    #     ax = fig.add_subplot(1,1,1)
    #     agreement_points = self.__calculate.get_agreement_points()[1]
    #     x = [point[0] for point in agreement_points]
    #     y = [point[1] for point in agreement_points]
    #     ax.scatter(x,y)
    #     ax.set_title('first scatter plot')
    #     ax.set_xlabel('x')
    #     ax.set_ylabel('y')
    #     plt.show()

    # def display_points_2d(self, action_list):
        # fig = plt.figure()
        # ax = fig.add_subplot(1,1,1)
#
        # agreement_points = self.__calculate.get_agreement_points()[1]
        # x = [i[0] for i in agreement_points]
        # y = [i[1] for i in agreement_points]
        # ax.scatter(x, y, c='black', marker='s', label='candidate')
#
        # for i in range(self.__agent_num):
            # bid_list = [x.get_bid().get_indexes() for x in action_list
                            # if (isinstance(x, agentAction.Offer) or isinstance(x, agentAction.Accept))
                            # and x.get_agent_id() == i]
            # value_list = self.__calculate.get_utilities(bid_list)
            # x = [i[0] for i in value_list]
            # y = [i[1] for i in value_list]
            # if i == 0:
                # ax.scatter(x, y, c='red', s=20, label='id:'+str(i))
            # elif i == 1:
                # ax.scatter(x, y, c='blue', s=30, label='id:'+str(i))
            # elif i == 2:
                # ax.scatter(x, y, c='green', s=10, label='id:'+str(i))
#
#        ここおかしい
        # if not isinstance(action_list[-1], agentAction.EndNegotiation):
            # agreement = action_list[-1].get_bid().get_indexes()
            # agreement = self.__calculate.get_utility(agreement)
            # ax.scatter(agreement[0], agreement[1], c='yellow', marker='o', s=50, label='agreement')
#
#        ax.set_title('first scatter plot')
        # ax.set_xlabel('id:0 utility')
        # ax.set_ylabel('id:1 utility')
        # ax.grid(True)
        # ax.set_xlim(0,1)
        # ax.set_ylim(0,1)
        # ax.legend(loc='upper right')
        # plt.show()
#
    # def display_points_3d(self, action_list):
        # self.__fig = plt.figure()
        # self.__ax = Axes3D(fig)
#
        # agreement_points = self.__calculate.get_agreement_points()[1]
        # x = [i[0] for i in agreement_points]
        # y = [i[1] for i in agreement_points]
        # z = [i[2] for i in agreement_points]
        # ax.scatter(x, y, z, c='black', marker='s', s=5, label='candidate')
#
        # for i in range(self.__agent_num):
            # bid_list = [x.get_bid().get_indexes() for x in action_list
                            # if (isinstance(x, agentAction.Offer) or isinstance(x, agentAction.Accept))
                            # and x.get_agent_id() == i]
            # value_list = self.__calculate.get_utilities(bid_list)
            # x = [i[0] for i in value_list]
            # y = [i[1] for i in value_list]
            # z = [i[2] for i in value_list]
            # if i == 0:
                # ax.scatter(x, y, z, c='red', marker='o', s=20, alpha=0.2, label='id:'+str(i))
            # elif i == 1:
                # ax.scatter(x, y, z, c='blue', marker='o', s=30, alpha=0.3, label='id:'+str(i))
            # elif i == 2:
                # ax.scatter(x, y, z, c='green', marker='o', s=10, alpha=0.4, label='id:'+str(i))
#
        # if not isinstance(action_list[-1], agentAction.EndNegotiation):
            # agreement = action_list[-1].get_bid().get_indexes()
            # agreement = self.__calculate.get_utility(agreement)
            # ax.scatter(agreement[0], agreement[1], agreement[2], c='yellow', marker='o', s=100, label='agreement')
            # print(agreement)
#
        # ax.set_xlabel('id:0 utility')
        # ax.set_ylabel('id:1 utility')
        # ax.set_zlabel('id:2 utility')
        # ax.grid(True)
        # ax.set_xlim(0,1)
        # ax.set_ylim(0,1)
        # ax.set_zlim(0,1)
        # ax.legend(loc='upper right')
        # plt.show()
