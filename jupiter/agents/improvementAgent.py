# coding:utf-8
import random
import sys
import numpy as np
import time
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam
from keras.utils import plot_model
from collections import deque
from keras import backend as K
import tensorflow as tf
from scipy import stats
import copy
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../')
from jupiter.simulator import abstractAgent
from jupiter.simulator import agentAction
from jupiter.simulator import abstractUtilitySpace
from jupiter.simulator import negotiationRule
from jupiter.simulator import bid
import itertools


class ImprovementAgent(abstractAgent.AbstractAgent):
    def __init__(self, utility_space: abstractUtilitySpace.AbstractUtilitySpace,
                    negotiation_rule: negotiationRule.NegotiationRule, agent_id: int, agent_num:int):
        self.__utility_space = utility_space
        self.__rule = negotiation_rule
        self.__agent_id = agent_id
        self.__random = random
        self.__random.seed(0)
        self.__issue_size_list = self.__utility_space.get_issue_size_list()
        self.__agent_num = agent_num
        self.init_dqn()

    def init_opponents_info(self):
        self.__can_accept = False
        self.__opponents_action_list = [[]] * (self.__agent_num - 1)
        self.__opponents_bid_list = [[]] * (self.__agent_num - 1)
        self.__opponents_value_list = [[]] * (self.__agent_num - 1)

    def init_dqn(self, max_episodes=10000, max_number_of_steps=10):
        def search_values(roop_num):
            bid_ = bid.Bid(len(self.__issue_size_list))
            values = [0] * 10
            for i in range(0, roop_num):
                for i, size in enumerate(self.__issue_size_list):
                    bid_.set_issue_by_index(i, self.__random.randint(0, size-1))
                values[10 - int(self.__utility_space.get_utility(bid_)*10)] += 1
                # print(bid_.get_indexes())
            # print("values:", values)
            indexes = []
            for i, value in enumerate(values):
                if value == 0:
                    indexes.append(i)
            # print(indexes)
            return indexes
        self.DQN_MODE = 0    # 1がDQN、0がDDQNです
        # LENDER_MODE = 1 # 0は学習後も描画なし、1は学習終了後に描画する

        # env = gym.make('CartPole-v0')
        self.episode = 0
        self.num_episodes = max_episodes  # 総試行回数
        # self.goal_average_reward = 0.52  # この報酬を超えると学習終了
        self.num_consecutive_iterations = 10  # 学習完了評価をするために，用いるデータの数．平均計算を行う母数，試行回数
        self.total_reward_vec = np.zeros(self.num_consecutive_iterations)  # 各試行の報酬を格納
        self.gamma = 0.99    # 割引係数
        # islearned = 0  # 学習が終わったフラグ
        # isrender = 0  # 描画フラグ
        # ---
        hidden_size = 16               # Q-networkの隠れ層のニューロンの数
        learning_rate = 0.00001         # Q-networkの学習係数
        memory_size = 10000            # バッファーメモリの大きさ
        # self.batch_size = 32                # Q-networkを更新するバッチの大記載
        self.batch_size = 10                # Q-networkを更新するバッチの大記載

        # [5.2]Qネットワークとメモリ、Actorの生成--------------------------------------------------------
        indexes = search_values(1000)
        self.mainQN = QNetwork(hidden_size=hidden_size, action_size=10-len(indexes), learning_rate=learning_rate)     # メインのQネットワーク
        self.targetQN = QNetwork(hidden_size=hidden_size, action_size=10-len(indexes), learning_rate=learning_rate)   # 価値を計算するQネットワーク
        # plot_model(mainQN.model, to_file='Qnetwork.png', show_shapes=True)        # Qネットワークの可視化
        self.memory = Memory(max_size=memory_size)
        self.actor = Actor(copy.deepcopy(indexes))
        for i in range(0, 10):
            if i not in indexes:
                self.first_state = [int(10-i)/10, (int(10-i)-1)/10]
                # print(self.first_state)
                break

        self.max_number_of_steps = max_number_of_steps # 1試行のstep数
        print(indexes)


    def init_state(self):
        self.targetQN = self.mainQN   # 行動決定と価値計算のQネットワークをおなじにする
        self.is_initial_state = True
        self.state = np.reshape([0, 1, 0, 0], [1, 4]) #最大，最小，分散，平均時刻，(ドメインの大きさ)
        self.step_now = 0

    # def init_action(self):
    #     #state, reward, done, _ = env.step(env.action_space.sample())  # 1step目は適当な行動をとる
    #     episode_reward = 0
    #
    #     pass
    # def get_step_now(self, time:float):
    #     term_of_step = 1 / self.max_number_of_steps
    #     self.step_now = int(time / term_of_step)
    #     if self.is_initial_state:
    #         self.is_initial_state = False
    #     pass
    # def define_searching_range(self):
    #     self.y = [x*0.1 for x in range(0, 11)].reverse()

    # def make_parameters(self, point_num:int):
    #     #y = [x*0.1 for x in range(0, 11)].reverse()
    #     y = (x*0.1 for x in range(0, 11))
    #     y = list(itertools.permutations(y, 2))
    #     y = [[y1, y2] for y1, y2 in y if y1 >= y2 and y1 - y2 >= 0.35] #3だと端数でうまくいかない．端数のために3.5
    #     y.reverse()
    #     #param_list
    #     print(y)


    def get_conssetion_value(self, ):
        # if(self.__rule.get_time_now())
        pass

    def get_action(self):
        pass

    # def get_state(self):
    #     max_value = max(self.__opponents_value_list[-1])
    #     min_value = min(self.__opponents_value_list[-1])
    #     std = np.std(np.array(self.__opponents_value_list[-1]))
    #     time = self.step_now + 1 / self.max_number_of_steps / 2
    #     self.__opponents_value_list[-1] = []
    #     self.state = np.reshape([max_value, min_value, std, time], [1, 4]) #最大，最小，分散，平均時刻，(ドメインの大きさ)
    #     return self.state

    def get_state(self, value_list):
        max_value = max(value_list)
        min_value = min(value_list)
        std = np.std(np.array(value_list))
        time = self.step_now + 1 / self.max_number_of_steps / 2
        value_list = []
        return np.reshape([max_value, min_value, std, time], [1, 4]) #最大，最小，分散，平均時刻，(ドメインの大きさ)

    def get_conssetion_values(self, time, x1, x2, y_u1, y_u2, y_l1, y_l2):
        def calc_value_range(x:[float, float], y:[float, float]):
            slope, intercept, _, _, _ = stats.linregress(x, y)
            return slope, intercept
        slope_u, intercept_u = calc_value_range([x1, x2], [y_u1, y_u2])
        slope_l, intercept_l = calc_value_range([x1, x2], [y_l1, y_l2])
        return slope_u * time + intercept_u, slope_l * time + intercept_l

    def make_bid(self, upper, lower):
        bid_offer = bid.Bid(len(self.__issue_size_list))
        for i, size in enumerate(self.__issue_size_list):
            bid_offer.set_issue_by_index(i, self.__random.randint(0, size-1))
        # while lower >= self.__utility_space.get_utility_discounted(bid_offer, self.__rule.get_time_now()) or \
        #         self.__utility_space.get_utility_discounted(bid_offer, self.__rule.get_time_now()) >= upper:
        roop_num = 0
        # print("values:", lower, upper)
        while lower >= self.__utility_space.get_utility(bid_offer) or \
                self.__utility_space.get_utility(bid_offer) >= upper:
            for i, size in enumerate(self.__issue_size_list):
                bid_offer.set_issue_by_index(i, self.__random.randint(0, size-1))
            if roop_num > 1000:
                lower -= 0.1
            if roop_num > 2000:
                raise ValueError('cannnot make bid in improvementAgent')
            roop_num += 1
        # print("make bid:", lower, upper, self.__utility_space.get_utility(bid_offer))
        return bid_offer

    def make_action(self, v0:[float, float], v1:[float, float]):
        upper, lower = self.get_conssetion_values(self.__rule.get_time_now(),
            self.step_now/10, (self.step_now+1)/10, v0[0], v1[0], v0[1], v1[1])
        # print("conssettion_value:", upper, lower, self.__can_accept)
        #if lower <= self.__utility_space.get_utility_discounted(self.__opponents_bid_list[-1][-1], self.__rule.get_time_now()) \
        if self.__can_accept and \
        lower <= self.__utility_space.get_utility(self.__opponents_bid_list[-1][-1]):
            #self.get_conssetion_value() < self.__utility_space.get_utility_discounted(self.__opponent_bid, self.__opponent_action.get_time_offered()) \
            # print("accept bid:", lower, upper, self.__utility_space.get_utility(self.__opponents_bid_list[-1][-1]))
            return agentAction.Accept(self.__agent_id)
        else:
            return agentAction.Offer(self.__agent_id, self.make_bid(upper, lower))

    def send_action(self):
        def get_step_new(max_number_of_steps, time:float):
            if time == 0:
                return 0
            term_of_step = 1 / max_number_of_steps
            if time / term_of_step == 0:
                return int(time / term_of_step) - 1
            else:
                return int(time / term_of_step)

        if self.step_now == 0 and get_step_new(self.max_number_of_steps, self.__rule.get_time_now()) == 0:
            # return self.make_action([1, 0.9], [1, 0.9])
            return self.make_action(self.first_state, self.first_state)

        if self.step_now == get_step_new(self.max_number_of_steps, self.__rule.get_time_now()):
            return self.make_action(self.actor.get_action_point_from_index(self.last_action_index),
                                    self.actor.get_action_point_from_index(self.action_index))
        else:
            self.last_state = self.state.copy()
            self.state = self.get_state(self.__opponents_value_list[-1])
            self.action_index = self.actor.get_action_index(
                self.last_state, self.episode, self.mainQN)   # 時刻tでの行動を決定する
            # print("index:", self.actor.get_action_point_from_index(self.action_index))

            if self.step_now == 0:
                self.last_action_index = 0
            else:
                reward = 0.01
                self.memory.add((self.last_state, self.last_action_index, reward, self.state))     # メモリの更新する
                self.last_action_index = self.action_index
            # Qネットワークの重みを学習・更新する replay
            if (self.memory.len() > self.batch_size):
                self.mainQN.replay(self.memory, self.batch_size, self.gamma, self.targetQN)
            if self.DQN_MODE:
                self.targetQN = self.mainQN  # 行動決定と価値計算のQネットワークをおなじにする
            self.step_now = get_step_new(self.max_number_of_steps, self.__rule.get_time_now())
            return self.make_action(self.actor.get_action_point_from_index(self.last_action_index),
                                    self.actor.get_action_point_from_index(self.action_index))


    def receive_action(self, agentAction_: agentAction.AbstractAction):
        if isinstance(agentAction_, agentAction.EndNegotiation):
            self.__opponents_action_list[agentAction_.get_agent_id()].append(agentAction_)
            return
        if isinstance(agentAction_, agentAction.Offer):
            self.__can_accept = True
        self.__opponents_action_list[-1].append(agentAction_)
        self.__opponents_bid_list[-1].append(agentAction_.get_bid())
        value = self.__utility_space.get_utility_discounted(agentAction_.get_bid(), agentAction_.get_time_offered())
        self.__opponents_value_list[-1].append(value)

    # def sendAction(self):
        # if self.__opponent_action is not None and \
            # self.get_conssetion_value() < self.__utility_space.get_utility(self.__opponent_bid) \
                # and self.__is_first_turn == False:
            # # self.get_conssetion_value() < self.__utility_space.get_utility_discounted(self.__opponent_bid, self.__opponent_action.get_time_offered()) \
            # return agentAction.Accept(self.__agent_id)
#
        # bid_offer = bid.Bid(len(self.__issue_size_list))
        # for i, size in enumerate(self.__issue_size_list):
            # bid_offer.set_issue_by_index(i, self.__random.randint(0, size-1))
        # #while self.__utility_space.get_utility_discounted(bid_offer, self.__rule.get_time_now()) < self.get_conssetion_value():
        # while self.__utility_space.get_utility(bid_offer) < self.get_conssetion_value():
            # for i, size in enumerate(self.__issue_size_list):
                # bid_offer.set_issue_by_index(i, self.__random.randint(0, size-1))
        # return agentAction.Offer(self.__agent_id, bid_offer)

    def receive_start_negotiation(self):
        # print("start improve")
        self.init_opponents_info()
        self.init_state()
        self.episode += 1
        self.episode_reward = 0
        # self.reward = 0
        # self.mainQN.load()
        self.targetQN = self.mainQN   # 行動決定と価値計算のQネットワークをおなじにする
        self.action_index = None

    def receive_end_negotiation(self):
        # print("end improve")
        # print('%d Episode finished after %f time steps / mean %f' % (episode, t + 1, total_reward_vec.mean()))
        last_action = self.__opponents_action_list[-1][-1]
        if isinstance(last_action, (agentAction.Offer, agentAction.Accept)):
            reward = self.__utility_space.get_utility_discounted(last_action.get_bid(), last_action.get_time_offered())
        elif isinstance(last_action, agentAction.EndNegotiation):
            reward = self.__utility_space.get_discount_reservation_value(last_action.get_time_offered())
        else:
            raise ValueError('cannnot get reward in improvementAgent')
        reward -= self.__utility_space.get_utility(self.__opponents_bid_list[-1][0])
        # print("reward:", reward)

        self.total_reward_vec = np.hstack((self.total_reward_vec[1:], reward))  # 報酬を記録
        # 報酬を設定し、与える
        next_state = np.zeros(self.state.shape)  # 次の状態s_{t+1}はない
        self.memory.add((self.state, self.action_index, reward, next_state))     # メモリの更新する

        # if self.episode == 1000:
        #     self.mainQN.save()

    def get_name(self):
        return 'ImprovementAgent'




# [2]Q関数をディープラーニングのネットワークをクラスとして定義
class QNetwork:
    def __init__(self, learning_rate=0.01, state_size=4, action_size=10, hidden_size=10):
        # 損失関数の定義
        # 損失関数にhuber関数を使用します 参考https://github.com/jaara/AI-blog/blob/master/CartPole-DQN.py
        def huberloss(y_true, y_pred):
            err = y_true - y_pred
            cond = K.abs(err) < 1.0
            L2 = 0.5 * K.square(err)
            L1 = (K.abs(err) - 0.5)
            loss = tf.where(cond, L2, L1)  # Keras does not cover where function in tensorflow :-(
            return K.mean(loss)
        self.state_size = state_size
        self.action_size = action_size
        self.model = Sequential()
        self.model.add(Dense(hidden_size, activation='relu', input_dim=state_size))
        # self.model.add(Dense(hidden_size, activation='relu'))
        self.model.add(Dense(action_size, activation='linear'))
        self.optimizer = Adam(lr=learning_rate)  # 誤差を減らす学習方法はAdam
        # self.model.compile(loss='mse', optimizer=self.optimizer)
        self.model.compile(loss=huberloss, optimizer=self.optimizer)

    # 重みの学習
    def replay(self, memory, batch_size, gamma, targetQN):
        inputs = np.zeros((batch_size, self.state_size))
        targets = np.zeros((batch_size, self.action_size))
        mini_batch = memory.sample(batch_size)

        for i, (state_b, action_b, reward_b, next_state_b) in enumerate(mini_batch):
            inputs[i:i + 1] = state_b
            target = reward_b
            if not (next_state_b == np.zeros(state_b.shape)).all(axis=1):
                # 価値計算（DDQNにも対応できるように、行動決定のQネットワークと価値観数のQネットワークは分離）
                retmainQs = self.model.predict(next_state_b)[0]
                next_action = np.argmax(retmainQs)  # 最大の報酬を返す行動を選択する
                target = reward_b + gamma * targetQN.model.predict(next_state_b)[0][next_action]

            targets[i] = self.model.predict(state_b)    # Qネットワークの出力
            targets[i][action_b] = target               # 教師信号
            self.model.fit(inputs, targets, epochs=1, verbose=0)  # epochsは訓練データの反復回数、verbose=0は表示なしの設定

    def save(self):
        f_model = 'agents/model/'
        # print('save the architecture of a model')
        json_string = self.model.to_json()
        open(os.path.join(f_model,'dqn_model.json'), 'w').write(json_string)
        # print('save weights')
        self.model.save_weights(os.path.join(f_model,'cnn_model_weights.hdf5'))

    def load(self):
        f_model = 'agents/model/'
        # print('save the architecture of a model')
        # json_string = self.model.to_json()
        # open(os.path.join(f_model,'dqn_model.json'), 'w').write(json_string)
        # print('load weights')
        self.model.load_weights(os.path.join(f_model,'cnn_model_weights.hdf5'))


# [3]Experience ReplayとFixed Target Q-Networkを実現するメモリクラス
class Memory:
    def __init__(self, max_size=10000):
        self.buffer = deque(maxlen=max_size)

    def add(self, experience):
        self.buffer.append(experience)

    # self.bufferリストからランダムにバッチサイズの数だけ要素を抽出
    def sample(self, batch_size):
        idx = np.random.choice(np.arange(len(self.buffer)), size=batch_size, replace=False)
        return [self.buffer[ii] for ii in idx]

    def len(self):
        return len(self.buffer)


# [4]カートの状態に応じて、行動を決定するクラス
class Actor:
    def __init__(self, none_indexes):
        self.action_list = (x*0.1 for x in range(0, 11))
        self.action_list = list(itertools.permutations(self.action_list, 2))
        # self.action_list = [[y1, y2] for y1, y2 in self.action_list if y1 >= y2 and y1 - y2 >= 0.35] #3だと端数でうまくいかない．端数のために3.5
        self.action_list = [[y1, y2] for y1, y2 in self.action_list if y1 >= y2 and y1 - y2 <= 0.11]
        self.action_list.reverse()
        if none_indexes is not None:
            none_indexes.sort(reverse=True)
            for index in none_indexes:
                self.action_list.pop(index)
        self.action_num = len(self.action_list)
        # print("action_num:", self.action_list)

    def get_action_index(self, state, episode, targetQN):   # [C]ｔ＋１での行動を返す
        # 徐々に最適行動のみをとる、ε-greedy法
        #epsilon = 0.001 + 0.9 / (1.0+episode)
        # epsilon = 0.001 + 1000 / (1.0+episode)
        if episode < 900:
            epsilon = 0.001 + 300 / (1.0+episode)
        else:
            epsilon = 0
        if epsilon <= np.random.uniform(0, 1):
            # print(state, "e"*30)
            retTargetQs = targetQN.model.predict(state)[0]
            action = np.argmax(retTargetQs)  # 最大の報酬を返す行動を選択する
        else:
            # print(state, "r"*30)
            #action = np.random.choice([0, 1])  # ランダムに行動する
            action = np.random.choice(range(0, self.action_num))  # ランダムに行動する
        return action

    def get_action_point_from_index(self, index):
        return self.action_list[index]

    def get_action_point(self, state, episode, targetQN):
        return self.action_list[self.get_action_index(state, episode, targetQN)]

    # def get_action_point(self, state, episode, targetQN):
        # index = self.get_action_index(state, episode, targetQN)
        # return self.action_list[index]
